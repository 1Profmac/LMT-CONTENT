<?php
/**
 * Plugin Name: LMT Join Now Form
 * Description: Adds [lmt_join_form] shortcode to the join-now page. One form submission creates a WordPress account, enrolls in LearnDash course 1091, applies the pioneer-active Mailchimp tag, and redirects to Lesson 1.
 * Version: 1.5.0
 * Author: LMT
 * Requires at least: 5.0
 * Requires PHP: 7.2
 */

if (!defined('ABSPATH')) {
    exit;
}

class LMT_Join_Now_Form {

    // ============================================
    // CONFIGURATION
    // ============================================
    private $course_id            = 1091;
    private $lesson_url           = 'https://50plustechbridge.com/courses/50techbridge/lessons/introduction-to-digital-skills-agetech/';
    private $mailchimp_api_key    = 'REDACTED';
    private $mailchimp_audience_id = '5ed5071656';
    private $recaptcha_site_key   = '6Lf9Hw0tAAAAACx73cqd3zGuLhYRpG4sV3rEp2Qp';
    private $recaptcha_secret_key = '6Lf9Hw0tAAAAHKeY7AIt8wED92_7EIhq2Z64o7f';
    // ============================================

    private $api_endpoint;

    public function __construct() {
        $dc                 = substr($this->mailchimp_api_key, strpos($this->mailchimp_api_key, '-') + 1);
        $this->api_endpoint = "https://{$dc}.api.mailchimp.com/3.0/";

        add_action('init', array($this, 'handle_submission'), 5);
        add_shortcode('lmt_join_form', array($this, 'render_form'));
        add_action('wp_head', array($this, 'maybe_inject_css'));
    }

    // ================================================================
    // FORM PROCESSING
    // ================================================================

