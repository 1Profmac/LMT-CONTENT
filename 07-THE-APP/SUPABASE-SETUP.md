# Supabase Setup — Barb App Student Login

## One-time setup (~10 minutes)

---

### STEP 1 — Create free Supabase account
1. Go to supabase.com
2. Click "Start your project" → sign in with GitHub or Google
3. Click "New project"
   - Name: `barb-app`
   - Password: (pick something strong — save it)
   - Region: US East (Virginia)
4. Wait ~2 minutes for project to spin up

---

### STEP 2 — Create the students table
1. In Supabase → click **SQL Editor** (left sidebar)
2. Click **New query**
3. Paste this entire block and click **Run**:

```sql
CREATE TABLE students (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  lessons_completed INTEGER[] DEFAULT '{}',
  questions_asked INTEGER DEFAULT 0,
  helpful_count INTEGER DEFAULT 0,
  email_captured BOOLEAN DEFAULT FALSE,
  pioneer_level TEXT DEFAULT 'New',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  last_seen TIMESTAMPTZ DEFAULT NOW()
);

-- Allow public read/write (app uses anon key)
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all" ON students FOR ALL USING (true) WITH CHECK (true);
```

---

### STEP 3 — Get your API credentials
1. In Supabase → **Settings** (gear icon, left sidebar) → **API**
2. Copy two things:
   - **Project URL** → looks like `https://xxxxxxxxxxxx.supabase.co`
   - **anon public key** → long string starting with `eyJ...`

---

### STEP 4 — Add to Streamlit secrets
In Streamlit Cloud → your app → **Settings** → **Secrets** → paste:

```toml
ANTHROPIC_API_KEY = "your-anthropic-key-here"
MAILERLITE_API_KEY = "your-mailerlite-key-here"
MAILERLITE_GROUP_ID = "your-group-id-here"
SUPABASE_URL = "https://xxxxxxxxxxxx.supabase.co"
SUPABASE_KEY = "eyJ..."
```

---

### STEP 5 — View your student roster
In Supabase → **Table Editor** → click `students`
You'll see every student: name, email, lessons completed, questions asked, last seen.

To export as CSV: click the download icon top right.

---

## What gets saved per student
| Field | What it is |
|---|---|
| email | Their unique identifier |
| name | First name they entered |
| lessons_completed | Which of the 3 lessons they've marked done |
| questions_asked | Total questions asked to Barb |
| helpful_count | How many 👍 they gave |
| pioneer_level | Beginner → Explorer → Pioneer → Trailblazer |
| last_seen | When they last opened the app |
| created_at | When they first signed up |
