# Bot Protection — Registration Spam Fix

**Problem:** 123 "students" enrolled, most are bots with random usernames.
**Akismet:** Active, catches comment spam (543 blocked) but NOT registration spam.

## Fix Options (pick one)

### Option 1: Add CAPTCHA to Registration (recommended)
- Plugins → Add New → search "reCaptcha by BestWebSoft" or "hCaptcha"
- Install, activate, configure with Google reCAPTCHA keys
- Get keys at: https://www.google.com/recaptcha/admin
- Select reCAPTCHA v2 "I'm not a robot" checkbox

### Option 2: BuddyBoss Built-in (check first)
- BuddyBoss → Settings → look for Registration or reCAPTCHA toggle
- Some BuddyBoss versions have this built in

### Option 3: Email Verification Plugin
- Search "Email Verification for WooCommerce and WordPress"
- Forces users to verify email before account activates
- Kills bots completely but adds friction for real users

## After Adding Protection
1. Export user list from LearnDash Reports
2. Sort by username — delete all random-letter usernames (bots)
3. Keep real users (normal names, company emails, quiz activity)
4. Update verified Pioneer count with real number

## Current Status
- Akismet: Active, 100% accuracy on comments
- Registration: "Anyone can register" is ON (required for free course)
- CAPTCHA: Not installed yet
- Email verification: Not enabled
