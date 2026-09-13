<?php
/**
 * Plugin Name: LMT Bot Cleanup
 * Description: One-click bot user cleanup. Go to Users > Bot Cleanup to scan and delete. DELETE THIS PLUGIN AFTER USE.
 * Version: 1.0.0
 * Author: LMT
 */

if (!defined('ABSPATH')) exit;

add_action('admin_menu', function () {
    add_users_page('Bot Cleanup', 'Bot Cleanup', 'manage_options', 'lmt-bot-cleanup', 'lmt_bot_cleanup_page');
});

function lmt_is_bot_user($user) {
    // Skip admins, keymaster, contributor roles
    $safe_roles = array('administrator', 'keymaster', 'contributor', 'editor', 'author');
    foreach ($safe_roles as $role) {
        if (in_array($role, (array) $user->roles)) return false;
    }

    // Skip BuddyBoss demo users
    if (strpos($user->user_login, 'bb-') === 0) return false;

    // Skip known safe usernames
    $safe_users = array('brian', 'brian1', 'b', 'barbara', 'bennytest2', 'bhtechmail');
    if (in_array(strtolower($user->user_login), $safe_users)) return false;

    $name = $user->display_name;

    // Bot pattern: display name is 15+ chars with no spaces (gibberish)
    if (strlen($name) >= 15 && strpos($name, ' ') === false && preg_match('/[A-Z]/', $name) && preg_match('/[a-z]/', $name)) {
        return true;
    }

    // Bot pattern: name contains crypto/BTC spam
    if (preg_match('/BTC|BALANCE|DOLLARS|crypto|graph\.org/i', $name)) {
        return true;
    }

    // Bot pattern: username has lots of dots like an.t.ho.n.ie.s
    if (substr_count($user->user_login, '.') >= 4) {
        return true;
    }

    return false;
}

function lmt_bot_cleanup_page() {
    if (!current_user_can('manage_options')) return;

    echo '<div class="wrap"><h1>LMT Bot Cleanup</h1>';

    // Handle deletion
    if (isset($_POST['lmt_delete_bots']) && wp_verify_nonce($_POST['_wpnonce'], 'lmt_delete_bots')) {
        $bot_ids = isset($_POST['bot_ids']) ? array_map('intval', $_POST['bot_ids']) : array();
        $current_user_id = get_current_user_id();
        $deleted = 0;

        require_once(ABSPATH . 'wp-admin/includes/user.php');

        foreach ($bot_ids as $id) {
            if ($id === $current_user_id) continue;
            if (wp_delete_user($id, $current_user_id)) {
                $deleted++;
            }
        }

        echo '<div class="notice notice-success"><p><strong>' . $deleted . ' bot accounts deleted.</strong> Their content was reassigned to your account.</p></div>';
    }

    // Scan users
    $all_users = get_users(array('number' => -1));
    $bots = array();

    foreach ($all_users as $user) {
        if (lmt_is_bot_user($user)) {
            $bots[] = $user;
        }
    }

    if (empty($bots)) {
        echo '<p>No bot accounts detected. You\'re clean!</p>';
        echo '<p><strong>You can now deactivate and delete this plugin.</strong></p>';
        echo '</div>';
        return;
    }

    echo '<p>Found <strong>' . count($bots) . ' suspected bot accounts</strong>. Review the list below and click Delete to remove them all.</p>';
    echo '<form method="post">';
    wp_nonce_field('lmt_delete_bots');

    echo '<table class="widefat striped"><thead><tr>';
    echo '<th>Username</th><th>Display Name</th><th>Email</th><th>Role</th><th>Registered</th>';
    echo '</tr></thead><tbody>';

    foreach ($bots as $bot) {
        echo '<tr>';
        echo '<td>' . esc_html($bot->user_login) . '</td>';
        echo '<td>' . esc_html($bot->display_name) . '</td>';
        echo '<td>' . esc_html($bot->user_email) . '</td>';
        echo '<td>' . esc_html(implode(', ', $bot->roles)) . '</td>';
        echo '<td>' . esc_html($bot->user_registered) . '</td>';
        echo '</tr>';
        echo '<input type="hidden" name="bot_ids[]" value="' . intval($bot->ID) . '">';
    }

    echo '</tbody></table>';
    echo '<br><input type="submit" name="lmt_delete_bots" class="button button-primary button-hero" value="Delete All ' . count($bots) . ' Bot Accounts" onclick="return confirm(\'Delete ' . count($bots) . ' bot accounts? This cannot be undone.\')">';
    echo '</form>';
    echo '<p><em>Their content will be reassigned to your admin account. This cannot be undone.</em></p>';
    echo '</div>';
}
