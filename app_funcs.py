import streamlit as st
from transformers import pipeline
import fitz
import docx
import re

@st.cache_resource
def emotion_generate(plain_text):
    emotion = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=1
    )

    emotion_labels = emotion(plain_text)
    return emotion_labels[0][0]["label"]


@st.cache_data
def extract_text_txt(uploaded_txt_file, downloaded_txt_file):
    with open(uploaded_txt_file) as intxt:
        data = intxt.read()

    data = re.findall('[aA-zZ]+', data)
    with open(downloaded_txt_file, 'w') as outtxt:
        outtxt.write('\n'.join(data))
    return ' '.join(data)


@st.cache_data
def extract_text_pdf(uploaded_pdf_file):
    with fitz.open(uploaded_pdf_file) as intxt:
        text = ""
        for page in intxt:
            text += page.get_text()
    return text


@st.cache_data
def extract_text_docx(uploaded_docx_file):
    doc = docx.Document(uploaded_docx_file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ' '.join(fullText)


def download_success():
    st.balloons()
