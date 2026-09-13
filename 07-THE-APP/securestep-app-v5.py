"""
Barb App v5 — Tiered monetization
Free | Pioneer $9/mo | Organization $49/mo
"""

import streamlit as st
import anthropic
import os, json, urllib.request, urllib.parse
from datetime import datetime

st.set_page_config(page_title="Ask Barb — 50+TechBridge", page_icon="🌟", layout="centered")

# ── Tier helpers ──────────────────────────────────────────────────────────────
def tier_rank(tier: str) -> int:
    return {"free": 0, "pioneer": 1, "organization": 2}.get(tier, 0)

def can(feature: str) -> bool:
    """Check if current student's tier allows a feature."""
    tier = st.session_state.get("student_tier", "free")
    gates = {
        "live_ai":       ["pioneer", "organization"],
        "spanish":       ["pioneer", "organization"],
        "read_aloud":    ["pioneer", "organization"],
        "save_chat":     ["pioneer", "organization"],
        "instructor":    ["organization"],
        "roster":        ["organization"],
        "csv_export":    ["organization"],
    }
    return tier in gates.get(feature, [])

def upgrade_prompt(feature_label: str, required_tier: str):
    """Show an upgrade card when a free user hits a gated feature."""
    tier_labels = {"pioneer": "Pioneer ($9/mo)", "organization": "Organization ($49/mo)"}
    stripe_keys = {"pioneer": "STRIPE_PIONEER_LINK", "organization": "STRIPE_ORG_LINK"}
    link = os.environ.get(stripe_keys[required_tier]) or st.secrets.get(stripe_keys[required_tier], "#")
    st.markdown(f"""
    <div style="background:#162640; border:2px solid #C8942E; border-radius:12px; padding:24px; margin:16px 0; text-align:center;">
        <div style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#C8942E; margin-bottom:8px;">
            {feature_label} — {tier_labels[required_tier]}
        </div>
        <div style="color:#A8B8CC; font-size:17px; margin-bottom:16px;">
            Upgrade to unlock this feature and support the 50+TechBridge mission.
        </div>
        <a href="{link}?prefilled_email={urllib.parse.quote(st.session_state.get('student_email',''))}"
           target="_blank"
           style="display:inline-block; background:#C8942E; color:#0E1C2F; font-weight:700;
                  font-size:18px; padding:12px 32px; border-radius:8px; text-decoration:none;">
            Upgrade Now →
        </a>
        <div style="font-size:13px; color:#A8B8CC; margin-top:10px;">
            Cancel any time. Billed monthly via Stripe.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Supabase ──────────────────────────────────────────────────────────────────
def get_creds():
    url = os.environ.get("SUPABASE_URL") or st.secrets.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY", "")
    return url, key

def supabase_req(method, path, data=None):
    url, key = get_creds()
    if not url or not key: return None
    try:
        req = urllib.request.Request(
            f"{url}/rest/v1/{path}", data=json.dumps(data).encode() if data else None,
            method=method, headers={
                "apikey": key, "Authorization": f"Bearer {key}",
                "Content-Type": "application/json", "Prefer": "return=representation",
            }
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            return json.loads(r.read())
    except Exception:
        return None

def load_student(email):
    r = supabase_req("GET", f"students?email=eq.{urllib.parse.quote(email)}&select=*")
    return r[0] if r else None

def create_student(email, name):
    r = supabase_req("POST", "students", {"email": email, "name": name,
        "lessons_completed": [], "questions_asked": 0, "helpful_count": 0,
        "email_captured": False, "tier": "free", "subscription_status": "inactive"})
    return r[0] if r else None

def save_student(email):
    if not email: return
    level, _ = get_pioneer_level(st.session_state.questions_asked)
    supabase_req("PATCH", f"students?email=eq.{urllib.parse.quote(email)}", {
        "lessons_completed": sorted(list(st.session_state.lessons_completed)),
        "questions_asked": st.session_state.questions_asked,
        "helpful_count": st.session_state.helpful_count,
        "email_captured": st.session_state.email_captured,
        "pioneer_level": level,
        "last_seen": datetime.utcnow().isoformat(),
    })

def load_all_students():
    return supabase_req("GET", "students?select=*&order=last_seen.desc") or []

# ── Internet check ────────────────────────────────────────────────────────────
def check_internet():
    try:
        urllib.request.urlopen("https://www.google.com", timeout=2)
        return True
    except Exception:
        return False

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700;800&display=swap');
html,body,[class*="css"],.stApp{background-color:#0E1C2F!important;color:#C4CDD9!important;font-family:'DM Sans',sans-serif!important;font-size:18px!important}
.block-container{background-color:#0E1C2F!important;padding-top:2rem!important}
section[data-testid="stSidebar"]{background-color:#162640!important}
section[data-testid="stSidebar"]>div{background-color:#162640!important}
h1,h2,h3,.stMarkdown h1,.stMarkdown h2,.stMarkdown h3{font-family:'Playfair Display',serif!important;color:#C8942E!important}
p,li,label,span,div{font-family:'DM Sans',sans-serif!important;color:#C4CDD9!important}
.stButton>button{background-color:#C8942E!important;color:#0E1C2F!important;font-weight:700!important;font-size:18px!important;border-radius:8px!important;border:none!important;padding:12px 24px!important;min-height:48px!important;width:100%!important;cursor:pointer!important}
.stButton>button:hover{background-color:#E8B84B!important}
.pill-btn>button{background-color:#1E3A5F!important;color:#C8942E!important;border:1.5px solid #C8942E!important;border-radius:24px!important;font-weight:600!important;padding:10px 20px!important}
.pill-btn>button:hover{background-color:#C8942E!important;color:#0E1C2F!important}
.outline-btn>button{background-color:transparent!important;color:#C8942E!important;border:2px solid #C8942E!important;border-radius:8px!important}
.stChatMessage{font-size:18px!important;border-radius:10px!important;padding:12px!important;margin-bottom:10px!important}
[data-testid="stChatMessageContent"]{font-size:18px!important;color:#C4CDD9!important}
[data-testid="stChatMessage"][data-role="user"]{background-color:#1E3A5F!important;border-left:4px solid #C8942E!important}
[data-testid="stChatMessage"][data-role="assistant"]{background-color:#162640!important;border-left:4px solid #109F35!important}
.stChatInput textarea,.stChatInput input{background-color:#162640!important;color:#C4CDD9!important;border:1.5px solid #A8B8CC!important;border-radius:8px!important;font-size:18px!important}
.stTextInput input{background-color:#162640!important;color:#C4CDD9!important;border:1.5px solid #A8B8CC!important;border-radius:8px!important;font-size:18px!important;padding:10px 14px!important}
.stSelectbox>div>div{background-color:#162640!important;color:#C4CDD9!important;border:1.5px solid #A8B8CC!important;border-radius:8px!important;font-size:18px!important}
.stRadio>div{background-color:transparent!important}
[data-testid="stMetric"]{background-color:#162640!important;border-radius:10px!important;padding:16px!important;border:1px solid #1E3A5F!important}
[data-testid="stMetricValue"]{color:#C8942E!important;font-family:'Playfair Display',serif!important;font-size:2rem!important}
hr{border-color:#1E3A5F!important}
.lmt-tip-card{background-color:#162640;border-left:5px solid #C8942E;border-radius:10px;padding:20px 24px;margin:12px 0;font-size:18px}
.lmt-progress-card{background-color:#162640;border:2px solid #C8942E;border-radius:12px;padding:24px;margin:12px 0;text-align:center}
.lmt-progress-card h2{font-family:'Playfair Display',serif;color:#C8942E;margin:0 0 8px 0;font-size:2rem}
.lmt-level-badge{background-color:#1E3A5F;border:1.5px solid #C8942E;border-radius:10px;padding:12px 16px;margin:8px 0;text-align:center}
.lmt-level-badge strong{color:#C8942E;font-family:'Playfair Display',serif}
.lmt-section-card{background-color:#162640;border-radius:12px;padding:20px 24px;margin:12px 0;border:1px solid #1E3A5F}
.lmt-section-card h3{font-family:'Playfair Display',serif;color:#C8942E;margin-top:0}
.lmt-section-card a{color:#C8942E;text-decoration:underline}
.lmt-section-card ul{padding-left:20px}
.lmt-section-card li{color:#C4CDD9;margin-bottom:8px}
.lmt-barb-greeting{background-color:#162640;border-left:4px solid #109F35;border-radius:10px;padding:20px 24px;margin:12px 0;font-size:18px}
.lmt-orange-msg{background-color:rgba(232,115,58,.15);border-left:4px solid #E8733A;border-radius:8px;padding:16px 20px;color:#E8B84B;font-size:18px;margin:12px 0}
.lmt-table{width:100%;border-collapse:collapse;font-size:16px}
.lmt-table th{background-color:#1E3A5F;color:#C8942E;padding:10px 14px;text-align:left;border-bottom:2px solid #C8942E}
.lmt-table td{background-color:#162640;color:#C4CDD9;padding:10px 14px;border-bottom:1px solid #1E3A5F}
.lesson-card{background-color:#162640;border-radius:14px;padding:24px;margin:14px 0;border:1px solid #1E3A5F}
.lesson-card.completed{border-color:#109F35}
.lesson-badge{display:inline-block;background-color:#C8942E;color:#0E1C2F;font-weight:700;font-size:13px;border-radius:20px;padding:4px 14px;margin-bottom:10px}
.lesson-badge.done{background-color:#109F35}
.lesson-title{font-family:'Playfair Display',serif;font-size:1.4rem;color:#C8942E;margin:0 0 8px 0}
.lesson-skills{color:#A8B8CC;font-size:16px;margin:0 0 12px 0}
.skill-tag{display:inline-block;background-color:#1E3A5F;color:#C8942E;border:1px solid #C8942E;border-radius:20px;padding:3px 12px;font-size:14px;margin:3px 3px 3px 0}
.tier-badge-free{background:#1E3A5F;color:#A8B8CC;border:1px solid #A8B8CC;border-radius:20px;padding:2px 12px;font-size:13px;font-weight:700}
.tier-badge-pioneer{background:#1A3A1A;color:#109F35;border:1px solid #109F35;border-radius:20px;padding:2px 12px;font-size:13px;font-weight:700}
.tier-badge-org{background:#2A1A00;color:#C8942E;border:1px solid #C8942E;border-radius:20px;padding:2px 12px;font-size:13px;font-weight:700}
.lock-icon{color:#A8B8CC;font-size:14px;margin-left:6px}
.offline-banner{background-color:#2A1A0A;border:1px solid #E8733A;border-radius:8px;padding:10px 16px;color:#E8B84B;font-size:15px;margin-bottom:12px}
</style>""", unsafe_allow_html=True)

