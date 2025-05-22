from gtts import gTTS
import qrcode
import os

rack = "Rack 01"
sections = [
    ("001.42", "Research methods"),
    ("001.422", "Statistical methods"),
    ("001.424", "Operations Research"),
    ("001.43", "Computer Simulation"),
    ("001.5", "Information and Communication"),
    ("001.53", "Cybernetics"),
    ("001.535", "Artificial Intelligence"),
]

text = f"Hi, you are in {rack} and it has the following sections: "
for call_no, subject in sections:
    text += f"Call number {call_no} has subject {subject}. "

# Create output directories
os.makedirs("../src/main/resources/static/audio", exist_ok=True)
os.makedirs("../src/main/resources/static/qr", exist_ok=True)

# Generate audio
audio_path = "../src/main/resources/static/audio/rack01_audio.mp3"
tts = gTTS(text)
tts.save(audio_path)

# Generate QR code pointing to the hosted audio
audio_url = "http://localhost:8080/audio/rack01_audio.mp3"
qr = qrcode.make(audio_url)
qr_path = "../src/main/resources/static/qr/rack01_qr.png"
qr.save(qr_path)

print("Audio and QR code generated successfully.")
