import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

# Page Config
st.set_page_config(page_title="AI Translator", page_icon="🌍", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 AI Language Translator</h1>", unsafe_allow_html=True)
st.write("Translate text instantly with AI 🚀")

# Input Text
text = st.text_area("✍️ Enter text:", height=150)

# Languages
languages = {
    "Arabic 🇪🇬": "ar",
    "English 🇺🇸": "en",
    "French 🇫🇷": "fr",
    "German 🇩🇪": "de",
    "Spanish 🇪🇸": "es",
    "Italian 🇮🇹": "it",
    "Hindi 🇮🇳": "hi"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From", list(languages.keys()))

with col2:
    target_lang = st.selectbox("To", list(languages.keys()))

# Session for history
if "history" not in st.session_state:
    st.session_state.history = []

# Translate Button
if st.button("🚀 Translate"):
    if text:
        with st.spinner("Translating..."):
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

        st.success("✅ Translation:")
        st.write(translated)

        # Save history
        st.session_state.history.append((text, translated))

        # Copy box
        st.code(translated)

        # Text-to-Speech
        tts = gTTS(translated)
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        tts.save(temp_file.name)

        st.audio(temp_file.name)

    else:
        st.warning("⚠️ Please enter text!")

# ================= Sidebar History =================
st.sidebar.title("📜 Translation History")

if st.session_state.history:
    for original, translated in reversed(st.session_state.history[-5:]):
        st.sidebar.markdown(f"**📝 Original:** {original}")
        st.sidebar.markdown(f"**🌐 Translated:** {translated}")
        st.sidebar.markdown("---")
else:
    st.sidebar.write("No translations yet")

# زرار مسح الهيستوري
if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared!")