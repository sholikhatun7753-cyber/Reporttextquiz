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

total_slides = len(questions) + 1  # +1 untuk slide hasil

# ====== STATE SLIDE ======
if "slide" not in st.session_state:
    st.session_state.slide = 0

# ====== TAMPILKAN SOAL ======
if st.session_state.slide < len(questions):

    q = questions[st.session_state.slide]

    st.title("🍽️ Morning Quiz – Quizizz Style")
    st.subheader(f"Soal {st.session_state.slide + 1}")
    st.write(q["title"])

    st.radio("Pilih jawaban:", q["options"], key=q["key"])

else:
    # ====== SLIDE HASIL ======
    st.title("🎉 Hasil Kamu")

    sarapan = st.session_state.get("sarapan", None)
    mood = st.session_state.get("mood", None)

    if sarapan:
        st.write("🍽️ Sarapanmu:", sarapan)

    if mood == "Sleepy":
        st.warning("😴 Kamu ngantuk, mungkin kurang sarapan.")
    elif mood == "Hungry":
        st.error("🍔 Kamu lapar! Seharusnya sarapan dulu.")
    elif mood == "Focus":
        st.success("✨ Kamu fokus! Bagus sekali!")
    else:
        st.info("Mood tidak terbaca.")

    st.write("Terima kasih sudah mengikuti quiz! 🌞")

# ====== NAVIGASI ======
col1, col2, col3 = st.columns(3)

# Tombol Prev
with col1:
    if st.session_state.slide > 0:
        if st.button("⬅️ Prev"):
            st.session_state.slide -= 1

# Tombol Next
with col3:
    if st.session_state.slide < total_slides - 1:
        if st.button("Next ➡️"):
            st.session_state.slide += 1