# ── Offline FAQ ───────────────────────────────────────────────────────────────
OFFLINE_FAQ = {
    "what is ai": "AI stands for Artificial Intelligence. It reads your question and writes back a helpful answer in plain English. It's not magic, not alive, and not always right. It predicts what a helpful answer looks like — it doesn't look things up like Google.",
    "can ai make mistakes": "Yes — AI can be wrong, especially about specific facts or medical details. Always double-check anything important with your doctor, a government website, or a trusted person.",
    "what are the pressure tactics": "Scammers use four levers: HURRY (act now), FEAR (you'll be arrested), SECRECY (don't tell your family), and AUTHORITY (badge number, familiar logo). If you feel any of these — stop. Hang up. Call back on a number you already had.",
    "two factor": "Two-factor authentication — 2FA — adds a second lock after your password. After you log in, the site sends a code to your phone. You type it in. Even if someone steals your password, they can't get in without that code. Turn it on for email first, then your bank.",
    "passphrase": "A passphrase is random words used as a password — like 'maple-porch-radio-Thursday.' Longer means harder to crack and easier to remember.",
    "never move money": "No real bank, government, or official ever asks you to move money to protect it. Gift cards, wire transfers, crypto ATMs, couriers — these are all scam payments. Full stop.",
    "already sent money": "Stop immediately. Call your bank — number on the back of your card. Report at reportfraud.ftc.gov and ic3.gov. Change your email password. Tell one trusted person. Speed matters.",
    "family code word": "A secret phrase only your family knows. If someone calls claiming to be your grandchild — ask for the code word. If they can't give it, hang up and call your family member directly.",
    "spot a fake": "Check: 1) The sender domain — does it look right? 2) The greeting — 'Dear Customer' is a warning. 3) The ask — links, downloads, codes. 4) Did you start this? If they contacted you first, be suspicious.",
    "gift cards": "No real government agency or emergency ever requires payment in gift cards. Anyone asking for gift card numbers is a scammer.",
    "report a scam": "Report at reportfraud.ftc.gov (FTC) and ic3.gov (FBI). Identity theft: identitytheft.gov.",
    "chatgpt": "Go to chat.openai.com — free, no account needed to start. Type your question like a text message and press Enter.",
}

