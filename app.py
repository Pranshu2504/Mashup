import streamlit as st
import yt_dlp
import os
import zipfile
import smtplib
from email.message import EmailMessage
from pydub import AudioSegment
from dotenv import load_dotenv

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="YouTube Mashup Generator 🎵", page_icon="🎧", layout="centered")

st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:800;
    text-align:center;
    color:#ff4b4b;
}
.subtitle {
    font-size:18px;
    text-align:center;
    color:gray;
}
.stButton>button {
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎵 YouTube Mashup Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create a mashup from your favorite singer</div>', unsafe_allow_html=True)

st.divider()

# -----------------------------
# INPUTS
# -----------------------------
singer = st.text_input("🎤 Singer Name")
num_videos = st.number_input("📹 Number of Videos (>10)", min_value=11, step=1)
duration = st.number_input("⏱ Duration per Video (seconds, >20)", min_value=21, step=1)
email = st.text_input("📧 Email Address")

generate = st.button("🚀 Generate Mashup")

# -----------------------------
# FUNCTIONS
# -----------------------------
def download_videos(singer, num_videos):
    os.makedirs("downloads", exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }
    search_query = f"ytsearch{num_videos}:{singer} songs"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

def convert_trim_merge(duration, output_name):
    combined = AudioSegment.empty()
    for file in os.listdir("downloads"):
        if file.endswith((".webm", ".m4a", ".mp4")):
            path = os.path.join("downloads", file)
            audio = AudioSegment.from_file(path)
            trimmed = audio[:duration * 1000]
            combined += trimmed
    combined.export(output_name, format="mp3")

def send_email(receiver, filename):
    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File 🎵"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver

    with open(filename, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=filename
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)

# -----------------------------
# MAIN
# -----------------------------
if generate:
    if not singer or not email:
        st.error("Please fill all fields.")
    else:
        try:
            with st.spinner("Downloading videos..."):
                download_videos(singer, num_videos)

            with st.spinner("Processing audio..."):
                output_file = "mashup.mp3"
                convert_trim_merge(duration, output_file)

            zip_filename = "mashup.zip"
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                zipf.write(output_file)

            with st.spinner("Sending email..."):
                send_email(email, zip_filename)

            st.success("🎉 Mashup sent successfully!")

        except Exception as e:
            st.error(f"Error: {e}")
