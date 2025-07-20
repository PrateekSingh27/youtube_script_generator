import streamlit as st
from script_generator_groq import generate_script
import datetime

st.set_page_config(page_title="YouTube Script Generator", layout="centered")

st.title("🎥 YouTube Script Generator")

topic = st.text_input("🎯 Enter your video topic")

if st.button("Generate Script"):
    with st.spinner("Crafting your cinematic masterpiece..."):
        script = generate_script(topic)
        st.success("✅ Script generated!")

        # Display the script
        st.text_area("📜 Your Script", value=script, height=400)

        # Prepare script as downloadable file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"youtube_script_{timestamp}.txt"

        st.download_button(
            label="📥 Download Script as .txt",
            data=script,
            file_name=filename,
            mime="text/plain"
        )