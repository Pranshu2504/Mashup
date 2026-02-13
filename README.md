# 🎵 YouTube Mashup Generator

A beautiful Streamlit web application that generates a mashup from YouTube videos of your favorite singer.

This project was developed as part of the **Mashup Assignment**, which includes:

- ✅ Command Line Mashup Program
- ✅ Web App Mashup Generator
- ✅ Email delivery of generated mashup
- ✅ Secure environment variable handling

---

## 🚀 Live Web App

👉 Deployed on Streamlit Cloud  
https://yt-mashup.streamlit.app/

---

## 🖥️ UI Preview

![UI Preview](ui-preview.png)

---

## ✨ Features

- 🎤 Download N YouTube videos of a singer
- 🎧 Extract and trim first Y seconds from each
- 🎼 Merge all trimmed audios into one mashup
- 📦 Compress output into ZIP file
- 📧 Automatically send mashup to user email
- 🔐 Secure credentials using Streamlit Secrets
- 🧹 Auto cleanup of temporary files

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **yt-dlp**
- **FFmpeg**
- **SMTP (Gmail App Password)**
- **Streamlit Cloud Deployment**

---

## 📥 How It Works

1. User enters:
   - Singer Name
   - Number of Videos (>10)
   - Duration per Video (>20 seconds)
   - Valid Email Address

2. Application:
   - Downloads videos using yt-dlp
   - Trims audio using FFmpeg
   - Merges audio files
   - Creates mashup.zip
   - Sends file to user email

---

## 🔐 Environment Variables

This project uses **Streamlit Secrets** for secure credentials.

Add in Streamlit Cloud → App Settings → Secrets:

```
SENDER_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

---

## 📦 requirements.txt

```
streamlit
yt-dlp
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure

```
Mashup/
│
├── app.py
├── requirements.txt
├── ui-preview.png
└── README.md
```

---

## 🎯 Assignment Requirements Covered

### ✅ Program 1
- Command line Python program
- Parameter validation
- Exception handling
- Audio trimming & merging

### ✅ Program 2
- Web-based mashup generator
- User input validation
- Email delivery in ZIP format
- Secure credentials

---

## 📧 Author

Pranshu Goel

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub!
