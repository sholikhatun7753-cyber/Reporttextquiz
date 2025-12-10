import streamlit as st

# --- Slideshow sederhana ---
st.title("🍽️ Descriptive Text: The Golden Plate of Morning Energy")

slides = [
    "### Slide 1\n🍳 **Selamat datang di Menu Sarapan Pagi!**\nNikmati energi pagi dengan pilihan makanan bergizi.",
    "### Slide 2\n🍱 **Menu untuk Sarapan:**\n- Fried Rice\n- Fried Chicken\n- Fries",
    "### Slide 3\n💬 **Bagikan perasaan pagimu!**\nApakah kamu merasa sleepy, hungry, atau focus?"
]

# Session state untuk index slide
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Tampilkan slide sekarang
st.markdown(slides[st.session_state.slide_index])

# Tombol navigasi
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Prev") and st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1
with col2:
    if st.button("Next ➡️") and st.session_state.slide_index < len(slides) - 1:
        st.session_state.slide_index += 1


st.markdown("---")

# --- Form Input Sarapan ---
st.subheader("🍽️ Pilih Menu Sarapan")

menu_sarapan = st.selectbox(
    "Masukkan menu sarapanmu:",
    ["fried rice", "fried chicken", "fries"]
)

st.write(f"**Sarapanmu adalah:** {menu_sarapan}")

# --- Form Mood ---
st.subheader("💭 Bagaimana perasaanmu pagi ini?")

mood = st.selectbox(
    "Masukkan mood pagi kamu:",
    ["sleepy", "hungry", "focus"]
)

# Logika mood
if mood == "sleepy":
    st.warning("😴 Ngantuk! Kamu lupa sarapan bergizi.")
elif mood == "hungry":
    st.error("🍽️ Belajar tidak nyaman karena tidak sarapan sehat.")
elif mood == "focus":
    st.success("🎉 Selamat! Kamu bisa belajar dengan baik!")
else:
    st.info("Mood tidak dikenali, jangan lupa sarapan ya!")

st.markdown("### Terimakasih sudah berbagi perasaanmu pagi ini!")
