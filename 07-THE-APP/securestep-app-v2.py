import streamlit as st
import anthropic
import os
from datetime import datetime

# Page setup
st.set_page_config(page_title="Ask Barb — 50+TechBridge", page_icon="🌟", layout="centered")

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700;800&display=swap');

html, body, [class*="css"], .stApp {
    background-color: #0E1C2F !important;
    color: #C4CDD9 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 18px !important;
}
.block-container { background-color: #0E1C2F !important; padding-top: 2rem !important; }
section[data-testid="stSidebar"] { background-color: #162640 !important; }
section[data-testid="stSidebar"] > div { background-color: #162640 !important; }

h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    font-family: 'Playfair Display', serif !important;
    color: #C8942E !important;
}
p, li, label, span, div { font-family: 'DM Sans', sans-serif !important; color: #C4CDD9 !important; }

.stButton > button {
    background-color: #C8942E !important; color: #0E1C2F !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 700 !important;
    font-size: 18px !important; border-radius: 8px !important; border: none !important;
    padding: 12px 24px !important; min-height: 48px !important; width: 100% !important;
    cursor: pointer !important; transition: background-color 0.2s ease !important;
}
.stButton > button:hover { background-color: #E8B84B !important; color: #0E1C2F !important; }

.pill-btn > button {
    background-color: #1E3A5F !important; color: #C8942E !important;
    border: 1.5px solid #C8942E !important; border-radius: 24px !important;
    font-weight: 600 !important; padding: 10px 20px !important;
}
.pill-btn > button:hover { background-color: #C8942E !important; color: #0E1C2F !important; }

.outline-btn > button {
    background-color: transparent !important; color: #C8942E !important;
    border: 2px solid #C8942E !important; border-radius: 8px !important;
}
.outline-btn > button:hover { background-color: #C8942E !important; color: #0E1C2F !important; }

.stChatMessage { font-size: 18px !important; border-radius: 10px !important; padding: 12px !important; margin-bottom: 10px !important; }
[data-testid="stChatMessageContent"] { font-size: 18px !important; color: #C4CDD9 !important; }
[data-testid="stChatMessage"][data-role="user"] { background-color: #1E3A5F !important; border-left: 4px solid #C8942E !important; }
[data-testid="stChatMessage"][data-role="assistant"] { background-color: #162640 !important; border-left: 4px solid #109F35 !important; }

.stChatInput textarea, .stChatInput input {
    background-color: #162640 !important; color: #C4CDD9 !important;
    border: 1.5px solid #A8B8CC !important; border-radius: 8px !important;
    font-size: 18px !important; font-family: 'DM Sans', sans-serif !important;
}
.stChatInput textarea:focus, .stChatInput input:focus {
    border-color: #C8942E !important; outline: none !important;
    box-shadow: 0 0 0 2px rgba(200, 148, 46, 0.3) !important;
}
.stSelectbox > div > div {
    background-color: #162640 !important; color: #C4CDD9 !important;
    border: 1.5px solid #A8B8CC !important; border-radius: 8px !important; font-size: 18px !important;
}
.stRadio > div { background-color: transparent !important; }
.stRadio label { color: #C4CDD9 !important; font-size: 17px !important; }

[data-testid="stMetric"] { background-color: #162640 !important; border-radius: 10px !important; padding: 16px !important; border: 1px solid #1E3A5F !important; }
[data-testid="stMetricValue"] { color: #C8942E !important; font-family: 'Playfair Display', serif !important; font-size: 2rem !important; }
[data-testid="stMetricLabel"] { color: #A8B8CC !important; font-size: 16px !important; }

hr { border-color: #1E3A5F !important; }

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 { color: #C8942E !important; }
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label { color: #C4CDD9 !important; }

.lmt-tip-card { background-color: #162640; border-left: 5px solid #C8942E; border-radius: 10px; padding: 20px 24px; margin: 12px 0; font-size: 18px; color: #C4CDD9; font-family: 'DM Sans', sans-serif; }
.lmt-progress-card { background-color: #162640; border: 2px solid #C8942E; border-radius: 12px; padding: 24px; margin: 12px 0; text-align: center; }
.lmt-progress-card h2 { font-family: 'Playfair Display', serif; color: #C8942E; margin: 0 0 8px 0; font-size: 2rem; }
.lmt-progress-card p { color: #A8B8CC; margin: 0; font-size: 18px; }
.lmt-level-badge { background-color: #1E3A5F; border: 1.5px solid #C8942E; border-radius: 10px; padding: 12px 16px; margin: 8px 0; text-align: center; }
.lmt-level-badge strong { color: #C8942E; font-family: 'Playfair Display', serif; }
.lmt-section-card { background-color: #162640; border-radius: 12px; padding: 20px 24px; margin: 12px 0; border: 1px solid #1E3A5F; }
.lmt-section-card h3 { font-family: 'Playfair Display', serif; color: #C8942E; margin-top: 0; }
.lmt-section-card a { color: #C8942E; text-decoration: underline; }
.lmt-section-card a:hover { color: #E8B84B; }
.lmt-section-card ul { padding-left: 20px; }
.lmt-section-card li { color: #C4CDD9; margin-bottom: 8px; }
.lmt-cat-card { background-color: #162640; border-radius: 10px; padding: 18px 20px; margin: 6px 0; border: 1px solid #1E3A5F; }
.lmt-cat-card .cat-title { color: #C8942E; font-weight: 700; font-size: 18px; font-family: 'DM Sans', sans-serif; }
.lmt-cat-card .cat-example { color: #A8B8CC; font-size: 15px; margin-top: 4px; }
.lmt-hero-sub { color: #A8B8CC; font-size: 20px; font-family: 'DM Sans', sans-serif; margin-bottom: 8px; }
.lmt-orange-msg { background-color: rgba(232, 115, 58, 0.15); border-left: 4px solid #E8733A; border-radius: 8px; padding: 16px 20px; color: #E8B84B; font-size: 18px; font-family: 'DM Sans', sans-serif; margin: 12px 0; }
.lmt-barb-greeting { background-color: #162640; border-left: 4px solid #109F35; border-radius: 10px; padding: 20px 24px; margin: 12px 0; font-size: 18px; color: #C4CDD9; font-family: 'DM Sans', sans-serif; }
.lmt-table { width: 100%; border-collapse: collapse; font-family: 'DM Sans', sans-serif; font-size: 17px; }
.lmt-table th { background-color: #1E3A5F; color: #C8942E; padding: 12px 16px; text-align: left; border-bottom: 2px solid #C8942E; }
.lmt-table td { background-color: #162640; color: #C4CDD9; padding: 12px 16px; border-bottom: 1px solid #1E3A5F; }
.lmt-table tr:hover td { background-color: #1E3A5F; }

/* Lesson cards */
.lesson-card { background-color: #162640; border-radius: 14px; padding: 24px; margin: 14px 0; border: 1px solid #1E3A5F; position: relative; }
.lesson-card.completed { border-color: #109F35; }
.lesson-badge { display: inline-block; background-color: #C8942E; color: #0E1C2F; font-weight: 700; font-size: 13px; border-radius: 20px; padding: 4px 14px; margin-bottom: 10px; font-family: 'DM Sans', sans-serif; }
.lesson-badge.done { background-color: #109F35; }
.lesson-title { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #C8942E; margin: 0 0 8px 0; }
.lesson-skills { color: #A8B8CC; font-size: 16px; margin: 0 0 12px 0; }
.skill-tag { display: inline-block; background-color: #1E3A5F; color: #C8942E; border: 1px solid #C8942E; border-radius: 20px; padding: 3px 12px; font-size: 14px; margin: 3px 3px 3px 0; font-family: 'DM Sans', sans-serif; }
</style>
""", unsafe_allow_html=True)

# ── Lesson content (Barb knows all of this) ─────────────────────────────────
LESSONS = [
    {
        "number": 1,
        "title": "Welcome to AI",
        "subtitle": "What AI is, what it isn't, and your first real question",
        "skills": ["What AI actually is", "How to ask a good question", "Staying in charge of the answer"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": None,
        "summary": "Lesson 1 introduces what AI is in plain language. AI is a tool that predicts helpful responses based on patterns in text — it's not magic, not alive, and not always right. Students learn how to ask clear questions (prompts) and stay in charge of the answer by checking it before acting on it.",
    },
    {
        "number": 2,
        "title": "Talk to AI",
        "subtitle": "Have a real conversation with ChatGPT or Claude",
        "skills": ["Opening ChatGPT or Claude on your phone", "Asking your first question", "Getting better answers by being specific"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": None,
        "summary": "Lesson 2 is hands-on. Students open ChatGPT or Claude on their phone or computer and have their first real conversation. Key skills: typing a clear prompt, asking follow-up questions, and knowing when to trust — or double-check — the answer. The main takeaway: AI is a conversation, not a search engine.",
    },
    {
        "number": 3,
        "title": "Don't Get Scammed",
        "subtitle": "3 skills that keep scammers away from your money",
        "skills": ["Spot a Fake", "Name the Pressure", "Passwords & the Second Lock"],
        "url": "https://50plustechbridge.com/start-free-lessons/",
        "youtube": "https://youtu.be/YsSXhxo_fus",
        "summary": """Lesson 3 covers fraud prevention for adults 50+. Three skills:
1. SPOT A FAKE — look at the sender domain, the greeting, the ask, and whether you started the conversation. Hang up, look up the real number, call back.
2. NAME THE PRESSURE — four levers scammers use: Hurry, Fear, Secrecy, Authority. Never move money to protect it. Danger payments: gift cards, wire transfers, crypto ATMs, couriers, remote computer access. AI voice cloning is real — use a family code word.
3. PASSWORDS & THE SECOND LOCK — use a passphrase of 15+ characters. Unique password for email (it's the skeleton key). Two-factor authentication on email and bank. Never read a code to anyone.
If it happened: stop, call the bank, change email password, report at reportfraud.ftc.gov and ic3.gov.""",
    },
]

LESSON_SYSTEM_PROMPT = """You are Barb, a warm, patient AI guide for adults over 50 who are learning about AI and technology through 50+TechBridge's free lesson program.

You know the content of all three free lessons:

LESSON 1 — Welcome to AI
What AI is in plain language. AI predicts helpful responses based on text patterns — it's not magic, not alive, not always right. Students learn to ask clear questions (prompts) and stay in charge of the answer by verifying before acting.

LESSON 2 — Talk to AI
Hands-on: open ChatGPT or Claude on phone or computer. Type a clear prompt. Ask follow-up questions. Know when to trust vs. double-check. AI is a conversation, not a search engine.

LESSON 3 — Don't Get Scammed
Three skills:
1. SPOT A FAKE: Check the sender domain, greeting, ask, and whether you started the conversation. Hang up, look up real number, call back. AI fixed spelling — no typos is no longer a safety test.
2. NAME THE PRESSURE: Four levers — Hurry, Fear, Secrecy, Authority. Never move money to protect it. Danger payments: gift cards, wire transfers, crypto ATMs, couriers, remote computer access. AI voice cloning — use a family code word. 3 in 4 older adults who reported a scam lost NO money — they spotted it.
3. PASSWORDS & THE SECOND LOCK: 15+ character passphrase. Unique password for email. Two-factor authentication on email first, then bank. Never read a code to anyone. Report scams at reportfraud.ftc.gov and ic3.gov.

Your rules:
- Use simple, clear language. No tech jargon.
- Talk like a knowledgeable friend, not a professor.
- Give specific, actionable steps they can try today.
- Be encouraging — many users are trying technology for the first time.
- Keep answers concise — 3-5 short paragraphs max.
- If someone asks about a lesson topic, connect it back to what they learned.
- When someone seems confused or scared, reassure them first, then explain.
- Never share Social Security numbers, bank info, or passwords.
- You represent 50+TechBridge, a free program at Austin Public Library branches and senior centers."""

# ── Session state ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0
if "helpful_count" not in st.session_state:
    st.session_state.helpful_count = 0
if "lessons_completed" not in st.session_state:
    st.session_state.lessons_completed = set()
if "instructor_mode" not in st.session_state:
    st.session_state.instructor_mode = False
if "projector_mode" not in st.session_state:
    st.session_state.projector_mode = False
if "last_reply" not in st.session_state:
    st.session_state.last_reply = ""

# ── Daily tips ───────────────────────────────────────────────────────────────
daily_tips = [
    "You can ask Alexa or Siri to set medication reminders — just say 'Remind me to take my pills at 8am every day.'",
    "AI can help you write emails. Just tell ChatGPT or Claude 'Help me write a friendly email to my doctor about my upcoming appointment.'",
    "Worried about phone scams? AI can't answer your phone, but you can ask it 'What are the most common phone scams targeting adults 50+?' to learn what to watch for.",
    "The real IRS, Social Security, and FTC will never call you demanding gift cards or asking you to move money to protect it.",
    "Want to video call family? FaceTime (iPhone) or Google Meet (any phone) are the easiest options. Ask Barb how to set them up!",
    "A passphrase like 'maple-porch-radio-Thursday' is stronger AND easier to remember than a short jumbled password.",
    "AI is a conversation, not a search engine. If you don't like the answer, ask again differently — or ask a follow-up question.",
]
today_tip = daily_tips[datetime.now().timetuple().tm_yday % len(daily_tips)]

# ── Pioneer levels ───────────────────────────────────────────────────────────
def get_pioneer_level(questions):
    if questions >= 50:
        return "Trailblazer", "You're leading the way!"
    elif questions >= 25:
        return "Pioneer", "You're exploring with confidence!"
    elif questions >= 10:
        return "Explorer", "You're getting comfortable with AI!"
    elif questions >= 1:
        return "Beginner", "You've taken your first step!"
    else:
        return "New", "Ask your first question to get started!"

# ── Categories ───────────────────────────────────────────────────────────────
categories = {
    "Lesson Questions": [
        "What does AI actually do? (Lesson 1)",
        "How do I ask a better question in ChatGPT?",
        "What are the 4 pressure tactics scammers use?",
        "How do I set up two-factor authentication on my email?",
        "What should I do if I already sent money to a scammer?",
        "What is a passphrase and why is it better than a password?",
    ],
    "Health & Medications": [
        "How can AI help me remember my medications?",
        "Can AI help me prepare for a doctor's appointment?",
        "What apps track blood pressure or blood sugar?",
    ],
    "Money & Bills": [
        "How do I spot an online scam?",
        "Can AI help me manage my bills and budget?",
        "Can AI help me compare insurance plans?",
    ],
    "Staying Connected": [
        "What's the easiest way to video call my family?",
        "How can AI help me stay in touch with old friends?",
        "Can AI help me write letters or emails?",
    ],
    "Home & Safety": [
        "What AI tools can help me stay safe living alone?",
        "How do smart home devices work?",
        "Can AI detect if I've fallen?",
    ],
}

CATEGORY_ICONS = {
    "Lesson Questions": "📚",
    "Health & Medications": "💊",
    "Money & Bills": "💰",
    "Staying Connected": "📱",
    "Home & Safety": "🏠",
}

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image("logo.png", width=180)
    except Exception:
        pass

    st.markdown("""
    <div style="margin-top: 4px; margin-bottom: 2px;">
        <span style="font-family:'Playfair Display',serif; font-size:26px; font-weight:800; color:#C8942E;">Ask Barb</span><br>
        <span style="font-family:'DM Sans',sans-serif; font-size:14px; color:#A8B8CC; letter-spacing:0.5px;">50+TechBridge Free Lessons</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    nav_options = ["Home", "Free Lessons", "Ask Barb", "My Progress", "Resources"]
    if st.session_state.instructor_mode:
        nav_options.append("Instructor Guide")

    page = st.radio(
        "Navigate",
        nav_options,
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    # Lesson progress in sidebar
    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-level-badge">
        <div style="font-size:13px; color:#A8B8CC; margin-bottom:4px;">Lessons Completed</div>
        <strong style="font-size:26px;">{completed} / 3</strong><br>
        <div style="font-size:14px; color:#A8B8CC; margin-top:4px;">{"All done! You're a Pioneer." if completed == 3 else "Keep going!"}</div>
    </div>
    """, unsafe_allow_html=True)

    level, level_msg = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f"""
    <div style="text-align:center; margin:10px 0; font-size:16px; color:#A8B8CC;">
        Pioneer Level: <span style="color:#C8942E; font-weight:700;">{level}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    if st.button("Clear Chat History", key="clear_chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    # Instructor mode toggle
    st.markdown("<div style='font-size:13px; color:#A8B8CC; margin-bottom:6px;'>INSTRUCTOR OPTIONS</div>", unsafe_allow_html=True)
    instructor_on = st.toggle("Instructor Mode", value=st.session_state.instructor_mode)
    if instructor_on != st.session_state.instructor_mode:
        st.session_state.instructor_mode = instructor_on
        st.rerun()

    if st.session_state.instructor_mode:
        projector_on = st.toggle("Projector Mode (large text)", value=st.session_state.projector_mode)
        if projector_on != st.session_state.projector_mode:
            st.session_state.projector_mode = projector_on
            st.rerun()
        st.markdown('<div style="background:#1E3A5F; border-radius:6px; padding:8px 12px; font-size:13px; color:#C8942E;">✓ Instructor Mode ON</div>', unsafe_allow_html=True)

# ── Projector mode CSS ───────────────────────────────────────────────────────
if st.session_state.projector_mode:
    st.markdown("""
    <style>
    html, body, [class*="css"], .stApp, p, li, label, span, div {
        font-size: 24px !important;
    }
    .stChatMessage, [data-testid="stChatMessageContent"] {
        font-size: 24px !important;
    }
    h1 { font-size: 3.5rem !important; }
    h2 { font-size: 2rem !important; }
    h3 { font-size: 1.6rem !important; }
    .stButton > button { font-size: 22px !important; padding: 16px 28px !important; }
    .stChatInput textarea { font-size: 22px !important; }
    </style>
    """, unsafe_allow_html=True)

# ── Handle nav_to ─────────────────────────────────────────────────────────────
if "nav_to" in st.session_state:
    del st.session_state["nav_to"]

# ══════════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:3rem; color:#C8942E; margin-bottom:4px;">
        Hi, I'm Barb.
    </h1>
    <p class="lmt-hero-sub">Your AI guide for the 50+TechBridge free lesson program.</p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown(f'<div class="lmt-tip-card"><strong style="color:#C8942E;">Today\'s tip:</strong> {today_tip}</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <h2 style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#C8942E; margin-bottom:8px;">
        Your Free Lessons
    </h2>
    """, unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        badge_class = "done" if done else ""
        badge_text = "✓ Completed" if done else f"Lesson {lesson['number']}"
        card_class = "completed" if done else ""
        skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in lesson["skills"]])
        st.markdown(f"""
        <div class="lesson-card {card_class}">
            <span class="lesson-badge {badge_class}">{badge_text}</span>
            <div class="lesson-title">{lesson['title']}</div>
            <div class="lesson-skills">{lesson['subtitle']}</div>
            <div>{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go to Free Lessons", use_container_width=True, key="home_lessons"):
            st.session_state["nav_to"] = "Free Lessons"
            st.rerun()
    with col2:
        st.markdown('<div class="outline-btn">', unsafe_allow_html=True)
        if st.button("Ask Barb a Question", use_container_width=True, key="home_ask"):
            st.session_state["nav_to"] = "Ask Barb"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FREE LESSONS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Free Lessons":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:2.4rem; color:#C8942E; margin-bottom:4px;">
        Free Lessons
    </h1>
    <p style="color:#A8B8CC; font-size:18px; margin-bottom:0;">
        Three lessons. Watch, learn, and ask Barb anything along the way.
    </p>
    """, unsafe_allow_html=True)

    # ChatGPT launch button
    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E; margin-bottom:20px;">
        <div style="font-family:'Playfair Display',serif; font-size:1.2rem; color:#C8942E; margin-bottom:6px;">Ready to try AI yourself?</div>
        <div style="color:#C4CDD9; font-size:17px; margin-bottom:14px;">Open ChatGPT — free, no account needed to start. Practice what you learned in Lesson 2.</div>
        <a href="https://chat.openai.com" target="_blank"
           style="display:inline-block; background:#C8942E; color:#0E1C2F; font-weight:700;
                  font-size:18px; padding:12px 28px; border-radius:8px; text-decoration:none;
                  font-family:'DM Sans',sans-serif; letter-spacing:0.3px;">
            Open ChatGPT →
        </a>
        <span style="color:#A8B8CC; font-size:14px; margin-left:14px;">Opens in a new tab</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        badge_text = "✓ Completed" if done else f"Lesson {lesson['number']}"
        badge_class = "done" if done else ""
        card_class = "completed" if done else ""
        skills_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in lesson["skills"]])

        st.markdown(f"""
        <div class="lesson-card {card_class}">
            <span class="lesson-badge {badge_class}">{badge_text}</span>
            <div class="lesson-title">{lesson['title']}</div>
            <div class="lesson-skills">{lesson['subtitle']}</div>
            <div style="margin: 10px 0;">{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2, 2, 2])

        with col1:
            st.markdown(f'<a href="{lesson["url"]}" target="_blank" style="display:block; background:#C8942E; color:#0E1C2F; font-weight:700; text-align:center; padding:10px; border-radius:8px; text-decoration:none; font-family:\'DM Sans\',sans-serif;">Watch Lesson {lesson["number"]} →</a>', unsafe_allow_html=True)

        with col2:
            if lesson["youtube"]:
                st.markdown(f'<a href="{lesson["youtube"]}" target="_blank" style="display:block; background:#1E3A5F; color:#C8942E; font-weight:700; text-align:center; padding:10px; border-radius:8px; text-decoration:none; border: 1.5px solid #C8942E; font-family:\'DM Sans\',sans-serif;">▶ YouTube</a>', unsafe_allow_html=True)

        with col3:
            mark_label = "✓ Mark Done" if not done else "↩ Mark Undone"
            if st.button(mark_label, key=f"complete_{lesson['number']}", use_container_width=True):
                if done:
                    st.session_state.lessons_completed.discard(lesson["number"])
                else:
                    st.session_state.lessons_completed.add(lesson["number"])
                st.rerun()

        # Lesson-specific follow-up questions
        with st.expander(f"Ask Barb about Lesson {lesson['number']}"):
            followups = {
                1: [
                    "What exactly is AI in plain English?",
                    "How do I know if an AI answer is correct?",
                    "What's the difference between AI and Google?",
                ],
                2: [
                    "How do I open ChatGPT on my phone?",
                    "What's a good first question to ask AI?",
                    "What if I don't like the answer AI gives me?",
                ],
                3: [
                    "What are the 4 pressure tactics scammers use?",
                    "How do I set up two-factor authentication?",
                    "What do I do if I already sent money to a scammer?",
                    "What is a family code word and how do I pick one?",
                ],
            }
            for q in followups[lesson["number"]]:
                st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
                if st.button(q, key=f"lesson_q_{lesson['number']}_{q[:20]}", use_container_width=True):
                    st.session_state["user_input"] = q
                    st.session_state["nav_to"] = "Ask Barb"
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    if len(st.session_state.lessons_completed) == 3:
        st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)
        col_logo, col_text = st.columns([1, 2])
        with col_logo:
            try:
                st.image("agentic50-logo.png", width=160)
            except Exception:
                st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:2rem; color:#C8942E; text-align:center;">Agentic50</div>', unsafe_allow_html=True)
        with col_text:
            st.markdown("""
            <div style="padding: 12px 0;">
                <div style="font-family:'Playfair Display',serif; font-size:1.4rem; color:#C8942E; margin-bottom:6px;">You're a Digital Pioneer.</div>
                <div style="color:#C4CDD9; font-size:17px;">All 3 lessons complete. You now have the skills to spot fakes, stay safe, and use AI with confidence.</div>
                <div style="color:#A8B8CC; font-size:15px; margin-top:6px;">Follow <strong style="color:#C8942E;">Agentic50</strong> — weekly AI news written for people like you.</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div class="lmt-orange-msg" style="text-align:center; margin-top:8px;">
            <strong>Join us at a library session — bring a friend who needs this.</strong><br>
            <span style="font-size:15px;">Free. No signup required. Just show up.</span>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ASK BARB PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Ask Barb":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:2.4rem; color:#C8942E; margin-bottom:4px;">
        Ask Barb
    </h1>
    <p style="color:#A8B8CC; font-size:18px; margin-bottom:0;">No tech jargon. Just plain talk from a knowledgeable friend.</p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    selected_cat = st.selectbox("Choose a topic:", ["All Topics"] + list(categories.keys()))

    if selected_cat == "All Topics":
        examples = [q for cat_qs in categories.values() for q in cat_qs[:1]]
    else:
        examples = categories[selected_cat]

    st.markdown("<p style='color:#A8B8CC; font-size:16px; margin:12px 0 8px;'><strong style='color:#C4CDD9;'>Not sure what to ask? Try one of these:</strong></p>", unsafe_allow_html=True)

    for example in examples:
        st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
        if st.button(example, key=f"ex_{example}", use_container_width=True):
            st.session_state["user_input"] = example
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div class="lmt-barb-greeting">
            Hi there! I'm Barb, your guide through the 50+TechBridge lessons.
            Ask me anything about what you're learning — or anything about using AI and technology in daily life.
            <strong style="color:#C8942E;">No question is too simple.</strong>
        </div>
        """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Type your question here...")

    if "user_input" in st.session_state:
        prompt = st.session_state.pop("user_input")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.questions_asked += 1

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
            client = anthropic.Anthropic(api_key=api_key)

            with client.messages.stream(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system=LESSON_SYSTEM_PROMPT,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            ) as stream:
                reply = st.write_stream(stream.text_stream)

        st.session_state.messages.append({"role": "assistant", "content": reply})

        st.session_state.last_reply = reply

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

        # Instructor explainer — shows after every response in instructor mode
        if st.session_state.instructor_mode:
            st.markdown("""
            <div style="background:#0E2A1A; border:1px solid #109F35; border-radius:10px; padding:18px 22px; margin-top:16px;">
                <div style="font-size:13px; color:#109F35; font-weight:700; letter-spacing:1px; margin-bottom:8px;">INSTRUCTOR — WHAT JUST HAPPENED</div>
                <div style="color:#C4CDD9; font-size:17px; line-height:1.6;">
                    <strong style="color:#C8942E;">1. You typed a question</strong> — called a "prompt." The clearer the question, the better the answer.<br><br>
                    <strong style="color:#C8942E;">2. Barb read the whole conversation</strong> — not just your last message. AI keeps context, like a conversation with a friend.<br><br>
                    <strong style="color:#C8942E;">3. Barb predicted the best response</strong> — AI generates text one word at a time, choosing what word fits best based on billions of examples it was trained on.<br><br>
                    <strong style="color:#C8942E;">4. Barb followed her instructions</strong> — she's set up to be warm, plain-spoken, and focused on 50+ adults. Those rules shaped the answer.<br><br>
                    <em style="color:#A8B8CC;">Point out to students: Barb didn't "look it up." She generated a response. That's why you always verify important information.</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MY PROGRESS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "My Progress":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:2.4rem; color:#C8942E; margin-bottom:4px;">
        My Progress
    </h1>
    <p style="color:#A8B8CC; font-size:18px; margin-bottom:0;">Track your Pioneer journey.</p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    completed = len(st.session_state.lessons_completed)
    st.markdown(f"""
    <div class="lmt-progress-card">
        <div style="font-size:14px; color:#A8B8CC; margin-bottom:8px; text-transform:uppercase; letter-spacing:1px;">Lessons Completed</div>
        <h2>{completed} of 3</h2>
        <p>{"All three lessons done — you're a Digital Pioneer!" if completed == 3 else "Keep going — every lesson builds your confidence."}</p>
    </div>
    """, unsafe_allow_html=True)

    for lesson in LESSONS:
        done = lesson["number"] in st.session_state.lessons_completed
        icon = "✓" if done else "○"
        color = "#109F35" if done else "#A8B8CC"
        st.markdown(f"""
        <div style="display:flex; align-items:center; padding: 10px 0; border-bottom: 1px solid #1E3A5F;">
            <span style="font-size:22px; color:{color}; margin-right:14px;">{icon}</span>
            <div>
                <div style="font-family:'DM Sans',sans-serif; font-weight:700; color:#C4CDD9;">Lesson {lesson['number']}: {lesson['title']}</div>
                <div style="font-size:15px; color:#A8B8CC;">{lesson['subtitle']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    level, level_msg = get_pioneer_level(st.session_state.questions_asked)
    st.markdown(f"""
    <div class="lmt-progress-card">
        <div style="font-size:14px; color:#A8B8CC; margin-bottom:8px; text-transform:uppercase; letter-spacing:1px;">Your Pioneer Level</div>
        <h2>{level}</h2>
        <p>{level_msg}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Questions Asked", st.session_state.questions_asked)
    with col2:
        st.metric("Helpful Answers", st.session_state.helpful_count)
    with col3:
        st.metric("Lessons Done", completed)

# ══════════════════════════════════════════════════════════════════════════════
# RESOURCES PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Resources":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:2.4rem; color:#C8942E; margin-bottom:4px;">
        Resources
    </h1>
    <p style="color:#A8B8CC; font-size:18px; margin-bottom:0;">Helpful links for your AI learning journey.</p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card">
        <h3>50+TechBridge Free Lessons</h3>
        <ul>
            <li><a href="https://50plustechbridge.com/start-free-lessons/" target="_blank">Start Free Lessons →</a></li>
            <li><a href="https://youtu.be/YsSXhxo_fus" target="_blank">Lesson 3 on YouTube: Don't Get Scammed</a></li>
            <li>In-person sessions: Austin Public Library branches + senior centers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card">
        <h3>Report a Scam</h3>
        <ul>
            <li><a href="https://reportfraud.ftc.gov" target="_blank">reportfraud.ftc.gov</a> — Federal Trade Commission</li>
            <li><a href="https://www.ic3.gov" target="_blank">ic3.gov</a> — FBI Internet Crime Complaint Center</li>
            <li><a href="https://www.identitytheft.gov" target="_blank">identitytheft.gov</a> — If your identity was stolen</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card">
        <h3>Local Austin Resources</h3>
        <ul>
            <li><strong>Austin Public Library</strong> — Free computer classes and WiFi at 6 branches</li>
            <li><strong>AARP Austin</strong> — Senior centers and digital skills programs</li>
            <li><strong>Foundation Communities</strong> — Community tech support</li>
            <li><strong>211</strong> — Call or text for local services and support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card">
        <h3>AI Safety Reminders</h3>
        <ul>
            <li>Never share your Social Security number, bank info, or passwords with AI</li>
            <li>AI can make mistakes — always verify important health or legal information</li>
            <li>If something feels like a scam — it probably is. Hang up and call back on the real number.</li>
            <li>AI is a tool. Your doctor, lawyer, and financial advisor still matter.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# INSTRUCTOR GUIDE PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Instructor Guide":
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif; font-size:2.4rem; color:#C8942E; margin-bottom:4px;">
        Instructor Guide
    </h1>
    <p style="color:#A8B8CC; font-size:18px; margin-bottom:0;">
        How to demo Barb in class — what to say, what to show, what it means.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    # What is Barb — explain to students
    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E;">
        <h3>What to Tell the Class</h3>
        <p style="font-size:17px; line-height:1.7;">
            <em>"Barb is an AI assistant — the same technology as ChatGPT or Claude, but built specifically
            for people in this program. She knows the content of all three lessons. You can ask her anything
            you're confused about, and she'll answer in plain English — no jargon."</em>
        </p>
        <p style="font-size:17px; line-height:1.7;">
            <em>"But here's what's important to understand: Barb doesn't look things up. She generates
            her answer word by word, based on patterns in everything she was trained on. That means she
            can be wrong. For anything important — medical, legal, financial — you verify."</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:12px 0;'>", unsafe_allow_html=True)

    # Demo flow per lesson
    demo_flows = [
        {
            "lesson": "Lesson 1 — Welcome to AI",
            "setup": "Use this demo to show students what AI is before they've ever tried it.",
            "steps": [
                ("Say this", "\"Watch what happens when I type a question. I'm going to ask Barb something simple.\""),
                ("Type this", "\"What is AI in plain English?\""),
                ("Point out", "Notice how she answers in short paragraphs — no jargon. That's by design."),
                ("Say this", "\"Now watch — I'm going to ask a follow-up. AI remembers the conversation.\""),
                ("Type this", "\"Can AI make mistakes?\""),
                ("Debrief", "\"See how she kept the context? That's the difference between AI and a search engine. It's a conversation.\""),
            ],
            "talking_point": "AI is a conversation, not a search. The more specific your question, the better the answer.",
        },
        {
            "lesson": "Lesson 2 — Talk to AI",
            "setup": "Use after students have watched Lesson 2. This shows them what a real AI conversation looks like.",
            "steps": [
                ("Say this", "\"Let's practice asking a good question together. What's something you deal with every day?\""),
                ("Take a suggestion", "Pick one from the class — doctor appointment, medication reminder, etc."),
                ("Type it", "Type their suggestion into Barb as a question."),
                ("Point out", "\"Notice how I typed it like I'm talking to a person — not like a Google search.\""),
                ("Say this", "\"If you don't like the answer, you don't have to start over. Just say: Can you say that more simply?\""),
                ("Type this", "\"Can you say that in two sentences?\""),
                ("Debrief", "\"That's a follow-up prompt. You stay in charge of the conversation.\""),
            ],
            "talking_point": "You are always in charge. If the answer doesn't work for you, ask again differently.",
        },
        {
            "lesson": "Lesson 3 — Don't Get Scammed",
            "setup": "Use to reinforce the three skills after the lesson video.",
            "steps": [
                ("Say this", "\"Let's test Barb on what we just learned. I'm going to ask her about the pressure tactics.\""),
                ("Type this", "\"What are the four pressure tactics scammers use?\""),
                ("Point out", "\"She gives you the four levers — Hurry, Fear, Secrecy, Authority. Same as the lesson.\""),
                ("Say this", "\"Now let's ask her what to do if it already happened.\""),
                ("Type this", "\"What should I do if I already sent money to a scammer?\""),
                ("Point out", "\"She gives you steps. Notice she says 'tell one trusted person' — because shame keeps people from reporting.\""),
                ("Debrief", "\"You can use Barb at home to review anything from today. She won't judge you for asking the same question twice.\""),
            ],
            "talking_point": "No question is too simple. Barb is a practice partner — not a test.",
        },
    ]

    for flow in demo_flows:
        with st.expander(f"📋 {flow['lesson']}", expanded=False):
            st.markdown(f"""
            <div style="background:#1E3A5F; border-radius:8px; padding:12px 16px; margin-bottom:14px; font-size:16px; color:#C4CDD9;">
                <strong style="color:#C8942E;">Setup:</strong> {flow['setup']}
            </div>
            """, unsafe_allow_html=True)

            for i, (action, detail) in enumerate(flow["steps"]):
                color = "#C8942E" if action in ("Type this", "Say this") else "#109F35" if action == "Debrief" else "#A8B8CC"
                st.markdown(f"""
                <div style="display:flex; align-items:flex-start; padding:10px 0; border-bottom:1px solid #1E3A5F;">
                    <div style="min-width:110px; font-size:13px; font-weight:700; color:{color}; padding-top:2px;">{action.upper()}</div>
                    <div style="font-size:17px; color:#C4CDD9; line-height:1.5;">{detail}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="background:#0E2A1A; border-left:4px solid #109F35; border-radius:6px; padding:12px 16px; margin-top:14px;">
                <strong style="color:#109F35; font-size:13px;">KEY TALKING POINT</strong><br>
                <span style="color:#C4CDD9; font-size:17px;">{flow['talking_point']}</span>
            </div>
            """, unsafe_allow_html=True)

            # Live demo buttons
            st.markdown("<div style='margin-top:14px; font-size:14px; color:#A8B8CC;'>Run this demo question live:</div>", unsafe_allow_html=True)
            demo_qs = {
                "Lesson 1 — Welcome to AI": "What is AI in plain English?",
                "Lesson 2 — Talk to AI": "Can you help me write a message to my doctor about my next appointment?",
                "Lesson 3 — Don't Get Scammed": "What are the four pressure tactics scammers use?",
            }
            q = demo_qs[flow["lesson"]]
            st.markdown('<div class="pill-btn">', unsafe_allow_html=True)
            if st.button(f"▶ Demo: \"{q}\"", key=f"demo_{flow['lesson']}", use_container_width=True):
                st.session_state["user_input"] = q
                st.session_state["nav_to"] = "Ask Barb"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1E3A5F; margin:16px 0;'>", unsafe_allow_html=True)

    # Quick reference for instructors
    st.markdown("""
    <div class="lmt-section-card">
        <h3>Quick Reference — What to Say When Students Ask</h3>
        <table class="lmt-table">
            <thead><tr><th>If a student asks...</th><th>Say this</th></tr></thead>
            <tbody>
                <tr><td>"Is Barb always right?"</td><td>"No — and that's the lesson. AI generates answers. You verify the important ones."</td></tr>
                <tr><td>"How does it know what I'm asking?"</td><td>"It reads your whole message and predicts the most helpful response. The clearer you write, the better it works."</td></tr>
                <tr><td>"Is this safe to use?"</td><td>"Yes — don't type passwords or Social Security numbers into any AI. Everything else is fine to ask."</td></tr>
                <tr><td>"What if I can't spell?"</td><td>"Doesn't matter. AI is very good at understanding what you mean, even with typos."</td></tr>
                <tr><td>"Can I use this at home?"</td><td>"Yes — it's free at securestep.ai. So is ChatGPT at chat.openai.com."</td></tr>
                <tr><td>"Who is Barb?"</td><td>"Barb is an AI built for this program by 50+TechBridge. She's powered by Claude, the same AI as this class uses."</td></tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="lmt-section-card" style="border-color:#C8942E; margin-top:14px;">
        <h3>Instructor Reminders</h3>
        <ul>
            <li>Turn on <strong style="color:#C8942E;">Projector Mode</strong> in the sidebar before class — bigger text for the screen</li>
            <li>Run the demo questions FIRST yourself, before class — so you know what Barb will say</li>
            <li>If Barb gives a wrong or strange answer, use it — say "See? This is why we verify."</li>
            <li>Encourage students to type their OWN question during class — even one word is fine</li>
            <li>End every demo with: "You can ask Barb this same question at home. It's free."</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
