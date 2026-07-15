# 😲 Streamlit Based Deep Emotion Detector 😄

[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![Maintained by Jony](https://img.shields.io/badge/Maintained%20by-Jony-blue.svg)](https://github.com/jonyinti)

A Streamlit-based web application to process text and detect emotions from user input using the **EmoRoBERTa** model from Hugging Face Transformers 🤗.

---

## 📸 Demo

![Text Demo](https://user-images.githubusercontent.com/29462447/156898269-e6154cda-4e4c-4113-96c6-dc7fcd25dbf9.gif)

![Document Demo](https://user-images.githubusercontent.com/29462447/156898267-8b33d311-6d11-47f7-8638-c213b9cd30fc.gif)

---

# 🚀 Features

- Detect emotions from text
- Upload PDF, DOCX, and TXT files
- Real-time emotion prediction
- Interactive Streamlit interface
- Powered by Hugging Face Transformers

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/jonyinti/Deep-Emotion-Detector.git
```

Move into the project directory:

```bash
cd Deep-Emotion-Detector
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the application:

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

To increase the upload limit:

```bash
streamlit run app.py --server.maxUploadSize=1028
```

---

# 📊 Results

### Emotion Detection

![Emotion Detection](https://user-images.githubusercontent.com/29462447/156898275-e5ec4c14-845c-4311-9396-b4703537c2ad.png)

### Document Emotion Detection

![Document Result 1](https://user-images.githubusercontent.com/29462447/156898297-8dbc6a3a-f6ab-472b-929e-ab6cbcd9bdb8.png)

![Document Result 2](https://user-images.githubusercontent.com/29462447/156898300-dbc20937-c34b-4fd5-9bfe-2b010e83e6f6.png)

---

# 🐳 Running with Docker

Build the Docker image:

```bash
docker build -f Dockerfile -t app:latest .
```

Run the Docker container:

```bash
docker run -p 8501:8501 app:latest
```

Open:

```
http://localhost:8501
```

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

---

# 📁 Project Structure

```
Deep-Emotion-Detector/
│
├── app.py
├── app_funcs.py
├── requirements.txt
├── Dockerfile
├── setup.sh
├── README.md
├── static/
├── uploads/
├── downloads/
├── samples/
└── .streamlit/
```

---

# 👨‍💻 Maintainer

**Jony Emmanuel Inti**

GitHub: https://github.com/jonyinti

Repository:

https://github.com/jonyinti/Deep-Emotion-Detector

---

# 📄 License

This project is licensed under the MIT License.