def offline_answer(q):
    q = q.lower()
    for key, ans in OFFLINE_FAQ.items():
        if key in q: return ans
    best, score = None, 0
    for key in OFFLINE_FAQ:
        s = len(set(q.split()) & set(key.split()))
        if s > score: score, best = s, key
    return OFFLINE_FAQ[best] if best and score >= 1 else "I'm offline — ask your instructor or try again when internet is available."

# ── Lesson data ───────────────────────────────────────────────────────────────
LESSONS = [
    {"number":1,"title":"Welcome to AI","subtitle":"What AI is, what it isn't, and your first real question",
     "skills":["What AI actually is","How to ask a good question","Staying in charge"],
     "url":"https://50plustechbridge.com/start-free-lessons/","youtube":None},
    {"number":2,"title":"Talk to AI","subtitle":"Have a real conversation with ChatGPT or Claude",
     "skills":["Opening ChatGPT on your phone","Asking your first question","Getting better answers"],
     "url":"https://50plustechbridge.com/start-free-lessons/","youtube":None},
    {"number":3,"title":"Don't Get Scammed","subtitle":"3 skills that keep scammers away from your money",
     "skills":["Spot a Fake","Name the Pressure","Passwords & the Second Lock"],
     "url":"https://50plustechbridge.com/start-free-lessons/","youtube":"https://youtu.be/YsSXhxo_fus"},
]

SYSTEM_PROMPT    = """You are Barb, a warm AI guide for adults 50+ learning through 50+TechBridge. You know all three lessons: what AI is, how to talk to AI, and scam prevention (spot a fake, name the pressure, passwords and 2FA). Simple language, no jargon, 3-5 short paragraphs, always encouraging."""
SYSTEM_PROMPT_ES = """Eres Barb, una guía de IA para adultos 50+ del programa 50+TechBridge. Responde en español simple. Sin jerga. Máximo 3-5 párrafos cortos."""

def get_pioneer_level(q):
    if q>=50: return "Trailblazer","You're leading the way!"
    if q>=25: return "Pioneer","You're exploring with confidence!"
    if q>=10: return "Explorer","You're getting comfortable!"
    if q>=1:  return "Beginner","You've taken your first step!"
    return "New","Ask your first question!"

# ── Session defaults ──────────────────────────────────────────────────────────
DEFAULTS = {
    "messages":[],"questions_asked":0,"helpful_count":0,
    "lessons_completed":set(),"instructor_mode":False,"projector_mode":False,
    "spanish_mode":False,"email_captured":False,"last_reply":"",
    "logged_in":False,"student_email":"","student_name":"","student_tier":"free",
    "online":True,"connectivity_checked":False,"welcomed":False,
}
for k,v in DEFAULTS.items():
    if k not in st.session_state: st.session_state[k]=v

if not st.session_state.connectivity_checked:
    st.session_state.online = check_internet()
    st.session_state.connectivity_checked = True

