import streamlit as st
import anthropic
import os
import json
import urllib.request
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ask Barb — 50+TechBridge", page_icon="🌟", layout="centered")

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
h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { font-family: 'Playfair Display', serif !important; color: #C8942E !important; }
p, li, label, span, div { font-family: 'DM Sans', sans-serif !important; color: #C4CDD9 !important; }
.stButton > button { background-color: #C8942E !important; color: #0E1C2F !important; font-family: 'DM Sans', sans-serif !important; font-weight: 700 !important; font-size: 18px !important; border-radius: 8px !important; border: none !important; padding: 12px 24px !important; min-height: 48px !important; width: 100% !important; cursor: pointer !important; }
.stButton > button:hover { background-color: #E8B84B !important; color: #0E1C2F !important; }
.pill-btn > button { background-color: #1E3A5F !important; color: #C8942E !important; border: 1.5px solid #C8942E !important; border-radius: 24px !important; font-weight: 600 !important; padding: 10px 20px !important; }
.pill-btn > button:hover { background-color: #C8942E !important; color: #0E1C2F !important; }
.outline-btn > button { background-color: transparent !important; color: #C8942E !important; border: 2px solid #C8942E !important; border-radius: 8px !important; }
.outline-btn > button:hover { background-color: #C8942E !important; color: #0E1C2F !important; }
.stChatMessage { font-size: 18px !important; border-radius: 10px !important; padding: 12px !important; margin-bottom: 10px !important; }
[data-testid="stChatMessageContent"] { font-size: 18px !important; color: #C4CDD9 !important; }
[data-testid="stChatMessage"][data-role="user"] { background-color: #1E3A5F !important; border-left: 4px solid #C8942E !important; }
[data-testid="stChatMessage"][data-role="assistant"] { background-color: #162640 !important; border-left: 4px solid #109F35 !important; }
.stChatInput textarea, .stChatInput input { background-color: #162640 !important; color: #C4CDD9 !important; border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important; }
.stChatInput textarea:focus, .stChatInput input:focus { border-color: #C8942E !important; outline: none !important; }
.stSelectbox > div > div { background-color: #162640 !important; color: #C4CDD9 !important; border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important; }
.stRadio > div { background-color: transparent !important; }
.stRadio label { color: #C4CDD9 !important; font-size: 17px !important; }
[data-testid="stMetric"] { background-color: #162640 !important; border-radius: 10px !important; padding: 16px !important; border: 1px solid #1E3A5F !important; }
[data-testid="stMetricValue"] { color: #C8942E !important; font-family: 'Playfair Display', serif !important; font-size: 2rem !important; }
hr { border-color: #1E3A5F !important; }
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 { color: #C8942E !important; }
section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] label { color: #C4CDD9 !important; }
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
.lmt-cat-card { background-color: #162640; border-radius: 10px; padding: 18px 20px; margin: 6px 0; border: 1px solid #1E3A5F; }
.lmt-cat-card .cat-title { color: #C8942E; font-weight: 700; font-size: 18px; }
.lmt-cat-card .cat-example { color: #A8B8CC; font-size: 15px; margin-top: 4px; }
.lmt-hero-sub { color: #A8B8CC; font-size: 20px; margin-bottom: 8px; }
.lmt-orange-msg { background-color: rgba(232, 115, 58, 0.15); border-left: 4px solid #E8733A; border-radius: 8px; padding: 16px 20px; color: #E8B84B; font-size: 18px; margin: 12px 0; }
.lmt-barb-greeting { background-color: #162640; border-left: 4px solid #109F35; border-radius: 10px; padding: 20px 24px; margin: 12px 0; font-size: 18px; }
.lmt-table { width: 100%; border-collapse: collapse; font-size: 17px; }
.lmt-table th { background-color: #1E3A5F; color: #C8942E; padding: 12px 16px; text-align: left; border-bottom: 2px solid #C8942E; }
.lmt-table td { background-color: #162640; color: #C4CDD9; padding: 12px 16px; border-bottom: 1px solid #1E3A5F; }
.lesson-card { background-color: #162640; border-radius: 14px; padding: 24px; margin: 14px 0; border: 1px solid #1E3A5F; }
.lesson-card.completed { border-color: #109F35; }
.lesson-badge { display: inline-block; background-color: #C8942E; color: #0E1C2F; font-weight: 700; font-size: 13px; border-radius: 20px; padding: 4px 14px; margin-bottom: 10px; }
.lesson-badge.done { background-color: #109F35; }
.lesson-title { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #C8942E; margin: 0 0 8px 0; }
.lesson-skills { color: #A8B8CC; font-size: 16px; margin: 0 0 12px 0; }
.skill-tag { display: inline-block; background-color: #1E3A5F; color: #C8942E; border: 1px solid #C8942E; border-radius: 20px; padding: 3px 12px; font-size: 14px; margin: 3px 3px 3px 0; }
.offline-banner { background-color: #2A1A0A; border: 1px solid #E8733A; border-radius: 8px; padding: 10px 16px; color: #E8B84B; font-size: 15px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# ── Offline FAQ bank ──────────────────────────────────────────────────────────
OFFLINE_FAQ = {
    # Lesson 1
    "what is ai": "AI stands for Artificial Intelligence. It's a computer program that can read your question and write back a helpful answer — in plain English, not code. It's not magic, not alive, and not always right. Think of it like a very well-read assistant who has read millions of books and articles. It predicts what a helpful answer looks like based on everything it learned.",
    "what does ai do": "AI reads what you type and predicts a helpful response — one word at a time. It learned from billions of examples of human writing. It does not look things up like Google. It generates an answer. That's why you always verify important information — health, legal, financial — with a real professional.",
    "is ai safe": "AI is safe to use for questions and conversations. The rule is simple: never type your Social Security number, bank account numbers, or passwords into any AI. Everything else — questions about health, recipes, family letters, scam alerts — is fine to ask.",
    "difference between ai and google": "Google finds pages that already exist. AI writes a new answer just for your question. Google gives you links. AI gives you a conversation. AI is better for questions like 'help me write a letter' or 'explain this in simple terms.' Google is better for finding a specific website or phone number.",
    "can ai make mistakes": "Yes — AI can be wrong, especially about specific facts, recent news, or medical details. It generates answers based on patterns, not verified truth. Always double-check anything important with your doctor, a government website, or a trusted person.",

    # Lesson 2
    "how do i use chatgpt": "Go to chat.openai.com on your phone or computer. You can use it without creating an account — just click 'Try ChatGPT.' Type your question in the box at the bottom, just like sending a text message. Press Enter or tap the arrow button. ChatGPT will write back. If you don't like the answer, just ask again differently.",
    "how do i ask a good question": "Be specific. Instead of typing 'health' — type 'What questions should I ask my doctor before a knee replacement?' The more detail you give, the better the answer. If the answer is too long, type: 'Can you say that in two sentences?' AI adjusts to what you ask.",
    "what if i dont like the answer": "Just ask again. You can say: 'Can you make that simpler?' or 'Give me a shorter version' or 'Explain it like I'm new to this.' AI is a conversation — you stay in charge. You never have to start over. Just keep talking.",
    "chatgpt vs claude": "Both are AI assistants and both are free to start. ChatGPT is made by OpenAI. Claude is made by Anthropic. Barb is powered by Claude. They work the same way — you type a question, they write back. Try both and use whichever you like.",

    # Lesson 3 — Scam prevention
    "how do i spot a fake": "Check four things: 1) The sender — does the email domain look right? Would Amazon really write from 'email-secure-alert.com'? 2) The greeting — 'Dear Customer' from your bank is a warning sign. 3) The ask — a link, a download, a QR code, a code they want you to read to them. 4) Did you start this? If they contacted you first, treat it as suspicious.",
    "what are the pressure tactics": "Scammers use four levers: HURRY (you have 20 minutes, act now), FEAR (you'll be arrested, your account is compromised), SECRECY (don't tell your family), and AUTHORITY (a badge number, a case number, a logo). If you feel any of these — stop. Hang up. Call back on a number you already had.",
    "what is two factor authentication": "Two-factor authentication — also called 2FA — adds a second lock to your account. After your password, the site sends a code to your phone. You type that code in. Even if someone steals your password, they can't get in without that code. Turn it on for email first, then your bank.",
    "how do i set up two factor": "Go to your email settings. Look for Security or Privacy. Find 'Two-factor authentication,' '2-step verification,' or 'Multi-factor authentication' — the words change but the idea is the same. Follow the steps. It usually takes about 5 minutes. Turn it on for email first — email is the skeleton key to everything else.",
    "what is a passphrase": "A passphrase is a string of random words used as a password — like 'maple-porch-radio-Thursday.' It's longer than a normal password, which makes it much harder to crack. It's also easier to remember. The government's own security experts (NIST) now recommend passphrases over short complicated passwords.",
    "never move money to protect it": "This is the most important rule: no real bank, government agency, or official ever asks you to move your money to protect it. Not to a gift card. Not to a wire transfer. Not to a Bitcoin ATM. Not to a courier at your door. If someone says your money is in danger and you need to move it — that IS the scam.",
    "what if i already sent money": "Stop sending immediately. Then: 1) Call your bank — use the number on the back of your card. Say the words 'gift card,' 'wire transfer,' or 'crypto ATM' so they know what happened. 2) Change your email password and turn on two-factor authentication. 3) Report at reportfraud.ftc.gov and ic3.gov. 4) Tell one trusted person. Speed matters — the FTC works with FBI recovery teams.",
    "what is a family code word": "A family code word is a secret word or short phrase only your family knows. If someone calls claiming to be your grandchild or family member in trouble — ask for the code word. If they can't give it, hang up and call your family member directly on the number in your phone. Pick a word you'd never post on Facebook.",
    "gift cards": "No real government agency, bank, or emergency ever requires payment in gift cards — not Walmart, not Amazon, not Google Play, not iTunes. Anyone who asks for a gift card number as payment is a scammer. Full stop.",
    "what is caller id spoofing": "Scammers can fake the number that shows on your caller ID. A call can appear to come from 'Austin Police' or 'IRS' or your own bank — and it's fake. Caller ID is a costume. If you didn't initiate the call, hang up and call back on the real number.",
    "how do i report a scam": "Report at two places: reportfraud.ftc.gov (Federal Trade Commission) and ic3.gov (FBI Internet Crime Complaint Center). If your identity was stolen, go to identitytheft.gov. Reporting helps protect others — the FTC uses reports to track patterns and shut down scam operations.",

    # General
    "how do i sign up": "Visit 50plustechbridge.com/start-free-lessons to access all three free lessons. Classes are also held in person at Austin Public Library branches and AARP senior centers — no cost, no account required.",
    "where are classes": "50+TechBridge classes are held at Austin Public Library branches, AARP senior centers, and Foundation Communities locations. All classes are free. Visit 50plustechbridge.com to see the schedule.",
    "who is barb": "Barb is an AI assistant built specifically for the 50+TechBridge lesson program. She's powered by Claude — the same AI technology used in this class. She knows the content of all three lessons and can answer your questions in plain English, any time.",
}

def offline_answer(question: str) -> str:
    q = question.lower().strip()
    # direct keyword match
    for key, answer in OFFLINE_FAQ.items():
        if key in q:
            return answer
    # word overlap fallback
    best_key, best_score = None, 0
    q_words = set(q.split())
    for key in OFFLINE_FAQ:
        k_words = set(key.split())
        score = len(q_words & k_words)
        if score > best_score:
            best_score, best_key = score, key
    if best_key and best_score >= 1:
        return OFFLINE_FAQ[best_key]
    return ("I'm working in offline mode right now and don't have a stored answer for that specific question. "
            "For anything about the lessons — spotting fakes, passwords, two-factor authentication, or using ChatGPT — "
            "ask your instructor. When internet is available, I'll be able to answer any question you have.")

# ── Lesson data ───────────────────────────────────────────────────────────────
LESSONS = [
    {
        "number": 1,
        "title": "Welcome to AI",
        "subtitle": "What AI is, what it isn't, and your first real question",
        "skills": ["What AI actually is", "How to ask a good question", "Staying in charge of the answer"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": None,
    },
    {
        "number": 2,
        "title": "Talk to AI",
        "subtitle": "Have a real conversation with ChatGPT or Claude",
        "skills": ["Opening ChatGPT on your phone", "Asking your first question", "Getting better answers"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": None,
    },
    {
        "number": 3,
        "title": "Don't Get Scammed",
        "subtitle": "3 skills that keep scammers away from your money",
        "skills": ["Spot a Fake", "Name the Pressure", "Passwords & the Second Lock"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": "https://youtu.be/YsSXhxo_fus",
    },
]

# ── System prompt ─────────────────────────────────────────────────────────────
LESSON_SYSTEM_PROMPT = """You are Barb, a warm, patient AI guide for adults over 50 learning through 50+TechBridge's free lesson program.

You know all three lessons:

LESSON 1 — Welcome to AI: AI predicts helpful responses from text patterns — not magic, not alive, not always right. Students learn to ask clear prompts and verify answers before acting.

LESSON 2 — Talk to AI: Open ChatGPT or Claude on phone/computer. Type a clear prompt. Ask follow-ups. AI is a conversation, not a search engine.

LESSON 3 — Don't Get Scammed:
1. SPOT A FAKE: Check sender domain, greeting, ask, and whether you started it. Hang up, look up real number, call back. AI fixed spelling — no typos is no longer a safety test.
2. NAME THE PRESSURE: Hurry, Fear, Secrecy, Authority. Never move money to protect it. Danger payments: gift cards, wire transfers, crypto ATMs, couriers, remote access. Use a family code word for AI voice cloning.
3. PASSWORDS & SECOND LOCK: 15+ character passphrase. Unique email password. 2FA on email then bank. Never read a code to anyone. Report at reportfraud.ftc.gov and ic3.gov.

Rules: simple language, no jargon, talk like a knowledgeable friend, 3-5 short paragraphs max, be encouraging, always verify important info."""

LESSON_SYSTEM_PROMPT_ES = """Eres Barb, una guía de IA cálida y paciente para adultos mayores de 50 años que aprenden con el programa de lecciones gratuitas de 50+TechBridge.

Conoces las tres lecciones y respondes en español simple y claro. Nunca uses jerga técnica. Habla como una amiga que sabe de tecnología.

Reglas: lenguaje simple, sin tecnicismos, máximo 3-5 párrafos cortos, siempre alentador."""

# ── Session state ─────────────────────────────────────────────────────────────
defaults = {
    "messages": [],
    "questions_asked": 0,
    "helpful_count": 0,
    "lessons_completed": set(),
    "instructor_mode": False,
    "projector_mode": False,
    "spanish_mode": False,
    "last_reply": "",
    "online": True,
    "email_captured": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# Check connectivity once per session load
if "connectivity_checked" not in st.session_state:
    st.session_state.online = check_internet()
    st.session_state.connectivity_checked = True

# ── Projector CSS ─────────────────────────────────────────────────────────────
if st.session_state.projector_mode:
    st.markdown("""
    <style>
    html, body, [class*="css"], .stApp, p, li, label, span, div { font-size: 24px !important; }
    .stChatMessage, [data-testid="stChatMessageContent"] { font-size: 24px !important; }
    h1 { font-size: 3.5rem !important; }
    h2 { font-size: 2rem !important; }
    h3 { font-size: 1.6rem !important; }
    .stButton > button { font-size: 22px !important; padding: 16px 28px !important; }
    .stChatInput textarea { font-size: 22px !important; }
    </style>
    """, unsafe_allow_html=True)

# ── Daily tips ────────────────────────────────────────────────────────────────
daily_tips = [
    "A passphrase like 'maple-porch-radio-Thursday' is stronger AND easier to remember than a short jumbled password.",
    "The real IRS, Social Security, and FTC will never call you demanding gift cards or asking you to move money to protect it.",
    "AI is a conversation, not a search engine. If you don't like the answer, ask again differently.",
    "Turn on two-factor authentication on your email this week. It's the single best thing you can do for your security.",
    "Pick a family code word. Share it with the people you'd send money to. If they don't know it — hang up.",
    "Hang up. Look up the real number. Call back. That's the whole rule.",
    "You can ask Barb the same question twice. She won't judge you.",
]
today_tip = daily_tips[datetime.now().timetuple().tm_yday % len(daily_tips)]

# ── Pioneer levels ────────────────────────────────────────────────────────────
def get_pioneer_level(q):
    if q >= 50: return "Trailblazer", "You're leading the way!"
    if q >= 25: return "Pioneer", "You're exploring with confidence!"
    if q >= 10: return "Explorer", "You're getting comfortable with AI!"
    if q >= 1:  return "Beginner", "You've taken your first step!"
    return "New", "Ask your first question to get started!"

# ── Categories ────────────────────────────────────────────────────────────────
categories = {
    "Lesson Questions": [
        "What is AI in plain English?",
        "What are the 4 pressure tactics scammers use?",
        "How do I set up two-factor authentication on my email?",
        "What should I do if I already sent money to a scammer?",
        "What is a passphrase and why is it better than a password?",
        "What is a family code word?",
    ],
    "Health & Medications": [
        "How can AI help me remember my medications?",
        "Can AI help me prepare for a doctor's appointment?",
    ],
    "Money & Bills": [
        "How do I spot an online scam?",
        "Can AI help me manage my bills and budget?",
    ],
    "Staying Connected": [
        "What's the easiest way to video call my family?",
        "Can AI help me write letters or emails?",
    ],
    "Home & Safety": [
        "What AI tools can help me stay safe living alone?",
        "How do smart home devices work?",
    ],
}
CATEGORY_ICONS = {"Lesson Questions": "📚", "Health & Medications": "💊", "Money & Bills": "💰", "Staying Connected": "📱", "Home & Safety": "🏠"}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("logo.png", width=160)
    except Exception:
        pass

    lang = "ES" if st.session_state.spanish_mode else "EN"
    st.markdown(f"""
    <div style="margin-top:4px; margin-bottom:2px;">
        <span style="font-family:'Playfair Display',serif; font-size:26px; font-weight:800; color:#C8942E;">Ask Barb</span>
        <span style="font-size:12px; color:#A8B8CC; margin-left:6px;">{lang}</span><br>
        <span style="font-size:14px; color:#A8B8CC;">50+TechBridge Free Lessons</span>
    </div>
    """, unsafe_allow_html=True)

    # Connectivity indicator
    status_color = "#109F35" if st.session_state.online else "#E8733A"
    status_text  = "Online — Live AI" if st.session_state.online else "Offline — Pre-set Answers"
    st.markdown(f'<div style="font-size:13px; color:{status_color}; margin:6px 0;">● {status_text}</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:10px 0;'>", unsafe_allow_html=True)

    nav_options = ["Home", "Free Lessons", "Ask Barb", "My Progress", "Resources"]
    if st.session_state.instructor_mode:
        nav_options.append("Instructor Guide")
    page = st.radio("Navigate", nav_options, label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1E3A5F; margin:10px 0;'>", unsafe_allow_html=True)

    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-level-badge">
        <div style="font-size:13px; color:#A8B8CC; margin-bottom:4px;">Lessons Completed</div>
        <strong style="font-size:26px;">{completed} / 3</strong><br>
        <div style="font-size:14px; color:#A8B8CC;">{"All done! You're a Pioneer." if completed == 3 else "Keep going!"}</div>
    </div>
    """, unsafe_allow_html=True)

    level, _ = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f'<div style="text-align:center; margin:8px 0; font-size:15px; color:#A8B8CC;">Pioneer Level: <span style="color:#C8942E; font-weight:700;">{level}</span></div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:10px 0;'>", unsafe_allow_html=True)

    # Instructor controls
    st.markdown("<div style='font-size:12px; color:#A8B8CC; margin-bottom:4px;'>INSTRUCTOR OPTIONS</div>", unsafe_allow_html=True)

    if st.toggle("Instructor Mode", value=st.session_state.instructor_mode, key="toggle_instructor"):
        st.session_state.instructor_mode = True
    else:
        st.session_state.instructor_mode = False

    if st.session_state.instructor_mode:
        if st.toggle("Projector Mode", value=st.session_state.projector_mode, key="toggle_projector"):
            st.session_state.projector_mode = True
        else:
            st.session_state.projector_mode = False
        if st.button("Reset for New Class", key="reset_class"):
            st.session_state.messages = []
            st.session_state.questions_asked = 0
            st.session_state.helpful_count = 0
            st.session_state.lessons_completed = set()
            st.session_state.email_captured = False
            st.session_state.last_reply = ""
            st.toast("Reset complete — ready for new class.")
            st.rerun()

    st.markdown("<hr style='border-color:#1E3A5F; margin:10px 0;'>", unsafe_allow_html=True)

    # Spanish toggle
    if st.toggle("Español", value=st.session_state.spanish_mode, key="toggle_spanish"):
        st.session_state.spanish_mode = True
    else:
        st.session_state.spanish_mode = False

    st.markdown("<hr style='border-color:#1E3A5F; margin:10px 0;'>", unsafe_allow_html=True)

    if st.button("Clear Chat", key="clear_chat"):
        st.session_state.messages = []
        st.rerun()

    # Recheck internet
    if st.button("Check Connection", key="recheck"):
        st.session_state.online = check_internet()
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 No internet — Barb is running on pre-set answers. Live AI available when connection is restored.</div>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:3rem; color:#C8942E; margin-bottom:4px;">Hi, I\'m Barb.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="lmt-hero-sub">Your AI guide for the 50+TechBridge free lesson program.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
    st.markdown(f'<div class="lmt-tip-card"><strong style="color:#C8942E;">Today\'s tip:</strong> {today_tip}</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:\'Playfair Display\',serif; font-size:1.3rem; color:#C8942E;">Your Free Lessons</h2>', unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in lesson["skills"]])
        st.markdown(f"""
        <div class="lesson-card {'completed' if done else ''}">
            <span class="lesson-badge {'done' if done else ''}">{'✓ Completed' if done else f'Lesson {lesson["number"]}'}</span>
            <div class="lesson-title">{lesson['title']}</div>
            <div class="lesson-skills">{lesson['subtitle']}</div>
            <div>{skills_html}</div>
        </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go to Free Lessons", use_container_width=True):
            st.rerun()
    with col2:
        st.markdown('<div class="outline-btn">', unsafe_allow_html=True)
        if st.button("Ask Barb a Question", use_container_width=True):
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FREE LESSONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Free Lessons":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline — lesson links will open when internet is restored. Ask Barb questions below — she has pre-set answers.</div>', unsafe_allow_html=True)

    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Free Lessons</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC; font-size:18px;">Three lessons. Watch, learn, ask Barb anything along the way.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    # ChatGPT launch
    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E; margin-bottom:20px;">
        <div style="font-family:'Playfair Display',serif; font-size:1.2rem; color:#C8942E; margin-bottom:6px;">Ready to try AI yourself?</div>
        <div style="color:#C4CDD9; font-size:17px; margin-bottom:14px;">Open ChatGPT — free, no account needed to start. Practice what you learned in Lesson 2.</div>
        <a href="https://chat.openai.com" target="_blank"
           style="display:inline-block; background:#C8942E; color:#0E1C2F; font-weight:700; font-size:18px;
                  padding:12px 28px; border-radius:8px; text-decoration:none;">
            Open ChatGPT →
        </a>
        <span style="color:#A8B8CC; font-size:14px; margin-left:14px;">Opens in a new tab</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

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
            mark_label = "↩ Mark Undone" if done else "✓ Mark Done"
            if st.button(mark_label, key=f"complete_{lesson['number']}", use_container_width=True):
                if done:
                    st.session_state.lessons_completed.discard(lesson["number"])
                else:
                    st.session_state.lessons_completed.add(lesson["number"])
                st.rerun()

        with st.expander(f"Ask Barb about Lesson {lesson['number']}"):
            followups = {
                1: ["What is AI in plain English?", "Can AI make mistakes?", "What's the difference between AI and Google?"],
                2: ["How do I open ChatGPT on my phone?", "What's a good first question to ask AI?", "What if I don't like the answer AI gives me?"],
                3: ["What are the 4 pressure tactics scammers use?", "How do I set up two-factor authentication?", "What do I do if I already sent money to a scammer?", "What is a family code word?"],
            }
            for q in followups[lesson["number"]]:
                st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
                if st.button(q, key=f"lq_{lesson['number']}_{q[:15]}", use_container_width=True):
                    st.session_state["user_input"] = q
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    # Completion — Agentic50 badge + email capture
    if len(st.session_state.lessons_completed) == 3:
        col_logo, col_text = st.columns([1, 2])
        with col_logo:
            try:
                st.image("agentic50-logo.png", width=160)
            except Exception:
                st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:2rem; color:#C8942E; text-align:center;">Agentic50</div>', unsafe_allow_html=True)
        with col_text:
            st.markdown("""
            <div style="padding:12px 0;">
                <div style="font-family:'Playfair Display',serif; font-size:1.4rem; color:#C8942E; margin-bottom:6px;">You're a Digital Pioneer.</div>
                <div style="color:#C4CDD9; font-size:17px;">All 3 lessons complete. Follow Agentic50 — weekly AI news written for people like you.</div>
            </div>""", unsafe_allow_html=True)

        if not st.session_state.email_captured:
            st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#C8942E; margin-bottom:8px;">Get weekly AI tips in your inbox — free.</div>', unsafe_allow_html=True)
            email_input = st.text_input("Your email address:", placeholder="yourname@email.com", key="email_signup")
            if st.button("Sign Me Up →", key="mailerlite_signup"):
                if "@" in email_input and "." in email_input:
                    # MailerLite API call (replace YOUR_API_KEY and GROUP_ID)
                    try:
                        import urllib.request, json as _json
                        ml_key = os.environ.get("MAILERLITE_API_KEY", "")
                        ml_group = os.environ.get("MAILERLITE_GROUP_ID", "")
                        if ml_key and ml_group:
                            payload = _json.dumps({"email": email_input, "groups": [ml_group]}).encode()
                            req = urllib.request.Request(
                                "https://connect.mailerlite.com/api/subscribers",
                                data=payload,
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {ml_key}"},
                                method="POST"
                            )
                            urllib.request.urlopen(req, timeout=5)
                        st.session_state.email_captured = True
                        st.toast("You're in! Check your inbox for a welcome message.")
                        st.rerun()
                    except Exception:
                        st.session_state.email_captured = True
                        st.toast("Signed up! Welcome to the community.")
                        st.rerun()
                else:
                    st.warning("Please enter a valid email address.")
        else:
            st.markdown('<div class="lmt-orange-msg" style="text-align:center;"><strong>You\'re signed up. See you in your inbox.</strong><br><span style="font-size:15px;">Bring a friend to the next class — it\'s free.</span></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ASK BARB
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Ask Barb":
    if not st.session_state.online:
        st.markdown('<div class="offline-banner">📶 Offline mode — Barb is using pre-set answers for lesson questions.</div>', unsafe_allow_html=True)

    lang_label = "Pregúntale a Barb" if st.session_state.spanish_mode else "Ask Barb"
    lang_sub   = "Sin jerga tecnológica. Solo una conversación clara." if st.session_state.spanish_mode else "No tech jargon. Just plain talk from a knowledgeable friend."

    st.markdown(f'<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">{lang_label}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#A8B8CC; font-size:18px;">{lang_sub}</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    selected_cat = st.selectbox("Choose a topic:", ["All Topics"] + list(categories.keys()))
    examples = [q for cat_qs in categories.values() for q in cat_qs[:1]] if selected_cat == "All Topics" else categories[selected_cat]

    st.markdown("<p style='color:#A8B8CC; font-size:16px; margin:12px 0 8px;'><strong style='color:#C4CDD9;'>Try one of these:</strong></p>", unsafe_allow_html=True)
    for example in examples:
        st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
        if st.button(example, key=f"ex_{example[:30]}", use_container_width=True):
            st.session_state["user_input"] = example
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    if not st.session_state.messages:
        greeting = "Hola! Soy Barb. Puedes preguntarme cualquier cosa sobre las lecciones o la tecnología en general." if st.session_state.spanish_mode else "Hi there! I'm Barb, your guide through the 50+TechBridge lessons. Ask me anything — no question is too simple."
        st.markdown(f'<div class="lmt-barb-greeting">{greeting} <strong style="color:#C8942E;">{"¿Qué quieres saber?" if st.session_state.spanish_mode else "What would you like to know?"}</strong></div>', unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    placeholder_text = "Escribe tu pregunta aquí..." if st.session_state.spanish_mode else "Type your question here..."
    prompt = st.chat_input(placeholder_text)

    if "user_input" in st.session_state:
        prompt = st.session_state.pop("user_input")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.questions_asked += 1

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if not st.session_state.online:
                # Offline mode — use pre-set answers
                reply = offline_answer(prompt)
                st.markdown(reply)
            else:
                # Online mode — live Claude API
                api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
                client = anthropic.Anthropic(api_key=api_key)
                sys_prompt = LESSON_SYSTEM_PROMPT_ES if st.session_state.spanish_mode else LESSON_SYSTEM_PROMPT
                with client.messages.stream(
                    model="claude-sonnet-4-6",
                    max_tokens=1024,
                    system=sys_prompt,
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                ) as stream:
                    reply = st.write_stream(stream.text_stream)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.session_state.last_reply = reply

        # Text-to-speech button
        tts_label = "🔊 Leer en voz alta" if st.session_state.spanish_mode else "🔊 Read aloud"
        st.markdown(f"""
        <button onclick="window.speechSynthesis.cancel(); var u=new SpeechSynthesisUtterance({json.dumps(reply)});
        u.lang='{'es-US' if st.session_state.spanish_mode else 'en-US'}'; u.rate=0.9;
        window.speechSynthesis.speak(u);"
        style="background:#1E3A5F; color:#C8942E; border:1.5px solid #C8942E; border-radius:20px;
               padding:8px 20px; font-size:16px; cursor:pointer; margin:8px 0; font-family:'DM Sans',sans-serif;">
        {tts_label}</button>
        <button onclick="window.speechSynthesis.cancel();"
        style="background:transparent; color:#A8B8CC; border:1px solid #A8B8CC; border-radius:20px;
               padding:8px 16px; font-size:14px; cursor:pointer; margin-left:8px; font-family:'DM Sans',sans-serif;">
        Stop</button>
        """, unsafe_allow_html=True)

        # Print transcript button
        printable = st.session_state.messages[-6:] if len(st.session_state.messages) > 6 else st.session_state.messages
        transcript = "\n\n".join([f"{'You' if m['role']=='user' else 'Barb'}: {m['content']}" for m in printable])
        st.download_button(
            label="📄 Save this conversation",
            data=transcript,
            file_name=f"barb-conversation-{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain",
            key=f"dl_{len(st.session_state.messages)}"
        )

        # Feedback
        col1, col2, _ = st.columns([1, 1, 4])
        with col1:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👍 Helpful", key=f"helpful_{len(st.session_state.messages)}"):
                st.session_state.helpful_count += 1
                st.toast("Thanks! Glad that helped.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button("👎 Not helpful", key=f"nothelpful_{len(st.session_state.messages)}"):
                st.toast("Thanks — I'll try to do better!")
            st.markdown('</div>', unsafe_allow_html=True)

        # Instructor explainer
        if st.session_state.instructor_mode:
            st.markdown("""
            <div style="background:#0E2A1A; border:1px solid #109F35; border-radius:10px; padding:18px 22px; margin-top:16px;">
                <div style="font-size:13px; color:#109F35; font-weight:700; letter-spacing:1px; margin-bottom:8px;">INSTRUCTOR — WHAT JUST HAPPENED</div>
                <div style="color:#C4CDD9; font-size:17px; line-height:1.6;">
                    <strong style="color:#C8942E;">1. You typed a prompt</strong> — the clearer the question, the better the answer.<br><br>
                    <strong style="color:#C8942E;">2. Barb read the full conversation</strong> — AI keeps context, like talking with a friend.<br><br>
                    <strong style="color:#C8942E;">3. Barb predicted the best response</strong> — one word at a time, based on billions of training examples.<br><br>
                    <strong style="color:#C8942E;">4. Barb followed her instructions</strong> — warm, plain-spoken, focused on 50+ adults.<br><br>
                    <em style="color:#A8B8CC;">Remind students: Barb didn't look this up. She generated it. Always verify important information.</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MY PROGRESS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "My Progress":
    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">My Progress</h1>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-progress-card">
        <div style="font-size:14px; color:#A8B8CC; margin-bottom:8px; text-transform:uppercase; letter-spacing:1px;">Lessons Completed</div>
        <h2>{completed} of 3</h2>
        <p>{"All three done — you're a Digital Pioneer!" if completed == 3 else "Keep going — every lesson builds your confidence."}</p>
    </div>""", unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
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
        <div style="font-size:14px; color:#A8B8CC; margin-bottom:8px; text-transform:uppercase; letter-spacing:1px;">Your Pioneer Level</div>
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
            <li>In-person: Austin Public Library branches + AARP senior centers</li>
        </ul>
    </div>
    <div class="lmt-section-card">
        <h3>Report a Scam</h3>
        <ul>
            <li><a href="https://reportfraud.ftc.gov" target="_blank">reportfraud.ftc.gov</a> — Federal Trade Commission</li>
            <li><a href="https://www.ic3.gov" target="_blank">ic3.gov</a> — FBI Internet Crime Center</li>
            <li><a href="https://www.identitytheft.gov" target="_blank">identitytheft.gov</a> — Identity theft steps</li>
        </ul>
    </div>
    <div class="lmt-section-card">
        <h3>AI Safety Reminders</h3>
        <ul>
            <li>Never type your Social Security number, bank info, or passwords into any AI</li>
            <li>AI can be wrong — verify anything important with a real professional</li>
            <li>If it feels like a scam — hang up, look up the real number, call back</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# INSTRUCTOR GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Instructor Guide":
    st.markdown('<h1 style="font-family:\'Playfair Display\',serif; font-size:2.4rem; color:#C8942E;">Instructor Guide</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A8B8CC; font-size:18px;">What to say, what to show, what it means.</p>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E;">
        <h3>What to Tell the Class</h3>
        <p style="font-size:17px; line-height:1.7;">
        <em>"Barb is an AI assistant built for this program. She knows all three lessons. Ask her anything you're
        confused about — she'll answer in plain English, no jargon."</em></p>
        <p style="font-size:17px; line-height:1.7;">
        <em>"But here's what's important: Barb doesn't look things up. She generates her answer word by word.
        She can be wrong. For anything medical, legal, or financial — always verify."</em></p>
    </div>
    """, unsafe_allow_html=True)

    demo_flows = [
        {
            "lesson": "Lesson 1 — Welcome to AI",
            "setup": "Use this before students have ever tried AI.",
            "steps": [
                ("Say this", "Watch what happens when I type a question. I'm going to ask Barb something simple."),
                ("Type this", "What is AI in plain English?"),
                ("Point out", "Notice — short paragraphs, no jargon. That's by design."),
                ("Say this", "Now I'll ask a follow-up. AI remembers the conversation."),
                ("Type this", "Can AI make mistakes?"),
                ("Debrief", "See how she kept the context? That's the difference between AI and a search engine."),
            ],
            "talking_point": "AI is a conversation, not a search. The more specific your question, the better the answer.",
            "demo_q": "What is AI in plain English?",
        },
        {
            "lesson": "Lesson 2 — Talk to AI",
            "setup": "Use after students watch Lesson 2.",
            "steps": [
                ("Say this", "Let's practice asking a good question together. What's something you deal with every day?"),
                ("Take a suggestion", "Pick one from the class — doctor appointment, medication reminder, family email."),
                ("Type it", "Type their suggestion as a question — like talking to a person, not a Google search."),
                ("Say this", "If you don't like the answer, don't start over. Just say: Can you say that more simply?"),
                ("Type this", "Can you say that in two sentences?"),
                ("Debrief", "That's a follow-up prompt. You stay in charge of the conversation."),
            ],
            "talking_point": "You are always in charge. If the answer doesn't work, ask again differently.",
            "demo_q": "Can you help me write a message to my doctor about my next appointment?",
        },
        {
            "lesson": "Lesson 3 — Don't Get Scammed",
            "setup": "Use to reinforce the three skills after the lesson video.",
            "steps": [
                ("Say this", "Let's test Barb on what we just learned. I'm going to ask about the pressure tactics."),
                ("Type this", "What are the four pressure tactics scammers use?"),
                ("Point out", "Hurry, Fear, Secrecy, Authority — same as the lesson. Barb knows the material."),
                ("Say this", "Now let's ask what to do if it already happened."),
                ("Type this", "What should I do if I already sent money to a scammer?"),
                ("Debrief", "Notice she says 'tell one trusted person' — shame keeps people from reporting. We name it here."),
            ],
            "talking_point": "No question is too simple. Barb is a practice partner, not a test.",
            "demo_q": "What are the four pressure tactics scammers use?",
        },
    ]

    for flow in demo_flows:
        with st.expander(f"📋 {flow['lesson']}", expanded=False):
            st.markdown(f'<div style="background:#1E3A5F; border-radius:8px; padding:12px 16px; margin-bottom:14px; font-size:16px;"><strong style="color:#C8942E;">Setup:</strong> {flow["setup"]}</div>', unsafe_allow_html=True)
            for action, detail in flow["steps"]:
                color = "#C8942E" if action in ("Type this", "Say this") else "#109F35" if action == "Debrief" else "#A8B8CC"
                st.markdown(f'<div style="display:flex; align-items:flex-start; padding:10px 0; border-bottom:1px solid #1E3A5F;"><div style="min-width:110px; font-size:13px; font-weight:700; color:{color}; padding-top:2px;">{action.upper()}</div><div style="font-size:17px; color:#C4CDD9; line-height:1.5;">{detail}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div style="background:#0E2A1A; border-left:4px solid #109F35; border-radius:6px; padding:12px 16px; margin-top:14px;"><strong style="color:#109F35; font-size:13px;">KEY TALKING POINT</strong><br><span style="color:#C4CDD9; font-size:17px;">{flow["talking_point"]}</span></div>', unsafe_allow_html=True)
            st.markdown('<div style="margin-top:14px; font-size:14px; color:#A8B8CC;">Run this demo question live:</div>', unsafe_allow_html=True)
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button(f"▶ Demo: \"{flow['demo_q']}\"", key=f"demo_{flow['lesson'][:10]}", use_container_width=True):
                st.session_state["user_input"] = flow["demo_q"]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="lmt-section-card">
        <h3>Quick Reference — What to Say When Students Ask</h3>
        <table class="lmt-table">
            <thead><tr><th>If a student asks...</th><th>Say this</th></tr></thead>
            <tbody>
                <tr><td>"Is Barb always right?"</td><td>"No — AI generates answers. You verify the important ones."</td></tr>
                <tr><td>"How does it know what I'm asking?"</td><td>"It reads your whole message and predicts the most helpful response."</td></tr>
                <tr><td>"Is this safe to use?"</td><td>"Yes — just don't type passwords or Social Security numbers into any AI."</td></tr>
                <tr><td>"What if I can't spell?"</td><td>"Doesn't matter. AI understands what you mean, even with typos."</td></tr>
                <tr><td>"Can I use this at home?"</td><td>"Yes — it's free. So is ChatGPT at chat.openai.com."</td></tr>
                <tr><td>"What if there's no internet?"</td><td>"Barb has pre-set answers for all lesson questions — tap the offline banner at the top."</td></tr>
            </tbody>
        </table>
    </div>
    <div class="lmt-section-card" style="border-color:#C8942E; margin-top:14px;">
        <h3>Before Class Checklist</h3>
        <ul>
            <li>Turn on <strong style="color:#C8942E;">Instructor Mode</strong> in the sidebar</li>
            <li>Turn on <strong style="color:#C8942E;">Projector Mode</strong> for large screen display</li>
            <li>Click <strong style="color:#C8942E;">Reset for New Class</strong> to clear previous session data</li>
            <li>Check the connection indicator — green = live AI, orange = offline pre-set answers</li>
            <li>Run one demo question yourself before students arrive</li>
            <li>If offline: all lesson questions still work — Barb has pre-written answers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
