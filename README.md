😊 Face Emotion Detection App (Python | DeepFace | OpenCV | TTS)

A real-time facial emotion recognition app built using Python, OpenCV, DeepFace, and pyttsx3.
The system detects a face from the webcam, analyzes the emotion, shows it on the screen, and speaks the emotion using text-to-speech.

🔥 Features

Real-time webcam emotion detection

DeepFace CNN-based emotion analysis

Automatic text-to-speech response

Emotion stability check (prevents rapid speaking)

Cooldown timer for speaking

Bounding box + emotion label on screen

Supports sad, happy, angry, neutral, surprise, fear

🧠 Tech Stack

Python

OpenCV

DeepFace

Pyttsx3

NumPy

Time module

📁 Project Structure

face-emotion-detection-app/

│── emotion_app.py                # Main application code

│── README.md                     # Documentation

│── screenshots/                  # Output images (optional)

▶️ How the App Works

Opens your webcam

Reads frames continuously

Detects faces and extracts ROI

DeepFace predicts the dominant emotion

Shows the emotion on-screen

Speaks the emotion only when stable & cooldown passed

The stability logic prevents the model from speaking every frame.

▶️ Run the App

pip install opencv-python deepface pyttsx3

1. Install dependencies

2. (If DeepFace errors) install additional dependencies:

pip install tensorflow

pip install gdown

3. Run the script

python emotion_app.py

📸 Screenshots

![Output Screenshot](https://github.com/user-attachments/assets/b3bbb9f8-7e99-46f0-be6b-4ccc93805a8d)


🚀 Future Improvements

Add a GUI using Tkinter or PyQt

Save detected emotions to a log file

Add support for multiple faces

Add sound effects or alerts

Create a web-based version using Streamlit

📄 License

Open-source. Free to use and modify.


