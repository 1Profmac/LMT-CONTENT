# AGENTIC50 — Mailchimp Setup (Path 1: Link-Based Tagging)

**Purpose:** Auto-segment subscribers from the welcome email. No extra tools.

---

## STEP 1: Create Tags in Mailchimp

Go to Audience → Tags → Create Tag. Create all 9:

**Segment tags (Q1):**
- agentic50-workforce
- agentic50-entrepreneur
- agentic50-startup
- agentic50-pioneer

**Pain point tags (Q2):**
- pain-starting
- pain-burned
- pain-work
- pain-time

**Buy signal tags (Q3):**
- ready-self-serve
- ready-workshop
- ready-partner
- ready-private

---

## STEP 2: Create Thank You Pages

Create 3 pages on your site (one per question step). Each page shows the next question.

**Page 1:** learnmoretechnologies.com/welcome-step1/
Shows Q2 (challenge question) after they answer Q1

**Page 2:** learnmoretechnologies.com/welcome-step2/
Shows Q3 (what would help) after they answer Q2

**Page 3:** learnmoretechnologies.com/welcome-done/
Final confirmation: "You're all set, Pioneer. Your first newsletter drops Thursday."

**Simpler alternative:** Use ONE page with all 3 questions as anchor links, or send 1 email with all 3 questions using Mailchimp survey blocks.

---

## STEP 3: Build the Welcome Email

Automations → Welcome new subscribers

**From:** Brian McKinney | 50+TechBridge
**Subject:** Welcome, Pioneer. 3 quick clicks so I can help you.
**Preview:** Takes 30 seconds. Helps me send you the right stuff.

### Email Content:

```
Hey *|FNAME|*,

You're in. Every week you'll get one AI headline, one tool, one opportunity,
and one checklist — all translated for adults 50+.

3 quick clicks so I send you the right stuff:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. WHICH ONE SOUNDS MOST LIKE YOU?

[BUTTON] I'm working — want to stay relevant with AI
[BUTTON] I run a business — need to modernize
[BUTTON] I'm building something new
[BUTTON] AI for daily life and independence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2. WHAT'S HOLDING YOU BACK WITH TECH?

[BUTTON] I don't know where to start
[BUTTON] I've tried but it didn't stick
[BUTTON] I need it for work but no one's teaching me
[BUTTON] I want to learn but I don't have time

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. WHAT WOULD HELP YOU MOST RIGHT NOW?

[BUTTON] A free course I can do on my phone
[BUTTON] A live workshop at my church, library, or center
[BUTTON] Someone to train my organization's members
[BUTTON] One-on-one coaching

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

That's it. Now I know what to send you.

See you Thursday.

— Brian
```

---

## STEP 4: Set Up Click Automations (12 total)

In Mailchimp → Automations → Create one for each button:

### Q1 Buttons
| Button | Link Contains | Add Tag |
|---|---|---|
| Working | segment=workforce | agentic50-workforce |
| Business | segment=entrepreneur | agentic50-entrepreneur |
| Building new | segment=startup | agentic50-startup |
| Daily life | segment=pioneer | agentic50-pioneer |

### Q2 Buttons
| Button | Link Contains | Add Tag |
|---|---|---|
| Don't know where to start | pain=starting | pain-starting |
| Tried didn't stick | pain=burned | pain-burned |
| Need for work | pain=work | pain-work |
| No time | pain=time | pain-time |

### Q3 Buttons (MONEY QUESTIONS)
| Button | Link Contains | Add Tag | Brian's Action |
|---|---|---|---|
| Free course | ready=self-serve | ready-self-serve | Auto-drip newsletter |
| Live workshop | ready=workshop | ready-workshop | Invite to next Lunch & Learn |
| Train my org | ready=partner | ready-partner | **Personal email within 48 hrs** |
| One-on-one | ready=private | ready-private | **Send offer within 24 hrs** |

---

## STEP 5: Set Up Revenue Alerts

Create an automation that notifies Brian immediately when someone clicks Q3-C or Q3-D:

**Automation: "Hot Lead Alert"**
- Trigger: Tag `ready-partner` OR `ready-private` is added
- Action: Send internal notification to brian@learnmoretechnologies.com
- Subject: "HOT LEAD: [subscriber name] wants [partner training / 1-on-1 coaching]"

**This is the most important automation in the entire system.**

---

## STEP 6: Checklist Rotation

Everyone gets the same newsletter. Rotate the checklist section weekly:

| Week | Checklist | Audience Tag |
|---|---|---|
| 1 | Everyday Pioneer | agentic50-pioneer |
| 2 | Workforce | agentic50-workforce |
| 3 | Business Owner | agentic50-entrepreneur |
| 4 | Startup | agentic50-startup |
| 5 | Repeat cycle | — |