if st.session_state.projector_mode:
    st.markdown("""<style>
    html,body,[class*="css"],.stApp,p,li,label,span,div{font-size:24px!important}
    .stChatMessage,[data-testid="stChatMessageContent"]{font-size:24px!important}
    h1{font-size:3.5rem!important} h2{font-size:2rem!important}
    .stButton>button{font-size:22px!important;padding:16px 28px!important}
    </style>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LOGIN
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    st.markdown("""
    <div style="text-align:center;padding-top:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:3rem;color:#C8942E;">Ask Barb</div>
        <div style="color:#A8B8CC;font-size:18px;margin-bottom:30px;">50+TechBridge Free Lessons</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#162640;border:2px solid #C8942E;border-radius:16px;padding:36px 32px;max-width:480px;margin:0 auto;">
        <div style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#C8942E;margin-bottom:6px;">Welcome!</div>
        <div style="color:#A8B8CC;font-size:16px;margin-bottom:20px;">Enter your name and email. Your progress saves automatically — free, forever.</div>
    </div>""", unsafe_allow_html=True)

    name_in  = st.text_input("Your first name:", placeholder="e.g. Margaret")
    email_in = st.text_input("Your email address:", placeholder="yourname@email.com")

    if st.button("Let's Go →"):
        if not name_in.strip():
            st.warning("Please enter your first name.")
        elif "@" not in email_in or "." not in email_in:
            st.warning("Please enter a valid email address.")
        else:
            email = email_in.strip().lower()
            name  = name_in.strip()
            existing = load_student(email)
            if existing:
                st.session_state.student_email      = email
                st.session_state.student_name       = existing.get("name", name)
                st.session_state.student_tier       = existing.get("tier", "free")
                st.session_state.questions_asked    = existing.get("questions_asked", 0)
                st.session_state.helpful_count      = existing.get("helpful_count", 0)
                st.session_state.email_captured     = existing.get("email_captured", False)
                st.session_state.lessons_completed  = set(existing.get("lessons_completed", []))
                st.session_state.returning_student  = True
            else:
                create_student(email, name)
                st.session_state.student_email      = email
                st.session_state.student_name       = name
                st.session_state.student_tier       = "free"
                st.session_state.returning_student  = False
            st.session_state.logged_in = True
            st.rerun()

    st.markdown('<div style="font-size:14px;color:#A8B8CC;text-align:center;margin-top:12px;">No password needed. Email used only to save your progress.</div>', unsafe_allow_html=True)
    st.stop()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    try: st.image("logo.png", width=140)
    except: pass

    tier = st.session_state.student_tier
    tier_labels = {"free":"Free","pioneer":"Pioneer ✓","organization":"Organization ✓"}
    tier_badge_class = {"free":"tier-badge-free","pioneer":"tier-badge-pioneer","organization":"tier-badge-org"}
    st.markdown(f"""
    <div style="margin:4px 0;">
        <span style="font-family:'Playfair Display',serif;font-size:20px;font-weight:800;color:#C8942E;">Ask Barb</span>
    </div>
    <div style="font-size:15px;color:#C8942E;font-weight:700;">{st.session_state.student_name}</div>
    <div style="font-size:13px;color:#A8B8CC;margin-bottom:4px;">{st.session_state.student_email}</div>
    <span class="{tier_badge_class[tier]}">{tier_labels[tier]}</span>
    """, unsafe_allow_html=True)

    status_color = "#109F35" if st.session_state.online else "#E8733A"
    st.markdown(f'<div style="font-size:12px;color:{status_color};margin:6px 0;">● {"Online" if st.session_state.online else "Offline"}</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F;margin:8px 0;'>", unsafe_allow_html=True)

    nav = ["Home","Free Lessons","Ask Barb","My Progress","Upgrade","Resources"]
    if can("instructor"): nav.append("Instructor Guide")
    if can("roster"):     nav.append("Class Roster")
    page = st.radio("Navigate", nav, label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1E3A5F;margin:8px 0;'>", unsafe_allow_html=True)
    completed = len(st.session_state.lessons_completed)
    level, _ = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f"""
    <div class="lmt-level-badge">
        <div style="font-size:12px;color:#A8B8CC;">Lessons Completed</div>
        <strong style="font-size:22px;">{completed}/3</strong>
    </div>
    <div style="text-align:center;font-size:14px;color:#A8B8CC;margin:4px 0;">Level: <span style="color:#C8942E;font-weight:700;">{level}</span></div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F;margin:8px 0;'>", unsafe_allow_html=True)

    if can("instructor"):
        st.markdown("<div style='font-size:11px;color:#A8B8CC;margin-bottom:4px;'>INSTRUCTOR</div>", unsafe_allow_html=True)
        st.session_state.instructor_mode = st.toggle("Instructor Mode", value=st.session_state.instructor_mode)
        if st.session_state.instructor_mode:
            st.session_state.projector_mode = st.toggle("Projector Mode", value=st.session_state.projector_mode)
            if st.button("Reset for New Class"):
                for k in ["messages","questions_asked","helpful_count","lessons_completed","email_captured","logged_in","student_email","student_name","student_tier","welcomed"]:
                    st.session_state[k] = DEFAULTS[k]
                st.toast("Reset — ready for new class.")
                st.rerun()
        st.markdown("<hr style='border-color:#1E3A5F;margin:8px 0;'>", unsafe_allow_html=True)

    if can("spanish"):
        st.session_state.spanish_mode = st.toggle("Español", value=st.session_state.spanish_mode)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat"): st.session_state.messages=[]; st.rerun()
    with col2:
        if st.button("Log Out"):
            save_student(st.session_state.student_email)
            for k in DEFAULTS: st.session_state[k]=DEFAULTS[k]
            st.rerun()

if st.session_state.get("returning_student") and not st.session_state.welcomed:
    completed = len(st.session_state.lessons_completed)
    st.toast(f"Welcome back, {st.session_state.student_name}! {completed}/3 lessons complete.")
    st.session_state.welcomed = True

# ── Section divider helper ────────────────────────────────────────────────────
def hr(): st.markdown("<hr style='border-color:#1E3A5F;margin:16px 0;'>", unsafe_allow_html=True)
def h1(text): st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif;font-size:2.4rem;color:#C8942E;">{text}</h1>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — Barb is using pre-set answers.</div>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif;font-size:2.8rem;color:#C8942E;">Hi, {st.session_state.student_name}.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC;font-size:20px;">Your AI guide for the 50+TechBridge free lessons.</p>', unsafe_allow_html=True)
    hr()

    tips = ["A passphrase like 'maple-porch-radio-Thursday' is stronger AND easier to remember.",
            "The real IRS and Social Security never call demanding gift cards.",
            "AI is a conversation, not a search engine. Ask again if you don't like the first answer.",
            "Turn on two-factor authentication on your email this week.",
            "Pick a family code word. If they can't say it — hang up."]
    st.markdown(f'<div class="lmt-tip-card"><strong style="color:#C8942E;">Today\'s tip:</strong> {tips[datetime.now().timetuple().tm_yday % len(tips)]}</div>', unsafe_allow_html=True)
    hr()

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in lesson["skills"]])
        st.markdown(f"""
        <div class="lesson-card {'completed' if done else ''}">
            <span class="lesson-badge {'done' if done else ''}">{'✓ Done' if done else f'Lesson {lesson["number"]}'}</span>
            <div class="lesson-title">{lesson['title']}</div>
            <div class="lesson-skills">{lesson['subtitle']}</div>
            <div>{skills_html}</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FREE LESSONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Free Lessons":
    h1("Free Lessons")
    st.markdown('<p style="color:#A8B8CC;font-size:18px;">Three lessons. Watch, learn, ask Barb anything along the way.</p>', unsafe_allow_html=True)
    hr()

    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E;margin-bottom:20px;">
        <div style="font-family:'Playfair Display',serif;font-size:1.2rem;color:#C8942E;margin-bottom:6px;">Ready to try AI yourself?</div>
        <div style="color:#C4CDD9;font-size:17px;margin-bottom:14px;">Open ChatGPT free — no account needed. Practice what you learned in Lesson 2.</div>
        <a href="https://chat.openai.com" target="_blank"
           style="display:inline-block;background:#C8942E;color:#0E1C2F;font-weight:700;font-size:18px;padding:12px 28px;border-radius:8px;text-decoration:none;">
           Open ChatGPT →</a>
        <span style="color:#A8B8CC;font-size:14px;margin-left:14px;">Opens in a new tab</span>
    </div>""", unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in lesson["skills"]])
        st.markdown(f"""
        <div class="lesson-card {'completed' if done else ''}">
            <span class="lesson-badge {'done' if done else ''}">{'✓ Completed' if done else f'Lesson {lesson["number"]}'}</span>
            <div class="lesson-title">{lesson['title']}</div>
            <div class="lesson-skills">{lesson['subtitle']}</div>
            <div style="margin:10px 0;">{skills_html}</div>
        </div>""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2,2,2])
        with col1:
            st.markdown(f'<a href="{lesson["url"]}" target="_blank" style="display:block;background:#C8942E;color:#0E1C2F;font-weight:700;text-align:center;padding:10px;border-radius:8px;text-decoration:none;">Watch Lesson {lesson["number"]} →</a>', unsafe_allow_html=True)
        with col2:
            if lesson["youtube"]:
                st.markdown(f'<a href="{lesson["youtube"]}" target="_blank" style="display:block;background:#1E3A5F;color:#C8942E;font-weight:700;text-align:center;padding:10px;border-radius:8px;text-decoration:none;border:1.5px solid #C8942E;">▶ YouTube</a>', unsafe_allow_html=True)
        with col3:
            if st.button("↩ Undo" if done else "✓ Mark Done", key=f"done_{lesson['number']}", use_container_width=True):
                if done: st.session_state.lessons_completed.discard(lesson["number"])
                else: st.session_state.lessons_completed.add(lesson["number"])
                save_student(st.session_state.student_email)
                st.rerun()

        with st.expander(f"Ask Barb about Lesson {lesson['number']}"):
            fqs = {1:["What is AI in plain English?","Can AI make mistakes?","What's the difference between AI and Google?"],
                   2:["How do I open ChatGPT on my phone?","What's a good first question to ask AI?","What if I don't like the answer?"],
                   3:["What are the 4 pressure tactics?","How do I set up two-factor authentication?","What do I do if I already sent money?","What is a family code word?"]}
            for q in fqs[lesson["number"]]:
                st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
                if st.button(q, key=f"lq_{lesson['number']}_{q[:12]}", use_container_width=True):
                    st.session_state["user_input"] = q; st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        hr()

    if len(st.session_state.lessons_completed) == 3:
        col_logo, col_text = st.columns([1,2])
        with col_logo:
            try: st.image("agentic50-logo.png", width=160)
            except: st.markdown('<div style="font-family:\'Playfair Display\',serif;font-size:2rem;color:#C8942E;text-align:center;">Agentic50</div>', unsafe_allow_html=True)
        with col_text:
            st.markdown(f'<div style="padding:12px 0;"><div style="font-family:\'Playfair Display\',serif;font-size:1.4rem;color:#C8942E;">You\'re a Digital Pioneer, {st.session_state.student_name}.</div><div style="color:#C4CDD9;font-size:17px;margin-top:6px;">All 3 lessons complete.</div></div>', unsafe_allow_html=True)
        if not st.session_state.email_captured:
            email_conf = st.text_input("Get weekly AI tips free:", value=st.session_state.student_email, key="conf_email")
            if st.button("Sign Me Up →", key="ml_btn"):
                try:
                    ml_key = os.environ.get("MAILERLITE_API_KEY") or st.secrets.get("MAILERLITE_API_KEY","")
                    ml_grp = os.environ.get("MAILERLITE_GROUP_ID") or st.secrets.get("MAILERLITE_GROUP_ID","")
                    if ml_key and ml_grp:
                        payload = json.dumps({"email":email_conf,"groups":[ml_grp],"fields":{"name":st.session_state.student_name}}).encode()
                        req = urllib.request.Request("https://connect.mailerlite.com/api/subscribers",data=payload,method="POST",headers={"Content-Type":"application/json","Authorization":f"Bearer {ml_key}"})
                        urllib.request.urlopen(req,timeout=5)
                except: pass
                st.session_state.email_captured=True; save_student(st.session_state.student_email); st.rerun()
        else:
            st.markdown('<div class="lmt-orange-msg" style="text-align:center;"><strong>You\'re signed up.</strong></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ASK BARB
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Ask Barb":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — using pre-set answers.</div>', unsafe_allow_html=True)

    h1("Pregúntale a Barb" if st.session_state.spanish_mode else "Ask Barb")
    st.markdown('<p style="color:#A8B8CC;font-size:18px;">No tech jargon. Just plain talk.</p>', unsafe_allow_html=True)
    hr()

    cats = {"Lesson Questions":["What is AI in plain English?","What are the 4 pressure tactics?","How do I set up two-factor authentication?","What is a passphrase?","What if I already sent money to a scammer?"],
            "Daily Life":["How can AI help me remember my medications?","Can AI help me write a letter to my doctor?","What's the easiest way to video call my family?"]}
    sel = st.selectbox("Choose a topic:", ["All Topics"]+list(cats.keys()))
    examples = [q for qs in cats.values() for q in qs[:1]] if sel=="All Topics" else cats[sel]
    for ex in examples:
        st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
        if st.button(ex, key=f"ex_{ex[:20]}", use_container_width=True): st.session_state["user_input"]=ex
        st.markdown('</div>', unsafe_allow_html=True)

    hr()

    if not st.session_state.messages:
        st.markdown(f'<div class="lmt-barb-greeting">Hi {st.session_state.student_name}! I\'m Barb. Ask me anything about the lessons or using AI. No question is too simple.</div>', unsafe_allow_html=True)

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    prompt = st.chat_input("Type your question here...")
    if "user_input" in st.session_state: prompt = st.session_state.pop("user_input")

    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        st.session_state.questions_asked += 1

        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            if not st.session_state.online:
                reply = offline_answer(prompt)
                st.markdown(reply)
            elif not can("live_ai"):
                # Free tier — limited offline-style answer + upgrade prompt
                reply = offline_answer(prompt)
                st.markdown(reply)
                st.markdown("""
                <div style="background:#1E3A5F;border-left:3px solid #C8942E;border-radius:6px;padding:10px 14px;margin-top:10px;font-size:15px;color:#A8B8CC;">
                    💡 <strong style="color:#C8942E;">Pioneer</strong> members get unlimited live AI answers.
                    <a href="#" style="color:#C8942E;">Upgrade for $9/mo →</a>
                </div>""", unsafe_allow_html=True)
            else:
                api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
                client  = anthropic.Anthropic(api_key=api_key)
                sys_p   = SYSTEM_PROMPT_ES if st.session_state.spanish_mode else SYSTEM_PROMPT
                with client.messages.stream(
                    model="claude-sonnet-4-6", max_tokens=1024, system=sys_p,
                    messages=[{"role":m["role"],"content":m["content"]} for m in st.session_state.messages],
                ) as stream:
                    reply = st.write_stream(stream.text_stream)

        st.session_state.messages.append({"role":"assistant","content":reply})
        st.session_state.last_reply = reply
        save_student(st.session_state.student_email)

        # Read aloud — Pioneer+
        if can("read_aloud"):
            lang_code = "es-US" if st.session_state.spanish_mode else "en-US"
            st.markdown(f"""
            <button onclick="window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance({json.dumps(reply)});u.lang='{lang_code}';u.rate=0.9;window.speechSynthesis.speak(u);"
            style="background:#1E3A5F;color:#C8942E;border:1.5px solid #C8942E;border-radius:20px;padding:8px 20px;font-size:16px;cursor:pointer;margin:8px 4px;font-family:'DM Sans',sans-serif;">🔊 Read aloud</button>
            <button onclick="window.speechSynthesis.cancel();"
            style="background:transparent;color:#A8B8CC;border:1px solid #A8B8CC;border-radius:20px;padding:8px 14px;font-size:14px;cursor:pointer;font-family:'DM Sans',sans-serif;">Stop</button>
            """, unsafe_allow_html=True)

        # Save conversation — Pioneer+
        if can("save_chat"):
            transcript = "\n\n".join([f"{'You' if m['role']=='user' else 'Barb'}: {m['content']}" for m in st.session_state.messages[-6:]])
            st.download_button("📄 Save conversation", data=transcript, file_name=f"barb-{datetime.now().strftime('%Y%m%d')}.txt", mime="text/plain", key=f"dl_{len(st.session_state.messages)}")

        col1, col2, _ = st.columns([1,1,4])
        with col1:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👍 Helpful", key=f"h_{len(st.session_state.messages)}"):
                st.session_state.helpful_count += 1; save_student(st.session_state.student_email); st.toast("Thanks!")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👎 Not helpful", key=f"nh_{len(st.session_state.messages)}"): st.toast("Thanks — I'll try to do better!")
            st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.instructor_mode and can("instructor"):
            st.markdown("""
            <div style="background:#0E2A1A;border:1px solid #109F35;border-radius:10px;padding:16px 20px;margin-top:14px;">
                <div style="font-size:12px;color:#109F35;font-weight:700;letter-spacing:1px;margin-bottom:8px;">INSTRUCTOR — WHAT JUST HAPPENED</div>
                <div style="color:#C4CDD9;font-size:16px;line-height:1.6;">
                <strong style="color:#C8942E;">1. Prompt typed</strong> — clearer question = better answer.<br><br>
                <strong style="color:#C8942E;">2. Full conversation sent</strong> — AI keeps context.<br><br>
                <strong style="color:#C8942E;">3. Response generated</strong> — one word at a time from training data.<br><br>
                <em style="color:#A8B8CC;">Barb didn't look this up — she generated it. Always verify important information.</em>
                </div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MY PROGRESS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "My Progress":
    h1(f"{st.session_state.student_name}'s Progress")
    hr()
    completed = len(st.session_state.lessons_completed)
    st.markdown(f'<div class="lmt-progress-card"><div style="font-size:13px;color:#A8B8CC;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px;">Lessons Completed</div><h2>{completed} of 3</h2><p>{"All three done — you\'re a Digital Pioneer!" if completed==3 else "Keep going!"}</p></div>', unsafe_allow_html=True)
    for lesson in LESSONS:
        done=lesson["number"] in st.session_state.lessons_completed
        icon="✓" if done else "○"; color="#109F35" if done else "#A8B8CC"
        st.markdown(f'<div style="display:flex;align-items:center;padding:10px 0;border-bottom:1px solid #1E3A5F;"><span style="font-size:22px;color:{color};margin-right:14px;">{icon}</span><div><div style="font-weight:700;color:#C4CDD9;">Lesson {lesson["number"]}: {lesson["title"]}</div><div style="font-size:15px;color:#A8B8CC;">{lesson["subtitle"]}</div></div></div>', unsafe_allow_html=True)
    hr()
    level,level_msg=get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f'<div class="lmt-progress-card"><div style="font-size:13px;color:#A8B8CC;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px;">Pioneer Level</div><h2>{level}</h2><p>{level_msg}</p></div>', unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c1: st.metric("Questions Asked", st.session_state.questions_asked)
    with c2: st.metric("Helpful Answers", st.session_state.helpful_count)
    with c3: st.metric("Lessons Done", completed)

# ══════════════════════════════════════════════════════════════════════════════
# UPGRADE PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Upgrade":
    h1("Upgrade Your Plan")
    st.markdown('<p style="color:#A8B8CC;font-size:18px;">Support the mission. Unlock more from Barb.</p>', unsafe_allow_html=True)
    hr()

    pioneer_link = os.environ.get("STRIPE_PIONEER_LINK") or st.secrets.get("STRIPE_PIONEER_LINK","#")
    org_link     = os.environ.get("STRIPE_ORG_LINK")     or st.secrets.get("STRIPE_ORG_LINK","#")
    email_param  = urllib.parse.quote(st.session_state.student_email)

    tier = st.session_state.student_tier

    plans = [
        {"name":"Free","price":"$0 / month","color":"#A8B8CC","border":"#1E3A5F",
         "features":["All 3 lessons","Barb offline answers","Progress tracker"],"cta":None,"current": tier=="free"},
        {"name":"Pioneer","price":"$9 / month","color":"#109F35","border":"#109F35",
         "features":["Everything in Free","Live AI — unlimited questions","Spanish mode","Read aloud","Save conversations"],"cta":f"{pioneer_link}?prefilled_email={email_param}","current": tier=="pioneer"},
        {"name":"Organization","price":"$49 / month","color":"#C8942E","border":"#C8942E",
         "features":["Everything in Pioneer","Instructor Mode","Class Roster","CSV export","Custom branding"],"cta":f"{org_link}?prefilled_email={email_param}","current": tier=="organization"},
    ]

    for plan in plans:
        features_html = "".join([f'<li style="color:#C4CDD9;margin-bottom:6px;">✓ {f}</li>' for f in plan["features"]])
        current_badge = '<span style="background:#1E3A5F;color:#A8B8CC;font-size:12px;border-radius:10px;padding:2px 10px;margin-left:8px;">Current Plan</span>' if plan["current"] else ""
        cta_html = f'<a href="{plan["cta"]}" target="_blank" style="display:block;background:{plan["color"]};color:#0E1C2F;font-weight:700;font-size:17px;text-align:center;padding:12px;border-radius:8px;text-decoration:none;margin-top:12px;">Upgrade to {plan["name"]} →</a>' if plan["cta"] and not plan["current"] else ""
        if plan["current"]: cta_html = f'<div style="text-align:center;color:{plan["color"]};font-weight:700;font-size:16px;margin-top:12px;">✓ Your current plan</div>'
        st.markdown(f"""
        <div style="background:#162640;border:2px solid {plan["border"]};border-radius:14px;padding:24px;margin:14px 0;">
            <div style="display:flex;align-items:center;margin-bottom:4px;">
                <span style="font-family:'Playfair Display',serif;font-size:1.4rem;color:{plan["color"]};">{plan["name"]}</span>
                {current_badge}
            </div>
            <div style="font-size:1.6rem;font-weight:700;color:#C4CDD9;margin-bottom:12px;">{plan["price"]}</div>
            <ul style="padding-left:16px;margin:0;">{features_html}</ul>
            {cta_html}
        </div>""", unsafe_allow_html=True)

    hr()
    st.markdown("""
    <div class="lmt-section-card">
        <h3>Frequently Asked Questions</h3>
        <ul>
            <li><strong style="color:#C8942E;">Can I cancel?</strong> Yes — cancel any time in your Stripe account. No fees, no questions.</li>
            <li><strong style="color:#C8942E;">Is my payment secure?</strong> Yes — payments are processed by Stripe. We never see your card number.</li>
            <li><strong style="color:#C8942E;">What if I need help?</strong> Email us at info@learnmoretechnologies.com</li>
            <li><strong style="color:#C8942E;">Can my library or senior center get Organization access?</strong> Yes — contact us about volume pricing.</li>
        </ul>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CLASS ROSTER (org only)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Class Roster":
    if not can("roster"):
        upgrade_prompt("Class Roster", "organization")
    else:
        h1("Class Roster")
        hr()
        students = load_all_students()
        if not students:
            st.markdown('<div class="lmt-orange-msg">No students yet — or Supabase not connected.</div>', unsafe_allow_html=True)
        else:
            c1,c2,c3,c4=st.columns(4)
            with c1: st.metric("Total Students", len(students))
            with c2: st.metric("All 3 Lessons Done", sum(1 for s in students if len(s.get("lessons_completed",[]))==3))
            with c3: st.metric("Total Questions", sum(s.get("questions_asked",0) for s in students))
            with c4: st.metric("Newsletter Signups", sum(1 for s in students if s.get("email_captured",False)))
            hr()
            rows=""
            for s in students:
                lessons=s.get("lessons_completed",[])
                lesson_str=" ".join([f"L{n}✓" for n in sorted(lessons)]) if lessons else "—"
                tier_s=s.get("tier","free")
                tier_badge=f'<span class="{tier_badge_class[tier_s]}">{tier_s}</span>'
                rows+=f'<tr><td>{s.get("name","—")}</td><td style="font-size:13px;">{s.get("email","—")}</td><td>{tier_badge}</td><td>{lesson_str}</td><td>{s.get("questions_asked",0)}</td><td>{"✓" if s.get("email_captured") else "—"}</td><td style="font-size:13px;">{str(s.get("last_seen",""))[:10]}</td></tr>'
            st.markdown(f'<table class="lmt-table"><thead><tr><th>Name</th><th>Email</th><th>Tier</th><th>Lessons</th><th>Questions</th><th>Subscribed</th><th>Last Seen</th></tr></thead><tbody>{rows}</tbody></table>', unsafe_allow_html=True)
            hr()
            if can("csv_export"):
                csv=["Name,Email,Tier,Lessons,Questions,Subscribed,Last Seen"]
                for s in students:
                    lessons="|".join(str(n) for n in sorted(s.get("lessons_completed",[])))
                    csv.append(f'{s.get("name","")},{s.get("email","")},{s.get("tier","free")},{lessons},{s.get("questions_asked",0)},{s.get("email_captured",False)},{str(s.get("last_seen",""))[:10]}')
                st.download_button("📥 Export CSV", data="\n".join(csv), file_name=f"barb-roster-{datetime.now().strftime('%Y%m%d')}.csv", mime="text/csv")

# ══════════════════════════════════════════════════════════════════════════════
# INSTRUCTOR GUIDE (org only)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Instructor Guide":
    if not can("instructor"):
        upgrade_prompt("Instructor Guide", "organization")
    else:
        h1("Instructor Guide")
        hr()
        st.markdown("""
        <div class="lmt-section-card" style="border-color:#C8942E;">
            <h3>Before Class Checklist</h3>
            <ul>
                <li>Instructor Mode ON → sidebar toggle</li>
                <li>Projector Mode ON → larger text for the screen</li>
                <li>Reset for New Class → clears all data</li>
                <li>Check connection indicator — green = live AI, orange = offline pre-set</li>
                <li>Run one demo question before students arrive</li>
            </ul>
        </div>
        <div class="lmt-section-card">
            <h3>What to Say When Students Ask</h3>
            <table class="lmt-table">
                <thead><tr><th>Student asks...</th><th>Say this</th></tr></thead>
                <tbody>
                    <tr><td>"Is Barb always right?"</td><td>"No. AI generates answers. Verify the important ones."</td></tr>
                    <tr><td>"Is this safe?"</td><td>"Yes — don't type passwords or SSN into any AI."</td></tr>
                    <tr><td>"Can I use this at home?"</td><td>"Yes — free at securestep.ai. Same email = your progress stays."</td></tr>
                    <tr><td>"No internet — now what?"</td><td>"Barb has pre-set answers for all lesson questions. She still works."</td></tr>
                </tbody>
            </table>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# RESOURCES
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Resources":
    h1("Resources")
    hr()
    st.markdown("""
    <div class="lmt-section-card">
        <h3>50+TechBridge</h3>
        <ul>
            <li><a href="https://50plustechbridge.com/start-free-lessons/" target="_blank">Start Free Lessons →</a></li>
            <li><a href="https://youtu.be/YsSXhxo_fus" target="_blank">Lesson 3 on YouTube</a></li>
        </ul>
    </div>
    <div class="lmt-section-card">
        <h3>Report a Scam</h3>
        <ul>
            <li><a href="https://reportfraud.ftc.gov" target="_blank">reportfraud.ftc.gov</a> — FTC</li>
            <li><a href="https://www.ic3.gov" target="_blank">ic3.gov</a> — FBI</li>
            <li><a href="https://www.identitytheft.gov" target="_blank">identitytheft.gov</a></li>
        </ul>
    </div>
    <div class="lmt-section-card">
        <h3>AI Safety Rules</h3>
        <ul>
            <li>Never type your Social Security number, bank info, or passwords into AI</li>
            <li>AI can be wrong — verify anything important with a real professional</li>
            <li>If it feels like a scam — hang up, look up the real number, call back</li>
        </ul>
    </div>""", unsafe_allow_html=True)
