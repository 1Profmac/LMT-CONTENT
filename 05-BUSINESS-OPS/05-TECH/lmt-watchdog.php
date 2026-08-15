<?php
/**
 * LMT Systems Watchdog v3.0
 * Runs daily via Bluehost cron job.
 * Monitors: Mailchimp, WordPress, LearnDash, Signup Form, All Pages
 * Emails one daily report with stats + alerts.
 *
 * v3.0 Changes (May 11, 2026):
 * - Fixed bot detection to reduce false positives (hCaptcha now active)
 * - Added real subscriber count (excludes unsubscribed/cleaned)
 * - Added social media links to report
 * - Improved Mailchimp stats reporting
 * - Added Jetpack Social / Buffer / Metricool links
 */

// ============================================
// CONFIGURATION
// ============================================
$mailchimp_api_key   = 'REDACTED';
$mailchimp_audience  = '5ed5071656';
$mailchimp_dc        = 'us20';
$alert_email         = 'hello@learnmoretechnologies.com';
$from_email          = 'watchdog@learnmoretechnologies.com';
$site_base           = 'https://learnmoretechnologies.com';

// Pages to monitor (name => URL)
$pages_to_check = [
    'Homepage'           => $site_base . '/',
    'Signup Form'        => $site_base . '/start-free-lesson/',
    'Course Page'        => $site_base . '/courses/50techbridge/',
    'Lesson 1'           => $site_base . '/courses/50techbridge/lessons/introduction-to-digital-skills-agetech/',
    'Login Page'         => $site_base . '/wp-login.php',
];

// WordPress REST API endpoint
$wp_api = $site_base . '/wp-json/wp/v2';

// ============================================
// HELPERS
// ============================================
function mc_api($endpoint, $api_key, $dc) {
    $ch = curl_init("https://{$dc}.api.mailchimp.com/3.0/{$endpoint}");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 15,
        CURLOPT_HTTPHEADER     => [
            'Authorization: Basic ' . base64_encode('user:' . $api_key),
            'Content-Type: application/json',
        ],
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return ['code' => $code, 'data' => json_decode($resp, true)];
}

function ping_site($url) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 15,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_USERAGENT      => 'LMT-Watchdog/3.0',
    ]);
    $body = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $time = round(curl_getinfo($ch, CURLINFO_TOTAL_TIME), 2);
    curl_close($ch);
    return ['code' => $code, 'body' => $body, 'time' => $time];
}

// ============================================
// INITIALIZE
// ============================================
$issues = [];
$stats  = [];

// ============================================
// 1. MAILCHIMP — AUTOMATION STATUS
// ============================================
$auto_resp = mc_api('automations', $mailchimp_api_key, $mailchimp_dc);
if ($auto_resp['code'] === 200 && !empty($auto_resp['data']['automations'])) {
    foreach ($auto_resp['data']['automations'] as $auto) {
        $name   = $auto['settings']['title'] ?? 'Unknown';
        $status = $auto['status'] ?? 'unknown';
        $stats[] = "Automation: {$name} — {$status}";
        if ($status !== 'sending') {
            $issues[] = "AUTOMATION NOT SENDING: \"{$name}\" status is \"{$status}\"\n  Fix: Mailchimp > Automations > click it > reactivate any paused steps.";
        }
    }
} else {
    $issues[] = "MAILCHIMP API ERROR: Could not fetch automations (HTTP {$auto_resp['code']}). Check API key.";
}

