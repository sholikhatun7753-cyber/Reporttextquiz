import streamlit as st

st.set_page_config(page_title="Quiz Sarapan", layout="centered")

# ====== DATA QUIZ ======
questions = [
    {
        "title": "Pilih menu sarapanmu!",
        "options": ["Fried Rice", "Fried Chicken", "Fries"],
        "key": "sarapan"
    },
    {
        "title": "Bagaimana perasaanmu pagi ini?",
        "options": ["Sleepy", "Hungry", "Focus"],
        "key": "mood"
    }
]

# ====== STATE SLIDE ======
if "slide" not in st.session_state:
    st.session_state.slide = 0

# ====== CONTENT SLIDE ======
q = questions[st.session_state.slide]   # soal berdasarkan index slide

st.title("🍽️ Morning Quiz – Style Quizizz")
st.subheader(f"Soal {st.session_state.slide + 1}")

st.markdown(f"### {q['title']}")

# pilihan jawaban
answer = st.radio("Pilih jawaban:", q["options"], key=q["key"])

# ====== Navigation Buttons ======
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.session_state.slide > 0:
        if st.button("⬅️ Prev"):
            st.session_state.slide -= 1

with col3:
    if st.session_state.slide < len(questions) - 1:
        if st.button("Next ➡️"):
            st.session_state.slide += 1

# ====== LAST SLIDE RESULT ======
if st.session_state.slide == len(questions) - 1:
    st.markdown("---")
    st.subheader("🎉 Hasil & Feedback")

    sarapan = st.session_state.get("sarapan", None)
    mood = st.session_state.get("mood", None)

    if sarapan:
        st.write(f"🍽️ **Sarapanmu:** {sarapan}")

    # Feedback mood
    if mood == "Sleepy":
        st.warning("😴 Ngantuk! Kamu lupa sarapan bergizi.")
    elif mood == "Hungry":
        st.error("🍽️ Belajar tidak nyaman karena tidak sarapan sehat.")
    elif mood == "Focus":
        st.success("🎉
