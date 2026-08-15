# AGENTIC50 — Google Form + Automation (Path 2)

**Purpose:** Standalone questionnaire for events, QR codes, and website embed.
Responses auto-flow to Google Sheets → Mailchimp via Make.com.

---

## STEP 1: Create the Google Form

Go to forms.google.com → Blank form

### Form Title:
**Join the Pioneers — 50+TechBridge**

### Form Description:
Sign up for the Agentic50 Weekly newsletter. AI news translated for adults 50+. Free. No spam.

---

### Question 1: First Name
- Type: Short answer
- Required: Yes

### Question 2: Email Address
- Type: Short answer
- Required: Yes

### Question 3: Which one sounds most like you?
- Type: Multiple choice
- Required: Yes
- Options:
  - I'm working and want to stay relevant with AI
  - I run a business and need to modernize
  - I'm building something new
  - I want AI for daily life and independence

### Question 4: What's holding you back with technology?
- Type: Multiple choice
- Required: Yes
- Options:
  - I don't know where to start
  - I've tried but it didn't stick
  - I need it for work but no one's teaching me
  - I want to learn but I don't have time

### Question 5: What would help you most right now?
- Type: Multiple choice
- Required: Yes
- Options:
  - A free course I can do on my phone
  - A live workshop at my church, library, or center
  - Someone to train my organization's members
  - One-on-one coaching

### Question 6: What city are you in?
- Type: Short answer
- Required: No

---

### Form Settings:
- Confirmation message: "You're in, Pioneer. Check your inbox Thursday for your first newsletter. — Brian"
- Collect email addresses: OFF (already in Q2)
- Limit to 1 response: OFF

---

## STEP 2: Link to Google Sheets

- In the Form → "Responses" tab → green Sheets icon → "Create a new spreadsheet"
- Name: `Agentic50 Subscribers`
- Columns will auto-populate: Timestamp | First Name | Email | Segment | Challenge | Help Needed | City

---

## STEP 3: Generate QR Code

- Get the form's shareable link (Send → Link → Copy)
- Go to any free QR generator
- Download PNG → save to `04-ASSETS/logos/agentic50-signup-qr.png`
- Print on every Lunch & Learn flyer and business card

---

## STEP 4: Automate Google Sheets → Mailchimp (Make.com)

### Scenario: "Agentic50 Signup to Mailchimp"

**Module 1: Google Sheets → Watch New Rows**
- Spreadsheet: Agentic50 Subscribers
- Sheet: Form Responses 1

**Module 2: Mailchimp → Add/Update Subscriber**
- List: LMT Hello
- Email: {{Email}}
- First Name: {{First Name}}
- Status: Subscribed

**Module 3: Router → Add Segment Tag (Q3)**
| If Column "Segment" Contains | Add Tag |
|---|---|
| "working" | agentic50-workforce |
| "business" | agentic50-entrepreneur |
| "building" | agentic50-startup |
| "daily life" | agentic50-pioneer |

**Module 4: Router → Add Pain Tag (Q4)**
| If Column "Challenge" Contains | Add Tag |
|---|---|
| "where to start" | pain-starting |
| "didn't stick" | pain-burned |
| "for work" | pain-work |
| "don't have time" | pain-time |

**Module 5: Router → Add Buy Signal Tag (Q5)**
| If Column "Help Needed" Contains | Add Tag |
|---|---|
| "free course" | ready-self-serve |
| "live workshop" | ready-workshop |
| "train my organization" | ready-partner |
| "one-on-one" | ready-private |

**Module 6: Filter → Hot Lead Alert**
- IF tag = ready-partner OR ready-private
- THEN send email to brian@learnmoretechnologies.com
- Subject: "HOT LEAD: {{First Name}} in {{City}} wants {{Help Needed}}"

### Schedule: Every 15 minutes (free tier)

---

## STEP 5: Test the Flow

1. Fill out the form on your phone with a test email
2. Check Google Sheets — row appears
3. Run Make.com scenario manually (or wait 15 min)
4. Check Mailchimp — subscriber + 3 tags should appear
5. If you selected "train my org" or "one-on-one" — check your inbox for the hot lead alert
6. Delete test data when confirmed

---

## WHERE TO USE THE FORM

| Location | How |
|---|---|
| Lunch & Learn events | QR code on flyer |
| Business cards | QR code on back |
| Website | Embed on learnmoretechnologies.com/subscribe |
| LinkedIn posts | Link in comments |
| Email signature | "Join the Pioneers" link |
| Partner orgs | Share link with coordinators |
| After speaking gigs | QR code on final slide |