// ============================================
// 2. MAILCHIMP — AUDIENCE STATS (cleaned up)
// ============================================
$list_resp = mc_api("lists/{$mailchimp_audience}", $mailchimp_api_key, $mailchimp_dc);
if ($list_resp['code'] === 200) {
    $s = $list_resp['data']['stats'] ?? [];
    $total     = $s['member_count'] ?? '?';
    $unsub     = $s['unsubscribe_count'] ?? '?';
    $cleaned   = $s['cleaned_count'] ?? '?';
    $new_since = $s['member_count_since_send'] ?? '?';
    $campaign_count = $s['campaign_count'] ?? '?';

    // Open rate from Mailchimp is already a percentage decimal (0.45 = 45%)
    $open_rate = isset($s['open_rate']) ? round($s['open_rate'] * 100, 1) : '?';

    $stats[] = "";
    $stats[] = "--- MAILCHIMP ---";
    $stats[] = "Active subscribers: {$total}";
    $stats[] = "New since last send: {$new_since}";
    $stats[] = "Avg open rate: {$open_rate}%";
    $stats[] = "Total campaigns sent: {$campaign_count}";

    // Only flag unsubscribes and cleaned if they changed recently
    // Show as info, not as a problem
    $stats[] = "Lifetime unsubscribes: {$unsub}";
    $stats[] = "Lifetime cleaned/bounced: {$cleaned}";

    // Alert if subscriber count drops below a threshold
    if (is_numeric($total) && $total < 10) {
        $issues[] = "LOW SUBSCRIBER COUNT: Only {$total} active subscribers.\n  Fix: Check if hCaptcha is blocking signups. Test signup flow.";
    }
} else {
    $issues[] = "MAILCHIMP API ERROR: Could not fetch audience stats (HTTP {$list_resp['code']}).";
}

// ============================================
// 3. MAILCHIMP — BOT DETECTION (improved)
// hCaptcha is now active, so fewer bots expected.
// Only flag high-confidence bot patterns.
// ============================================
$members_resp = mc_api("lists/{$mailchimp_audience}/members?count=10&sort_field=timestamp_signup&sort_dir=DESC&status=subscribed", $mailchimp_api_key, $mailchimp_dc);
if ($members_resp['code'] === 200 && !empty($members_resp['data']['members'])) {
    $suspicious = [];
    $today = date('Y-m-d');
    foreach ($members_resp['data']['members'] as $m) {
        $fname = $m['merge_fields']['FNAME'] ?? '';
        $lname = $m['merge_fields']['LNAME'] ?? '';
        $email = $m['email_address'] ?? '';
        $signup_date = isset($m['timestamp_signup']) ? substr($m['timestamp_signup'], 0, 10) : '';

        // Only check signups from the last 7 days
        if (!empty($signup_date) && strtotime($signup_date) < strtotime('-7 days')) {
            continue;
        }

        // Gibberish name: >20 chars, no spaces, random mixed case
        if (strlen($fname) > 20 && strpos($fname, ' ') === false && preg_match('/[A-Z].*[a-z].*[A-Z].*[a-z]/', $fname)) {
            $suspicious[] = "{$email} (gibberish name: {$fname})";
        }
        // Disposable email domains
        if (preg_match('/@(tempmail|guerrillamail|throwaway|mailinator|yopmail|sharklasers)\./i', $email)) {
            $suspicious[] = "{$email} (disposable email domain)";
        }
        // Multiple dot-trick gmail (4+ dots before @)
        $local_part = explode('@', $email)[0];
        if (substr_count($local_part, '.') >= 4 && stripos($email, '@gmail.com') !== false) {
            $suspicious[] = "{$email} (excessive dot-trick gmail)";
        }
    }
    if (!empty($suspicious)) {
        $suspicious = array_unique($suspicious);
        $bot_list = implode("\n  - ", $suspicious);
        $issues[] = "POSSIBLE BOT SIGNUPS (last 7 days):\n  - {$bot_list}\n  Fix: Mailchimp > Audience > Contacts > review and delete if fake.";
    }
}