    public function handle_submission() {
        if (empty($_POST['lmt_nonce'])) {
            return;
        }

        if (!wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['lmt_nonce'])), 'lmt_join_submit')) {
            wp_die('Security check failed. Please go back and try again.');
        }

        $first_name = sanitize_text_field(wp_unslash($_POST['lmt_first_name'] ?? ''));
        $email      = sanitize_email(wp_unslash($_POST['lmt_email'] ?? ''));
        $password   = wp_unslash($_POST['lmt_password'] ?? '');

        error_log("LMT Join: Submission received — name={$first_name} email={$email}");

        // ---- Validate ----
        $errors = array();

        if (empty($first_name)) {
            $errors[] = 'Please enter your first name.';
        }
        if (empty($email) || !is_email($email)) {
            $errors[] = 'Please enter a valid email address.';
        }
        if (strlen($password) < 8) {
            $errors[] = 'Password must be at least 8 characters long.';
        }
        if (!empty($email) && is_email($email) && email_exists($email)) {
            $login_url = wp_login_url($this->lesson_url);
            $errors[]  = 'An account with this email already exists. <a href="' . esc_url($login_url) . '">Log in here</a>';
        }

        // ---- Honeypot check (hidden field bots fill in) ----
        $honeypot = sanitize_text_field($_POST['lmt_website'] ?? '');
        if (!empty($honeypot)) {
            error_log('LMT Join: Honeypot triggered — likely bot.');
            $errors[] = 'Submission blocked.';
        }

        // reCAPTCHA removed — honeypot provides bot protection

        if (!empty($errors)) {
            $this->store_errors($errors, $first_name, $email);
            return;
        }

        // ---- Build a unique username from the email ----
        $base = sanitize_user(strstr($email, '@', true), true);
        if (empty($base)) {
            $base = 'user';
        }
        $username = $base;
        $i        = 1;
        while (username_exists($username)) {
            $username = $base . $i++;
        }

        // ---- Create the WordPress / BuddyBoss user ----
        $user_id = wp_insert_user(array(
            'user_login'   => $username,
            'user_email'   => $email,
            'user_pass'    => $password,
            'first_name'   => $first_name,
            'display_name' => $first_name,
            'role'         => 'subscriber',
        ));

        if (is_wp_error($user_id)) {
            error_log('LMT Join: wp_insert_user failed — ' . $user_id->get_error_message());
            $this->store_errors(array('Account creation failed: ' . $user_id->get_error_message()), $first_name, $email);
            return;
        }

        error_log("LMT Join: WP user created — user_id={$user_id} username={$username} email={$email}");

        // ---- LearnDash enrollment ----
        $this->enroll_learndash($user_id);

        // ---- Mailchimp: subscribe + tag ----
        $this->mailchimp_subscribe_and_tag($email, $first_name, 'pioneer-active');

        // ---- Log the new user in ----
        wp_set_current_user($user_id);
        wp_set_auth_cookie($user_id, false);
        do_action('wp_login', $username, get_userdata($user_id));
        error_log("LMT Join: User {$user_id} logged in. Redirecting to lesson.");

        // ---- Redirect to Lesson 1 ----
        wp_redirect($this->lesson_url);
        exit;
    }

    // ================================================================
    // LEARNDASH ENROLLMENT
    // ================================================================

    private function enroll_learndash($user_id) {
        error_log("LMT Join [LD]: Enrolling user_id={$user_id} in course_id={$this->course_id}");

        if (function_exists('ld_update_course_access')) {
            $result = ld_update_course_access($user_id, $this->course_id, false);
            error_log("LMT Join [LD]: ld_update_course_access result: " . var_export($result, true));
        } else {
            error_log("LMT Join [LD]: ld_update_course_access() not found — using meta fallback only.");
        }

        $meta_key = 'course_' . $this->course_id . '_access_from';
        if (!get_user_meta($user_id, $meta_key, true)) {
            update_user_meta($user_id, $meta_key, time());
            error_log("LMT Join [LD]: Meta fallback written — {$meta_key}");
        }

        update_user_meta($user_id, 'lmt_ld_enrolled', '1');
    }

    // ================================================================
    // MAILCHIMP
    // ================================================================

    private function mailchimp_subscribe_and_tag($email, $first_name, $tag) {
        $email           = strtolower(trim($email));
        $subscriber_hash = md5($email);

        $auth = array(
            'Authorization' => 'Basic ' . base64_encode('user:' . $this->mailchimp_api_key),
            'Content-Type'  => 'application/json',
        );

        $member_url  = $this->api_endpoint . "lists/{$this->mailchimp_audience_id}/members/{$subscriber_hash}";
        $upsert_resp = wp_remote_request($member_url, array(
            'method'  => 'PUT',
            'headers' => $auth,
            'body'    => json_encode(array(
                'email_address' => $email,
                'status_if_new' => 'subscribed',
                'merge_fields'  => array('FNAME' => $first_name),
            )),
            'timeout' => 15,
        ));

        if (is_wp_error($upsert_resp)) {
            error_log("LMT Join [MC]: Upsert error for {$email}: " . $upsert_resp->get_error_message());
        } else {
            $upsert_code = wp_remote_retrieve_response_code($upsert_resp);
            error_log("LMT Join [MC]: Upsert response {$upsert_code} for {$email}");
            if ($upsert_code >= 400) {
                error_log("LMT Join [MC]: Upsert body: " . wp_remote_retrieve_body($upsert_resp));
            }
        }

        $tags_url = $this->api_endpoint . "lists/{$this->mailchimp_audience_id}/members/{$subscriber_hash}/tags";
        $tag_resp = wp_remote_post($tags_url, array(
            'headers' => $auth,
            'body'    => json_encode(array(
                'tags' => array(array('name' => $tag, 'status' => 'active')),
            )),
            'timeout' => 15,
        ));

        if (is_wp_error($tag_resp)) {
            error_log("LMT Join [MC]: Tag error for {$email}: " . $tag_resp->get_error_message());
            return false;
        }

        $tag_code = wp_remote_retrieve_response_code($tag_resp);
        if ($tag_code !== 204) {
            error_log("LMT Join [MC]: Tag failed (code {$tag_code}): " . wp_remote_retrieve_body($tag_resp));
            return false;
        }

        error_log("LMT Join [MC]: Tag '{$tag}' applied to {$email}.");
        return true;
    }

    // ================================================================
    // ERROR STORAGE / RETRIEVAL
    // ================================================================

    private function store_errors($errors, $first_name, $email) {
        $token = wp_generate_password(16, false);
        set_transient('lmt_join_err_' . $token, array(
            'errors' => $errors,
            'values' => array('first_name' => $first_name, 'email' => $email),
        ), 120);
        $referer = wp_get_referer() ?: home_url('/join-now/');
        wp_redirect(add_query_arg('lmt_t', $token, $referer));
        exit;
    }

    private function get_errors() {
        if (empty($_GET['lmt_t'])) {
            return array('errors' => array(), 'values' => array('first_name' => '', 'email' => ''));
        }
        $token = sanitize_text_field($_GET['lmt_t']);
        $data  = get_transient('lmt_join_err_' . $token);
        if ($data) {
            delete_transient('lmt_join_err_' . $token);
            return $data;
        }
        return array('errors' => array(), 'values' => array('first_name' => '', 'email' => ''));
    }

    // ================================================================
    // SHORTCODE / FORM HTML
    // ================================================================

    public function render_form() {
        if (is_user_logged_in()) {
            return '<div class="lmt-notice">You already have an account. <a href="' . esc_url($this->lesson_url) . '">Go to your lessons</a></div>';
        }

        $data       = $this->get_errors();
        $errors     = $data['errors'];
        $first_name = esc_attr($data['values']['first_name'] ?? '');
        $email      = esc_attr($data['values']['email'] ?? '');

        ob_start(); ?>

        <div class="lmt-form-wrap">

            <?php if (!empty($errors)) : ?>
                <div class="lmt-errors" role="alert">
                    <?php foreach ($errors as $e) : ?>
                        <p><?php echo wp_kses($e, array('a' => array('href' => array()))); ?></p>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>

            <form id="lmt-join-form" method="post" novalidate>
                <?php wp_nonce_field('lmt_join_submit', 'lmt_nonce'); ?>

                <!-- Honeypot — hidden from humans, bots fill it in -->
                <div style="position:absolute;left:-9999px;top:-9999px;" aria-hidden="true">
                    <input type="text" name="lmt_website" tabindex="-1" autocomplete="off">
                </div>

                <div class="lmt-field">
                    <label for="lmt_first_name">First Name</label>
                    <input
                        type="text"
                        id="lmt_first_name"
                        name="lmt_first_name"
                        value="<?php echo $first_name; ?>"
                        placeholder="Your first name"
                        required
                        autocomplete="given-name"
                    >
                </div>

                <div class="lmt-field">
                    <label for="lmt_email">Email Address</label>
                    <input
                        type="email"
                        id="lmt_email"
                        name="lmt_email"
                        value="<?php echo $email; ?>"
                        placeholder="you@example.com"
                        required
                        autocomplete="email"
                    >
                </div>

                <div class="lmt-field">
                    <label for="lmt_password">
                        Password
                        <span class="lmt-hint">(min. 8 characters)</span>
                    </label>
                    <input
                        type="password"
                        id="lmt_password"
                        name="lmt_password"
                        placeholder="Create a password"
                        required
                        minlength="8"
                        autocomplete="new-password"
                    >
                </div>

                <div class="lmt-field">
                    <button type="submit" id="lmt-btn" class="lmt-btn">
                        Start Your Free Lessons &rarr;
                    </button>
                </div>

                <p class="lmt-legal">
                    By signing up you agree to receive emails from Learn More Technologies.
                    Unsubscribe any time.
                </p>

            </form>
        </div>

        <script>
        (function () {
            var form = document.getElementById('lmt-join-form');
            var btn  = document.getElementById('lmt-btn');
            if (!form || !btn) return;

            form.addEventListener('submit', function (e) {
                if (!form.checkValidity()) return;
                btn.disabled    = true;
                btn.textContent = 'Creating your account\u2026';
            });
        }());
        </script>

        <?php
        return ob_get_clean();
    }

    // ================================================================
    // CSS
    // ================================================================

    public function maybe_inject_css() {
        if (!is_page('join-now')) {
            return;
        }
        echo '<style id="lmt-join-styles">';
        echo '.lmt-form-wrap{max-width:460px;margin:0 auto}';
        echo '</style>';
    }
}

new LMT_Join_Now_Form();
