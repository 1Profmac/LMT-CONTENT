import streamlit as st
import anthropic
import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ask Barb — 50+TechBridge", page_icon="🌟", layout="centered")

# ── Supabase helpers ──────────────────────────────────────────────────────────
def get_supabase_creds():
    url = os.environ.get("SUPABASE_URL") or st.secrets.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY", "")
    return url, key

def supabase_request(method, path, data=None):
    url, key = get_supabase_creds()
    if not url or not key:
        return None
    try:
        full_url = f"{url}/rest/v1/{path}"
        payload = json.dumps(data).encode() if data else None
        req = urllib.request.Request(
            full_url, data=payload, method=method,
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "Prefer": "return=representation",
            }
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None

def load_student(email: str):
    result = supabase_request("GET", f"students?email=eq.{urllib.parse.quote(email)}&select=*")
    if result and len(result) > 0:
        return result[0]
    return None

def create_student(email: str, name: str):
    data = {"email": email, "name": name, "lessons_completed": [], "questions_asked": 0,
            "helpful_count": 0, "email_captured": False, "pioneer_level": "New"}
    result = supabase_request("POST", "students", data)
    return result[0] if result else None

def save_student(email: str):
    if not email:
        return
    completed = sorted(list(st.session_state.lessons_completed))
    level, _ = get_pioneer_level(st.session_state.questions_asked)
    data = {
        "lessons_completed": completed,
        "questions_asked": st.session_state.questions_asked,
        "helpful_count": st.session_state.helpful_count,
        "email_captured": st.session_state.email_captured,
        "pioneer_level": level,
        "last_seen": datetime.utcnow().isoformat(),
    }
    supabase_request("PATCH", f"students?email=eq.{urllib.parse.quote(email)}", data)

