import streamlit as st
from PIL import Image
import os
from app_funcs import *

st.set_page_config(
    page_title="Emotion Detector",
    page_icon="😉",
    layout="centered",
)

# Images
top_image = Image.open("static/banner_top.png")
bottom_image = Image.open("static/banner_bottom.png")
main_image = Image.open("static/main_banner.png")

upload_path = "uploads/"
download_path = "downloads/"

# Sidebar
st.sidebar.image(top_image, use_container_width=True)

format_type = st.sidebar.selectbox(
    "Detect Emotion From",
    ["Plain Text 📝", "Documents 📑"]
)

st.sidebar.image(bottom_image, use_container_width=True)

# Main Page
st.image(main_image, use_container_width=True)
st.title("😲 Deep Emotion Detector 😄")

# ===========================
# Plain Text
# ===========================
if format_type == "Plain Text 📝":

    text = st.text_area(
        "Enter your text here:",
        height=250,
        placeholder="Type your text here..."
    )

    if st.button("Find Emotion ✨"):

        if text.strip() == "":
            st.warning("Please enter some text.")
        else:
            emotion_output = emotion_generate(text)
            st.success(f"Detected Emotion: **{emotion_output.title()}**")
            download_success()

# ===========================
# Documents
# ===========================
else:

    st.info("Supported formats: TXT, PDF, DOCX")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["txt", "pdf", "docx"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(upload_path, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if uploaded_file.name.lower().endswith(".txt"):

            processed_file = os.path.join(
                download_path,
                "processed_" + uploaded_file.name
            )

            text = extract_text_txt(file_path, processed_file)

        elif uploaded_file.name.lower().endswith(".pdf"):

            text = extract_text_pdf(file_path)

        else:

            text = extract_text_docx(file_path)

        emotion_output = emotion_generate(text)

        st.success(f"Detected Emotion: **{emotion_output.title()}**")
        download_success()

# Footer
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ by <b>Jony</b></center>",
    unsafe_allow_html=True
)
