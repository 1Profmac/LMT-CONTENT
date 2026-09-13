# LMT Systems Watchdog — Make.com Setup Guide
## STATUS: SUPERSEDED by lmt-watchdog.php (v3.0) running on Bluehost cron
## This file is kept as reference only. The active watchdog is lmt-watchdog.php.

## What This Was Designed To Do
Runs every morning at 7 AM. Checks all your systems. Emails you ONE report:
- GREEN = everything running, here are your numbers
- RED = something broke, here's what

---

## SCENARIO 1: Daily Systems Monitor

### Module 1: Schedule (Trigger)
- Type: Schedule
- Run scenario: Every day at 7:00 AM CT

### Module 2: Mailchimp — List Automations
- App: Mailchimp
- Action: Make an API Call
- URL: /automations
- Method: GET
- Connection: Use API key REDACTED
- WHAT IT CHECKS: Are all automations active? Any paused steps?

### Module 3: Mailchimp — Get Audience Stats
- App: Mailchimp
- Action: Make an API Call
- URL: /lists/5ed5071656
- Method: GET
- WHAT IT CHECKS: Total subscribers, new this week, unsubscribes, open rate

### Module 4: Mailchimp — Get Recent Activity
- App: Mailchimp
- Action: Make an API Call
- URL: /lists/5ed5071656/activity
- Method: GET
- WHAT IT CHECKS: Daily subscribe/unsubscribe activity, bounces

### Module 5: HTTP — Ping Website
- App: HTTP
- Action: Make a request
- URL: https://learnmoretechnologies.com/start-free-lesson/
- Method: GET
- WHAT IT CHECKS: Is the site up? Does the page load?

### Module 6: HTTP — Ping Signup Form
- App: HTTP
- Action: Make a request
- URL: https://learnmoretechnologies.com/wp-json/wp/v2/plugins
- Method: GET
- Headers: Authorization: Basic (WordPress admin credentials, base64 encoded)
- WHAT IT CHECKS: Are all plugins active? Any deactivated?
- NOTE: This requires WordPress Application Password (we'll set this up)

### Module 7: Router
- Route 1: ALL GOOD (no issues found) → send green report
- Route 2: PROBLEM DETECTED (automation paused, site down, plugin off) → send red alert

### Module 8a: Gmail — Send Green Report
- To: hello@learnmoretechnologies.com
- Subject: [LMT] Daily Systems Report — All Good
- Body template:

```
DAILY SYSTEMS REPORT — [date]
================================

STATUS: ALL SYSTEMS GREEN

MAILCHIMP
- Subscribers: [total]
- New this week: [count]
- Welcome Series: ACTIVE
- Speaking Inquiry: ACTIVE
- Open Rate: [rate]%

WEBSITE
- Site Status: UP
- Signup Form: ACTIVE
- Plugins: All active

Have a productive day, Prof.
```

### Module 8b: Gmail — Send Red Alert
- To: hello@learnmoretechnologies.com
- Subject: [LMT] ALERT — System Issue Detected
- Body template:

```
ALERT — SYSTEM ISSUE DETECTED — [date]
==========================================

WHAT BROKE:
[list of issues]

WHAT TO DO:
[specific fix instructions for each issue]

Fix this before doing anything else today.
```

---

## SETUP STEPS (do these in order)

### Step 1: Create Mailchimp Connection
1. In Make.com, go to Connections
2. Add new → Mailchimp
3. API Key: REDACTED
4. Server prefix: us20
5. Test connection

### Step 2: Create Gmail Connection
1. Add new → Gmail
2. Sign in with your hello@learnmoretechnologies.com Google account
3. Authorize Make.com to send emails

### Step 3: Create WordPress Application Password
1. Go to WordPress → Users → Your Profile
2. Scroll to "Application Passwords"
3. Name: "Make.com Monitor"
4. Click "Add New Application Password"
5. Copy the password — save it, you'll need it for the HTTP module

### Step 4: Build the Scenario
1. Click "Create scenario"
2. Add modules in order listed above
3. Connect each module to the next
4. Set up the Router with filter conditions
5. Test run the scenario
6. Turn on scheduling

---

## MAKE.COM CREDIT USAGE
- Each daily run uses approximately 6-8 credits (7 modules)
- 30 days x 8 credits = 240 credits/month
- Free plan gives 1,000 credits/month
- PLENTY of room — can even run twice daily if needed