// ============================================
// 4. MAILCHIMP — RECENT CAMPAIGN PERFORMANCE
// ============================================
$campaign_resp = mc_api('campaigns?count=3&sort_field=send_time&sort_dir=DESC&status=sent', $mailchimp_api_key, $mailchimp_dc);
if ($campaign_resp['code'] === 200 && !empty($campaign_resp['data']['campaigns'])) {
    $stats[] = "";
    $stats[] = "--- RECENT CAMPAIGNS ---";
    foreach ($campaign_resp['data']['campaigns'] as $camp) {
        $title = $camp['settings']['subject_line'] ?? 'No subject';
        $sent  = $camp['emails_sent'] ?? 0;
        $opens = $camp['report_summary']['open_rate'] ?? 0;
        $clicks = $camp['report_summary']['click_rate'] ?? 0;
        $date  = isset($camp['send_time']) ? date('M j', strtotime($camp['send_time'])) : '?';
        $opens_pct = round($opens * 100, 1);
        $clicks_pct = round($clicks * 100, 1);
        $stats[] = "{$date}: \"{$title}\" — sent:{$sent} opens:{$opens_pct}% clicks:{$clicks_pct}%";
    }
} else {
    $stats[] = "";
    $stats[] = "--- RECENT CAMPAIGNS ---";
    $stats[] = "No campaigns sent yet.";
}

// ============================================
// 5. WEBSITE — PAGE MONITORING
// ============================================
$stats[] = "";
$stats[] = "--- WEBSITE STATUS ---";

foreach ($pages_to_check as $name => $url) {
    $resp = ping_site($url);
    if ($resp['code'] >= 200 && $resp['code'] < 400) {
        $stats[] = "{$name}: UP ({$resp['time']}s)";
    } else {
        $issues[] = "PAGE DOWN: {$name} returned HTTP {$resp['code']}\n  URL: {$url}\n  Fix: Check Bluehost, flush permalinks (Settings > Permalinks > Save).";
    }

    // Signup form specific checks
    if ($name === 'Signup Form' && $resp['code'] === 200) {
        if (strpos($resp['body'], 'h-captcha') === false && strpos($resp['body'], 'hcaptcha') === false) {
            $issues[] = "HCAPTCHA MISSING on signup form!\n  Fix: Check the HTML block on the Start Free Lesson page in WordPress.";
        } else {
            $stats[] = "hCaptcha: Active on signup form";
        }
    }

    // Login page check
    if ($name === 'Login Page' && $resp['code'] === 200) {
        if (strpos($resp['body'], 'login_error') !== false) {
            $issues[] = "LOGIN PAGE ERROR: WordPress login page is showing errors.";
        }
    }
}

// ============================================
// 6. WORDPRESS — REST API HEALTH
// ============================================
$wp_resp = ping_site($wp_api . '/posts?per_page=1');
if ($wp_resp['code'] === 200) {
    $stats[] = "WordPress REST API: Responding";
} else {
    $issues[] = "WORDPRESS API DOWN: REST API returned HTTP {$wp_resp['code']}\n  This could mean WordPress is broken or a plugin crashed.";
}

// ============================================
// 7. WORDPRESS — CHECK FOR PLUGIN/THEME ISSUES
// ============================================
$home_resp = ping_site($site_base . '/');
if ($home_resp['code'] === 200) {
    if (stripos($home_resp['body'], 'Fatal error') !== false) {
        $issues[] = "PHP FATAL ERROR on homepage! A plugin or theme is crashing.\n  Fix: Log into WordPress > Plugins and deactivate recent updates.";
    }
    if (stripos($home_resp['body'], 'Warning:') !== false && stripos($home_resp['body'], 'php') !== false) {
        $issues[] = "PHP WARNING on homepage. Not fatal but needs attention.\n  Fix: Check WordPress > Tools > Site Health.";
    }
    if (stripos($home_resp['body'], 'maintenance mode') !== false || stripos($home_resp['body'], 'briefly unavailable') !== false) {
        $issues[] = "SITE IN MAINTENANCE MODE! Visitors see a maintenance page.\n  Fix: Delete the .maintenance file via Bluehost File Manager in public_html.";
    }
}

// ============================================
// 8. LEARNDASH — COURSE ACCESS CHECK
// ============================================
$course_resp = ping_site($pages_to_check['Course Page']);
if ($course_resp['code'] === 200) {
    if (stripos($course_resp['body'], 'lessons') !== false || stripos($course_resp['body'], 'LearnDash') !== false || stripos($course_resp['body'], 'ld-') !== false) {
        $stats[] = "LearnDash course: Rendering";
    } else {
        $issues[] = "LEARNDASH MAY BE BROKEN: Course page loaded but no LearnDash content detected.\n  Fix: Check if LearnDash plugin is active. Check for plugin update conflicts.";
    }
}

