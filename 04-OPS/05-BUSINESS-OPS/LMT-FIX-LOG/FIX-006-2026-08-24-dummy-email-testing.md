# FIX-006 — Dummy Email for Testing Forms
**Date:** 2026-08-24

## The Pattern

Use `+test` before the `@` in your real email:

```
brian+test1@learnmoretechnologies.com
brian+test2@learnmoretechnologies.com
brian+test3@learnmoretechnologies.com
```

## Why It Works

- Gmail and most providers deliver it to your real inbox
- MailerLite treats each one as a unique subscriber
- Increment the number each time to avoid duplicate subscriber errors

## Use This For

- Testing the start-free-lessons signup form
- Testing MailerLite automations and welcome sequences
- Testing any form on the site without creating fake accounts