def load_all_students():
    return supabase_request("GET", "students?select=*&order=last_seen.desc") or []

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
html, body, [class*="css"], .stApp { background-color: #0E1C2F !important; color: #C4CDD9 !important; font-family: 'DM Sans', sans-serif !important; font-size: 18px !important; }
.block-container { background-color: #0E1C2F !important; padding-top: 2rem !important; }
section[data-testid="stSidebar"] { background-color: #162640 !important; }
section[data-testid="stSidebar"] > div { background-color: #162640 !important; }
h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { font-family: 'Playfair Display', serif !important; color: #C8942E !important; }
p, li, label, span, div { font-family: 'DM Sans', sans-serif !important; color: #C4CDD9 !important; }
.stButton > button { background-color: #C8942E !important; color: #0E1C2F !important; font-family: 'DM Sans', sans-serif !important; font-weight: 700 !important; font-size: 18px !important; border-radius: 8px !important; border: none !important; padding: 12px 24px !important; min-height: 48px !important; width: 100% !important; cursor: pointer !important; }
.stButton > button:hover { background-color: #E8B84B !important; color: #0E1C2F !important; }
.pill-btn > button { background-color: #1E3A5F !important; color: #C8942E !important; border: 1.5px solid #C8942E !important; border-radius: 24px !important; font-weight: 600 !important; padding: 10px 20px !important; }
.pill-btn > button:hover { background-color: #C8942E !important; color: #0E1C2F !important; }
.outline-btn > button { background-color: transparent !important; color: #C8942E !important; border: 2px solid #C8942E !important; border-radius: 8px !important; }
.stChatMessage { font-size: 18px !important; border-radius: 10px !important; padding: 12px !important; margin-bottom: 10px !important; }
[data-testid="stChatMessageContent"] { font-size: 18px !important; color: #C4CDD9 !important; }
[data-testid="stChatMessage"][data-role="user"] { background-color: #1E3A5F !important; border-left: 4px solid #C8942E !important; }
[data-testid="stChatMessage"][data-role="assistant"] { background-color: #162640 !important; border-left: 4px solid #109F35 !important; }
.stChatInput textarea, .stChatInput input { background-color: #162640 !important; color: #C4CDD9 !important; border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important; }
.stTextInput input { background-color: #162640 !important; color: #C4CDD9 !important; border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important; padding: 10px 14px !important; }
.stTextInput input:focus { border-color: #C8942E !important; outline: none !important; }
.stSelectbox > div > div { background-color: #162640 !important; color: #C4CDD9 !important; border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important; }
.stRadio > div { background-color: transparent !important; }
.stRadio label { color: #C4CDD9 !important; font-size: 17px !important; }
[data-testid="stMetric"] { background-color: #162640 !important; border-radius: 10px !important; padding: 16px !important; border: 1px solid #1E3A5F !important; }
[data-testid="stMetricValue"] { color: #C8942E !important; font-family: 'Playfair Display', serif !important; font-size: 2rem !important; }
hr { border-color: #1E3A5F !important; }
.lmt-tip-card { background-color: #162640; border-left: 5px solid #C8942E; border-radius: 10px; padding: 20px 24px; margin: 12px 0; font-size: 18px; }
.lmt-progress-card { background-color: #162640; border: 2px solid #C8942E; border-radius: 12px; padding: 24px; margin: 12px 0; text-align: center; }
.lmt-progress-card h2 { font-family: 'Playfair Display', serif; color: #C8942E; margin: 0 0 8px 0; font-size: 2rem; }
.lmt-level-badge { background-color: #1E3A5F; border: 1.5px solid #C8942E; border-radius: 10px; padding: 12px 16px; margin: 8px 0; text-align: center; }
.lmt-level-badge strong { color: #C8942E; font-family: 'Playfair Display', serif; }
.lmt-section-card { background-color: #162640; border-radius: 12px; padding: 20px 24px; margin: 12px 0; border: 1px solid #1E3A5F; }
.lmt-section-card h3 { font-family: 'Playfair Display', serif; color: #C8942E; margin-top: 0; }
.lmt-section-card a { color: #C8942E; text-decoration: underline; }
.lmt-section-card ul { padding-left: 20px; }
.lmt-section-card li { color: #C4CDD9; margin-bottom: 8px; }
.lmt-barb-greeting { background-color: #162640; border-left: 4px solid #109F35; border-radius: 10px; padding: 20px 24px; margin: 12px 0; font-size: 18px; }
.lmt-orange-msg { background-color: rgba(232,115,58,0.15); border-left: 4px solid #E8733A; border-radius: 8px; padding: 16px 20px; color: #E8B84B; font-size: 18px; margin: 12px 0; }
.lmt-table { width: 100%; border-collapse: collapse; font-size: 16px; }
.lmt-table th { background-color: #1E3A5F; color: #C8942E; padding: 10px 14px; text-align: left; border-bottom: 2px solid #C8942E; }
.lmt-table td { background-color: #162640; color: #C4CDD9; padding: 10px 14px; border-bottom: 1px solid #1E3A5F; }
.lesson-card { background-color: #162640; border-radius: 14px; padding: 24px; margin: 14px 0; border: 1px solid #1E3A5F; }
.lesson-card.completed { border-color: #109F35; }
.lesson-badge { display: inline-block; background-color: #C8942E; color: #0E1C2F; font-weight: 700; font-size: 13px; border-radius: 20px; padding: 4px 14px; margin-bottom: 10px; }
.lesson-badge.done { background-color: #109F35; }
.lesson-title { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #C8942E; margin: 0 0 8px 0; }
.lesson-skills { color: #A8B8CC; font-size: 16px; margin: 0 0 12px 0; }
.skill-tag { display: inline-block; background-color: #1E3A5F; color: #C8942E; border: 1px solid #C8942E; border-radius: 20px; padding: 3px 12px; font-size: 14px; margin: 3px 3px 3px 0; }
.login-card { background-color: #162640; border: 2px solid #C8942E; border-radius: 16px; padding: 36px 32px; max-width: 480px; margin: 40px auto; }
.offline-banner { background-color: #2A1A0A; border: 1px solid #E8733A; border-radius: 8px; padding: 10px 16px; color: #E8B84B; font-size: 15px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# ── Offline FAQ ───────────────────────────────────────────────────────────────
OFFLINE_FAQ = {
    "what is ai": "AI stands for Artificial Intelligence. It's a computer program that reads your question and writes back a helpful answer in plain English. It's not magic, not alive, and not always right. Think of it like a very well-read assistant who has read millions of books. It predicts what a helpful answer looks like — it doesn't look things up like Google.",
    "can ai make mistakes": "Yes — AI can be wrong, especially about specific facts, recent news, or medical details. It generates answers based on patterns, not verified truth. Always double-check anything important with your doctor, a government website, or a trusted person.",
    "difference between ai and google": "Google finds pages that already exist. AI writes a new answer for your question. Google gives you links. AI gives you a conversation. AI is better for 'help me write a letter' or 'explain this simply.' Google is better for finding a specific website or phone number.",
    "how do i use chatgpt": "Go to chat.openai.com on your phone or computer. You can use it without an account — just click 'Try ChatGPT.' Type your question in the box at the bottom, just like sending a text. Press Enter. ChatGPT writes back. If you don't like the answer, ask again differently.",
    "how do i ask a good question": "Be specific. Instead of typing 'health' — type 'What questions should I ask my doctor before a knee replacement?' The more detail you give, the better the answer. If it's too long, type: 'Can you say that in two sentences?'",
    "what are the pressure tactics": "Scammers use four levers: HURRY (act now, 20 minutes), FEAR (you'll be arrested, your account is compromised), SECRECY (don't tell your family), and AUTHORITY (badge number, case number, familiar logo). If you feel any of these — stop. Hang up. Call back on a number you already had.",
    "what is two factor authentication": "Two-factor authentication — 2FA — adds a second lock after your password. The site sends a code to your phone. You type it in. Even if someone steals your password, they can't get in without that code. Turn it on for email first, then your bank.",
    "how do i set up two factor": "Go to your email settings → Security → look for 'Two-factor authentication,' '2-step verification,' or 'Multifactor.' Follow the steps. Takes about 5 minutes. Turn it on for email first — email is the skeleton key to everything else.",
    "what is a passphrase": "A passphrase is random words used as a password — like 'maple-porch-radio-Thursday.' Longer means harder to crack and easier to remember. The government's own security experts now recommend passphrases over short complicated passwords.",
    "never move money": "No real bank, government agency, or official ever asks you to move money to protect it. Not to a gift card. Not to a wire transfer. Not to a Bitcoin ATM. Not to a courier. If someone says your money is in danger and you need to move it — that IS the scam.",
    "what if i already sent money": "Stop immediately. Call your bank — number on the back of your card — say 'gift card,' 'wire transfer,' or 'crypto ATM.' Change your email password and turn on 2FA. Report at reportfraud.ftc.gov and ic3.gov. Tell one trusted person. Speed matters.",
    "what is a family code word": "A family code word is a secret phrase only your family knows. If someone calls claiming to be your grandchild or family member — ask for the code word. If they can't give it, hang up and call your family member on the number in your phone.",
    "gift cards": "No real government agency, bank, or emergency ever requires payment in gift cards. Anyone who asks for a gift card number as payment is a scammer. Full stop.",
    "how do i spot a fake": "Check four things: 1) The sender domain — would Amazon write from 'email-secure-alert.com'? 2) The greeting — 'Dear Customer' from your bank is a warning. 3) The ask — a link, download, QR code, or code they want read to them. 4) Did you start this? If they contacted you first, treat it as suspicious.",
    "how do i report a scam": "Report at reportfraud.ftc.gov (FTC) and ic3.gov (FBI). If identity was stolen: identitytheft.gov. Reporting helps protect others.",
    "where are classes": "50+TechBridge classes are held at Austin Public Library branches, AARP senior centers, and Foundation Communities. All free. Visit 50plustechbridge.com for the schedule.",
}

def offline_answer(question: str) -> str:
    q = question.lower().strip()
    for key, answer in OFFLINE_FAQ.items():
        if key in q:
            return answer
    best_key, best_score = None, 0
    q_words = set(q.split())
    for key in OFFLINE_FAQ:
        score = len(q_words & set(key.split()))
        if score > best_score:
            best_score, best_key = score, key
    if best_key and best_score >= 1:
        return OFFLINE_FAQ[best_key]
    return "I'm in offline mode and don't have a stored answer for that. Ask your instructor — or when internet is restored, I can answer anything."

# ── Lesson data ───────────────────────────────────────────────────────────────
LESSONS = [
    {"number": 1, "title": "Welcome to AI", "subtitle": "What AI is, what it isn't, and your first real question",
     "skills": ["What AI actually is", "How to ask a good question", "Staying in charge"],
     "url": "https://50plustechbridge.com/start-free-lessons/", "youtube": None},
    {"number": 2, "title": "Talk to AI", "subtitle": "Have a real conversation with ChatGPT or Claude",
     "skills": ["Opening ChatGPT on your phone", "Asking your first question", "Getting better answers"],
     "url": "https://50plustechbridge.com/start-free-lessons/", "youtube": None},
    {"number": 3, "title": "Don't Get Scammed", "subtitle": "3 skills that keep scammers away from your money",
     "skills": ["Spot a Fake", "Name the Pressure", "Passwords & the Second Lock"],
     "url": "https://50plustechbridge.com/start-free-lessons/", "youtube": "https://youtu.be/YsSXhxo_fus"},
]

SYSTEM_PROMPT = """You are Barb, a warm, patient AI guide for adults over 50 learning through 50+TechBridge's free lessons. You know all three lesson topics: what AI is, how to talk to AI, and scam prevention (spot a fake, name the pressure, passwords and 2FA). Use simple language, no jargon, 3-5 short paragraphs max, always encouraging."""
SYSTEM_PROMPT_ES = """Eres Barb, una guía de IA cálida para adultos mayores de 50 años del programa 50+TechBridge. Responde en español simple y claro. Sin jerga técnica. Máximo 3-5 párrafos cortos."""

# ── Pioneer levels ────────────────────────────────────────────────────────────
def get_pioneer_level(q):
    if q >= 50: return "Trailblazer", "You're leading the way!"
    if q >= 25: return "Pioneer", "You're exploring with confidence!"
    if q >= 10: return "Explorer", "You're getting comfortable with AI!"
    if q >= 1:  return "Beginner", "You've taken your first step!"
    return "New", "Ask your first question to get started!"

# ── Session state defaults ────────────────────────────────────────────────────
defaults = {
    "messages": [], "questions_asked": 0, "helpful_count": 0,
    "lessons_completed": set(), "instructor_mode": False,
    "projector_mode": False, "spanish_mode": False,
    "email_captured": False, "last_reply": "",
    "logged_in": False, "student_email": "", "student_name": "",
    "online": True, "connectivity_checked": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

if not st.session_state.connectivity_checked:
    st.session_state.online = check_internet()
    st.session_state.connectivity_checked = True

# ── Projector CSS ─────────────────────────────────────────────────────────────
if st.session_state.projector_mode:
    st.markdown("""<style>
    html, body, [class*="css"], .stApp, p, li, label, span, div { font-size: 24px !important; }
    .stChatMessage, [data-testid="stChatMessageContent"] { font-size: 24px !important; }
    h1 { font-size: 3.5rem !important; } h2 { font-size: 2rem !important; }
    .stButton > button { font-size: 22px !important; padding: 16px 28px !important; }
    </style>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LOGIN SCREEN
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    st.markdown("""
    <div style="text-align:center; padding-top:20px;">
        <div style="font-family:'Playfair Display',serif; font-size:3rem; color:#C8942E;">Ask Barb</div>
        <div style="color:#A8B8CC; font-size:18px; margin-bottom:30px;">50+TechBridge Free Lessons</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.5rem; color:#C8942E; margin-bottom:6px;">Welcome!</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#A8B8CC; font-size:16px; margin-bottom:20px;">Enter your name and email to get started. Your progress will be saved automatically.</div>', unsafe_allow_html=True)

        name_input  = st.text_input("Your first name:", placeholder="e.g. Margaret", key="login_name")
        email_input = st.text_input("Your email address:", placeholder="yourname@email.com", key="login_email")

        if st.button("Let's Go →", key="login_btn"):
            if not name_input.strip():
                st.warning("Please enter your first name.")
            elif "@" not in email_input or "." not in email_input:
                st.warning("Please enter a valid email address.")
            else:
                email = email_input.strip().lower()
                name  = name_input.strip()

                # Try to load existing student
                existing = load_student(email)

                if existing:
                    # Returning student — restore progress
                    st.session_state.student_email      = email
                    st.session_state.student_name       = existing.get("name", name)
                    st.session_state.questions_asked    = existing.get("questions_asked", 0)
                    st.session_state.helpful_count      = existing.get("helpful_count", 0)
                    st.session_state.email_captured     = existing.get("email_captured", False)
                    st.session_state.lessons_completed  = set(existing.get("lessons_completed", []))
                    st.session_state.logged_in          = True
                    st.session_state.returning_student  = True
                else:
                    # New student — create record
                    create_student(email, name)
                    st.session_state.student_email     = email
                    st.session_state.student_name      = name
                    st.session_state.logged_in         = True
                    st.session_state.returning_student = False

                st.rerun()

        st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; color:#A8B8CC; text-align:center;">No password needed. Your email is only used to save your progress.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP (logged in)
# ══════════════════════════════════════════════════════════════════════════════

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("logo.png", width=160)
    except Exception:
        pass

    lang = "ES" if st.session_state.spanish_mode else "EN"
    st.markdown(f"""
    <div style="margin-top:4px; margin-bottom:2px;">
        <span style="font-family:'Playfair Display',serif; font-size:22px; font-weight:800; color:#C8942E;">Ask Barb</span>
        <span style="font-size:11px; color:#A8B8CC; margin-left:6px;">{lang}</span>
    </div>
    <div style="font-size:15px; color:#C8942E; font-weight:700; margin:4px 0;">
        {st.session_state.student_name}
    </div>
    <div style="font-size:13px; color:#A8B8CC;">{st.session_state.student_email}</div>
    """, unsafe_allow_html=True)

    status_color = "#109F35" if st.session_state.online else "#E8733A"
    status_text  = "Online" if st.session_state.online else "Offline"
    st.markdown(f'<div style="font-size:12px; color:{status_color}; margin:6px 0;">● {status_text}</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:8px 0;'>", unsafe_allow_html=True)

    nav_options = ["Home", "Free Lessons", "Ask Barb", "My Progress", "Resources"]
    if st.session_state.instructor_mode:
        nav_options.append("Instructor Guide")
        nav_options.append("Class Roster")
    page = st.radio("Navigate", nav_options, label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1E3A5F; margin:8px 0;'>", unsafe_allow_html=True)

    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-level-badge">
        <div style="font-size:12px; color:#A8B8CC; margin-bottom:2px;">Lessons Completed</div>
        <strong style="font-size:22px;">{completed} / 3</strong>
    </div>""", unsafe_allow_html=True)

    level, _ = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f'<div style="text-align:center; margin:6px 0; font-size:14px; color:#A8B8CC;">Level: <span style="color:#C8942E; font-weight:700;">{level}</span></div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:8px 0;'>", unsafe_allow_html=True)

    st.markdown("<div style='font-size:11px; color:#A8B8CC; margin-bottom:4px;'>INSTRUCTOR</div>", unsafe_allow_html=True)
    st.session_state.instructor_mode = st.toggle("Instructor Mode", value=st.session_state.instructor_mode)
    if st.session_state.instructor_mode:
        st.session_state.projector_mode = st.toggle("Projector Mode", value=st.session_state.projector_mode)
        if st.button("Reset for New Class"):
            st.session_state.messages = []
            st.session_state.questions_asked = 0
            st.session_state.helpful_count = 0
            st.session_state.lessons_completed = set()
            st.session_state.email_captured = False
            st.session_state.logged_in = False
            st.session_state.student_email = ""
            st.session_state.student_name = ""
            st.toast("Reset — ready for new class.")
            st.rerun()

    st.markdown("<hr style='border-color:#1E3A5F; margin:8px 0;'>", unsafe_allow_html=True)
    st.session_state.spanish_mode = st.toggle("Español", value=st.session_state.spanish_mode)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("Log Out"):
            save_student(st.session_state.student_email)
            for k in defaults:
                st.session_state[k] = defaults[k]
            st.rerun()

# ── Welcome back toast ────────────────────────────────────────────────────────
if st.session_state.get("returning_student") and "welcomed" not in st.session_state:
    completed = len(st.session_state.lessons_completed)
    st.toast(f"Welcome back, {st.session_state.student_name}! {completed}/3 lessons complete.")
    st.session_state["welcomed"] = True

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — Barb is using pre-set answers.</div>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif; font-size:2.8rem; color:#C8942E;">Hi, {st.session_state.student_name}.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC; font-size:20px; margin-bottom:0;">Your AI guide for the 50+TechBridge free lessons.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    daily_tips = [
        "A passphrase like 'maple-porch-radio-Thursday' is stronger AND easier to remember than a short jumbled password.",
        "The real IRS and Social Security will never call demanding gift cards or asking you to move money.",
        "AI is a conversation, not a search engine. Ask again if you don't like the first answer.",
        "Turn on two-factor authentication on your email this week — it's the single best security step you can take.",
        "Pick a family code word. Share it only with people you'd send money to. If they can't say it — hang up.",
    ]
    tip = daily_tips[datetime.now().timetuple().tm_yday % len(daily_tips)]
    st.markdown(f'<div class="lmt-tip-card"><strong style="color:#C8942E;">Today\'s tip:</strong> {tip}</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown('<h2 style="font-family:\'Playfair Display\',serif; font-size:1.3rem; color:#C8942E;">Your Lessons</h2>', unsafe_allow_html=True)
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
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — lesson links open when internet returns.</div>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Free Lessons</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC; font-size:18px;">Three lessons. Watch, learn, ask Barb anything along the way.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E; margin-bottom:20px;">
        <div style="font-family:'Playfair Display',serif; font-size:1.2rem; color:#C8942E; margin-bottom:6px;">Ready to try AI yourself?</div>
        <div style="color:#C4CDD9; font-size:17px; margin-bottom:14px;">Open ChatGPT free — no account needed. Practice what you learned in Lesson 2.</div>
        <a href="https://chat.openai.com" target="_blank"
           style="display:inline-block; background:#C8942E; color:#0E1C2F; font-weight:700; font-size:18px;
                  padding:12px 28px; border-radius:8px; text-decoration:none;">Open ChatGPT →</a>
        <span style="color:#A8B8CC; font-size:14px; margin-left:14px;">Opens in a new tab</span>
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

        col1, col2, col3 = st.columns([2, 2, 2])
        with col1:
            st.markdown(f'<a href="{lesson["url"]}" target="_blank" style="display:block; background:#C8942E; color:#0E1C2F; font-weight:700; text-align:center; padding:10px; border-radius:8px; text-decoration:none;">Watch Lesson {lesson["number"]} →</a>', unsafe_allow_html=True)
        with col2:
            if lesson["youtube"]:
                st.markdown(f'<a href="{lesson["youtube"]}" target="_blank" style="display:block; background:#1E3A5F; color:#C8942E; font-weight:700; text-align:center; padding:10px; border-radius:8px; text-decoration:none; border:1.5px solid #C8942E;">▶ YouTube</a>', unsafe_allow_html=True)
        with col3:
            if st.button("↩ Undo" if done else "✓ Mark Done", key=f"done_{lesson['number']}", use_container_width=True):
                if done:
                    st.session_state.lessons_completed.discard(lesson["number"])
                else:
                    st.session_state.lessons_completed.add(lesson["number"])
                save_student(st.session_state.student_email)
                st.rerun()

        with st.expander(f"Ask Barb about Lesson {lesson['number']}"):
            followups = {
                1: ["What is AI in plain English?", "Can AI make mistakes?", "What's the difference between AI and Google?"],
                2: ["How do I open ChatGPT on my phone?", "What's a good first question to ask AI?", "What if I don't like AI's answer?"],
                3: ["What are the 4 pressure tactics scammers use?", "How do I set up two-factor authentication?", "What do I do if I already sent money to a scammer?", "What is a family code word?"],
            }
            for q in followups[lesson["number"]]:
                st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
                if st.button(q, key=f"lq_{lesson['number']}_{q[:15]}", use_container_width=True):
                    st.session_state["user_input"] = q
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    # Completion
    if len(st.session_state.lessons_completed) == 3:
        col_logo, col_text = st.columns([1, 2])
        with col_logo:
            try:
                st.image("agentic50-logo.png", width=160)
            except Exception:
                st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:2rem; color:#C8942E; text-align:center;">Agentic50</div>', unsafe_allow_html=True)
        with col_text:
            st.markdown(f"""
            <div style="padding:12px 0;">
                <div style="font-family:'Playfair Display',serif; font-size:1.4rem; color:#C8942E;">You're a Digital Pioneer, {st.session_state.student_name}.</div>
                <div style="color:#C4CDD9; font-size:17px; margin-top:6px;">All 3 lessons complete. Follow Agentic50 — weekly AI news for people like you.</div>
            </div>""", unsafe_allow_html=True)

        if not st.session_state.email_captured:
            st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#C8942E; margin-bottom:8px;">Get weekly AI tips in your inbox — free.</div>', unsafe_allow_html=True)
            confirm_email = st.text_input("Confirm your email:", value=st.session_state.student_email, key="confirm_email")
            if st.button("Sign Me Up →", key="ml_signup"):
                try:
                    ml_key   = os.environ.get("MAILERLITE_API_KEY") or st.secrets.get("MAILERLITE_API_KEY", "")
                    ml_group = os.environ.get("MAILERLITE_GROUP_ID") or st.secrets.get("MAILERLITE_GROUP_ID", "")
                    if ml_key and ml_group:
                        payload = json.dumps({"email": confirm_email, "groups": [ml_group],
                                              "fields": {"name": st.session_state.student_name}}).encode()
                        req = urllib.request.Request(
                            "https://connect.mailerlite.com/api/subscribers", data=payload, method="POST",
                            headers={"Content-Type": "application/json", "Authorization": f"Bearer {ml_key}"}
                        )
                        urllib.request.urlopen(req, timeout=5)
                    st.session_state.email_captured = True
                    save_student(st.session_state.student_email)
                    st.toast("You're in! Welcome to the community.")
                    st.rerun()
                except Exception:
                    st.session_state.email_captured = True
                    save_student(st.session_state.student_email)
                    st.rerun()
        else:
            st.markdown('<div class="lmt-orange-msg" style="text-align:center;"><strong>You\'re signed up.</strong> See you in your inbox.</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ASK BARB
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Ask Barb":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — using pre-set answers for lesson questions.</div>', unsafe_allow_html=True)

    label = "Pregúntale a Barb" if st.session_state.spanish_mode else "Ask Barb"
    sub   = "Sin jerga tecnológica." if st.session_state.spanish_mode else "No tech jargon. Just plain talk."
    st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">{label}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#A8B8CC; font-size:18px;">{sub}</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    categories = {
        "Lesson Questions": ["What is AI in plain English?", "What are the 4 pressure tactics scammers use?",
                             "How do I set up two-factor authentication?", "What is a passphrase?",
                             "What if I already sent money to a scammer?", "What is a family code word?"],
        "Health & Medications": ["How can AI help me remember my medications?", "Can AI help me prepare for a doctor's appointment?"],
        "Money & Bills": ["How do I spot an online scam?", "Can AI help me manage my bills?"],
        "Staying Connected": ["What's the easiest way to video call my family?", "Can AI help me write letters or emails?"],
    }
    selected_cat = st.selectbox("Choose a topic:", ["All Topics"] + list(categories.keys()))
    examples = [q for qs in categories.values() for q in qs[:1]] if selected_cat == "All Topics" else categories[selected_cat]

    for example in examples:
        st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
        if st.button(example, key=f"ex_{example[:25]}", use_container_width=True):
            st.session_state["user_input"] = example
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    if not st.session_state.messages:
        greeting = f"¡Hola, {st.session_state.student_name}! Soy Barb." if st.session_state.spanish_mode else f"Hi {st.session_state.student_name}! I'm Barb. Ask me anything about the lessons or using AI. No question is too simple."
        st.markdown(f'<div class="lmt-barb-greeting">{greeting}</div>', unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    placeholder = "Escribe tu pregunta aquí..." if st.session_state.spanish_mode else "Type your question here..."
    prompt = st.chat_input(placeholder)
    if "user_input" in st.session_state:
        prompt = st.session_state.pop("user_input")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.questions_asked += 1

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if not st.session_state.online:
                reply = offline_answer(prompt)
                st.markdown(reply)
            else:
                api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
                client  = anthropic.Anthropic(api_key=api_key)
                sys_p   = SYSTEM_PROMPT_ES if st.session_state.spanish_mode else SYSTEM_PROMPT
                with client.messages.stream(
                    model="claude-sonnet-4-6", max_tokens=1024, system=sys_p,
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                ) as stream:
                    reply = st.write_stream(stream.text_stream)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.session_state.last_reply = reply
        save_student(st.session_state.student_email)

        # Read aloud
        lang_code = "es-US" if st.session_state.spanish_mode else "en-US"
        tts_label = "🔊 Leer en voz alta" if st.session_state.spanish_mode else "🔊 Read aloud"
        st.markdown(f"""
        <button onclick="window.speechSynthesis.cancel(); var u=new SpeechSynthesisUtterance({json.dumps(reply)});
        u.lang='{lang_code}'; u.rate=0.9; window.speechSynthesis.speak(u);"
        style="background:#1E3A5F; color:#C8942E; border:1.5px solid #C8942E; border-radius:20px;
               padding:8px 20px; font-size:16px; cursor:pointer; margin:8px 4px; font-family:'DM Sans',sans-serif;">{tts_label}</button>
        <button onclick="window.speechSynthesis.cancel();"
        style="background:transparent; color:#A8B8CC; border:1px solid #A8B8CC; border-radius:20px;
               padding:8px 14px; font-size:14px; cursor:pointer; font-family:'DM Sans',sans-serif;">Stop</button>
        """, unsafe_allow_html=True)

        # Save conversation
        transcript = "\n\n".join([f"{'You' if m['role']=='user' else 'Barb'}: {m['content']}" for m in st.session_state.messages[-6:]])
        st.download_button("📄 Save conversation", data=transcript,
                           file_name=f"barb-{datetime.now().strftime('%Y%m%d')}.txt",
                           mime="text/plain", key=f"dl_{len(st.session_state.messages)}")

        col1, col2, _ = st.columns([1, 1, 4])
        with col1:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👍 Helpful", key=f"h_{len(st.session_state.messages)}"):
                st.session_state.helpful_count += 1
                save_student(st.session_state.student_email)
                st.toast("Thanks!")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👎 Not helpful", key=f"nh_{len(st.session_state.messages)}"):
                st.toast("Thanks — I'll try to do better!")
            st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.instructor_mode:
            st.markdown("""
            <div style="background:#0E2A1A; border:1px solid #109F35; border-radius:10px; padding:16px 20px; margin-top:14px;">
                <div style="font-size:12px; color:#109F35; font-weight:700; letter-spacing:1px; margin-bottom:8px;">INSTRUCTOR — WHAT JUST HAPPENED</div>
                <div style="color:#C4CDD9; font-size:16px; line-height:1.6;">
                <strong style="color:#C8942E;">1. Prompt typed</strong> — the clearer the question, the better the answer.<br><br>
                <strong style="color:#C8942E;">2. Full conversation sent</strong> — AI keeps context like a conversation with a friend.<br><br>
                <strong style="color:#C8942E;">3. Response generated</strong> — one word at a time, based on billions of training examples.<br><br>
                <em style="color:#A8B8CC;">Barb didn't look this up — she generated it. Always verify important information.</em>
                </div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MY PROGRESS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "My Progress":
    st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">{st.session_state.student_name}\'s Progress</h1>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-progress-card">
        <div style="font-size:13px; color:#A8B8CC; margin-bottom:6px; text-transform:uppercase; letter-spacing:1px;">Lessons Completed</div>
        <h2>{completed} of 3</h2>
        <p>{"All three done — you're a Digital Pioneer!" if completed == 3 else "Keep going — every lesson builds confidence."}</p>
    </div>""", unsafe_allow_html=True)

    for lesson in LESSONS:
        done  = lesson["number"] in st.session_state.lessons_completed
        icon  = "✓" if done else "○"
        color = "#109F35" if done else "#A8B8CC"
        st.markdown(f"""
        <div style="display:flex; align-items:center; padding:10px 0; border-bottom:1px solid #1E3A5F;">
            <span style="font-size:22px; color:{color}; margin-right:14px;">{icon}</span>
            <div>
                <div style="font-weight:700; color:#C4CDD9;">Lesson {lesson['number']}: {lesson['title']}</div>
                <div style="font-size:15px; color:#A8B8CC;">{lesson['subtitle']}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
    level, level_msg = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f"""
    <div class="lmt-progress-card">
        <div style="font-size:13px; color:#A8B8CC; margin-bottom:6px; text-transform:uppercase; letter-spacing:1px;">Pioneer Level</div>
        <h2>{level}</h2><p>{level_msg}</p>
    </div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Questions Asked", st.session_state.questions_asked)
    with col2: st.metric("Helpful Answers", st.session_state.helpful_count)
    with col3: st.metric("Lessons Done", completed)

# ══════════════════════════════════════════════════════════════════════════════
# RESOURCES
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Resources":
    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Resources</h1>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="lmt-section-card">
        <h3>50+TechBridge Free Lessons</h3>
        <ul>
            <li><a href="https://50plustechbridge.com/start-free-lessons/" target="_blank">Start Free Lessons →</a></li>
            <li><a href="https://youtu.be/YsSXhxo_fus" target="_blank">Lesson 3 on YouTube: Don't Get Scammed</a></li>
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
            <li>Never type your Social Security number, bank info, or passwords into any AI</li>
            <li>AI can be wrong — verify anything important with a real professional</li>
            <li>If it feels like a scam — hang up, look up the real number, call back</li>
        </ul>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CLASS ROSTER (instructor only)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Class Roster":
    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Class Roster</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC; font-size:18px;">Every student who has used Barb — progress, activity, level.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    students = load_all_students()

    if not students:
        st.markdown('<div class="lmt-orange-msg">No students yet — or Supabase is not connected. See SUPABASE-SETUP.md to configure.</div>', unsafe_allow_html=True)
    else:
        total     = len(students)
        done_all  = sum(1 for s in students if len(s.get("lessons_completed", [])) == 3)
        total_q   = sum(s.get("questions_asked", 0) for s in students)
        subscribed = sum(1 for s in students if s.get("email_captured", False))

        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Total Students", total)
        with col2: st.metric("All 3 Lessons Done", done_all)
        with col3: st.metric("Total Questions Asked", total_q)
        with col4: st.metric("Newsletter Signups", subscribed)

        st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

        # Table
        rows = ""
        for s in students:
            lessons = s.get("lessons_completed", [])
            lesson_str = " ".join([f"L{n}✓" for n in sorted(lessons)]) if lessons else "—"
            last = s.get("last_seen", "")[:10] if s.get("last_seen") else "—"
            email_icon = "✓" if s.get("email_captured") else "—"
            rows += f"""<tr>
                <td>{s.get('name','—')}</td>
                <td style="font-size:14px;">{s.get('email','—')}</td>
                <td>{lesson_str}</td>
                <td>{s.get('questions_asked', 0)}</td>
                <td>{s.get('pioneer_level','—')}</td>
                <td>{email_icon}</td>
                <td style="font-size:13px;">{last}</td>
            </tr>"""

        st.markdown(f"""
        <table class="lmt-table">
            <thead><tr>
                <th>Name</th><th>Email</th><th>Lessons</th>
                <th>Questions</th><th>Level</th><th>Subscribed</th><th>Last Seen</th>
            </tr></thead>
            <tbody>{rows}</tbody>
        </table>""", unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

        # Export
        csv_lines = ["Name,Email,Lessons Completed,Questions Asked,Pioneer Level,Subscribed,Last Seen"]
        for s in students:
            lessons = "|".join(str(n) for n in sorted(s.get("lessons_completed", [])))
            csv_lines.append(f"{s.get('name','')},{s.get('email','')},{lessons},{s.get('questions_asked',0)},{s.get('pioneer_level','')},{s.get('email_captured',False)},{s.get('last_seen','')[:10]}")
        st.download_button("📥 Export Roster as CSV", data="\n".join(csv_lines),
                           file_name=f"barb-roster-{datetime.now().strftime('%Y%m%d')}.csv",
                           mime="text/csv")

# ══════════════════════════════════════════════════════════════════════════════
# INSTRUCTOR GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Instructor Guide":
    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Instructor Guide</h1>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E;">
        <h3>Before Class Checklist</h3>
        <ul>
            <li>Turn on <strong style="color:#C8942E;">Instructor Mode</strong> in the sidebar</li>
            <li>Turn on <strong style="color:#C8942E;">Projector Mode</strong> for the classroom screen</li>
            <li>Click <strong style="color:#C8942E;">Reset for New Class</strong> — clears all data</li>
            <li>Check the connection indicator — green = live AI, orange = offline pre-set answers</li>
            <li>Run one demo question yourself before students arrive</li>
        </ul>
    </div>
    <div class="lmt-section-card">
        <h3>Quick Reference — What to Say When Students Ask</h3>
        <table class="lmt-table">
            <thead><tr><th>If a student asks...</th><th>Say this</th></tr></thead>
            <tbody>
                <tr><td>"Is Barb always right?"</td><td>"No. AI generates answers. You verify the important ones."</td></tr>
                <tr><td>"Is this safe?"</td><td>"Yes — don't type passwords or SSN into any AI. Everything else is fine."</td></tr>
                <tr><td>"What if I can't spell?"</td><td>"Doesn't matter. AI understands what you mean, even with typos."</td></tr>
                <tr><td>"Can I use this at home?"</td><td>"Yes — free at securestep.ai. Log in with the same email to keep your progress."</td></tr>
                <tr><td>"What if there's no internet?"</td><td>"Barb has pre-set answers for all lesson questions — she still works offline."</td></tr>
            </tbody>
        </table>
    </div>""", unsafe_allow_html=True)