$lesson_resp = ping_site($pages_to_check['Lesson 1']);
if ($lesson_resp['code'] === 200) {
    $stats[] = "Lesson 1: Accessible";
} else {
    $issues[] = "LESSON 1 NOT LOADING (HTTP {$lesson_resp['code']})\n  Fix: Settings > Permalinks > Save Changes. Check LearnDash plugin.";
}

// ============================================
// BUILD REPORT
// ============================================
$date = date('l, F j, Y');
$time = date('g:i A T');
$issue_count = count($issues);

$social_block  = "\nSOCIAL MEDIA & MARKETING\n";
$social_block .= str_repeat("-", 40) . "\n";
$social_block .= "  Analytics dashboard: https://app.metricool.com\n";
$social_block .= "  Schedule posts: https://publish.buffer.com\n";
$social_block .= "  LinkedIn analytics: https://www.linkedin.com/in/learnmo/\n";
$social_block .= "  Spotify podcast: https://podcasters.spotify.com\n";
$social_block .= "  Google Alerts: https://www.google.com/alerts\n";

if ($issue_count === 0) {
    $subject = "[LMT] Daily Report — All Systems Green — {$date}";
    $body  = "DAILY SYSTEMS REPORT\n";
    $body .= "{$date} at {$time}\n";
    $body .= str_repeat("=", 50) . "\n\n";
    $body .= "STATUS: ALL SYSTEMS GREEN\n";
    $body .= "No issues detected. Everything is running.\n\n";
    $body .= "NUMBERS & STATUS\n";
    $body .= str_repeat("-", 40) . "\n";
    foreach ($stats as $s) {
        if (strpos($s, '---') === 0) {
            $body .= "\n{$s}\n";
        } else {
            $body .= "  {$s}\n";
        }
    }
    $body .= $social_block;
    $body .= "\n— LMT Watchdog v3.0\n";
} else {
    $subject = "[LMT] ALERT — {$issue_count} Issue(s) — {$date}";
    $body  = "ALERT — SYSTEM ISSUES DETECTED\n";
    $body .= "{$date} at {$time}\n";
    $body .= str_repeat("=", 50) . "\n\n";
    $body .= "ISSUES FOUND: {$issue_count}\n";
    $body .= "Fix these BEFORE doing anything else today.\n";
    $body .= str_repeat("-", 40) . "\n";
    foreach ($issues as $i => $issue) {
        $body .= "\n" . ($i + 1) . ". {$issue}\n";
    }
    $body .= "\n\nNUMBERS & STATUS\n";
    $body .= str_repeat("-", 40) . "\n";
    foreach ($stats as $s) {
        if (strpos($s, '---') === 0) {
            $body .= "\n{$s}\n";
        } else {
            $body .= "  {$s}\n";
        }
    }
    $body .= $social_block;
    $body .= "\n— LMT Watchdog v3.0\n";
}

// ============================================
// SEND EMAIL (wp_mail for Bluehost reliability)
// ============================================

// Load WordPress so we can use wp_mail()
$wp_load = dirname(__FILE__) . '/wp-load.php';
if (!file_exists($wp_load)) {
    // Try common Bluehost paths
    $wp_load = $_SERVER['DOCUMENT_ROOT'] . '/wp-load.php';
}

if (file_exists($wp_load)) {
    require_once($wp_load);
    $headers = array('Content-Type: text/plain; charset=UTF-8');
    $sent = wp_mail($alert_email, $subject, $body, $headers);
} else {
    // Fallback to PHP mail() if wp-load not found
    $headers  = "From: LMT Watchdog <{$from_email}>\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $sent = mail($alert_email, $subject, $body, $headers);
}

if ($sent) {
    echo "Watchdog report sent to {$alert_email}\n";
} else {
    echo "ERROR: Failed to send watchdog email\n";
}
