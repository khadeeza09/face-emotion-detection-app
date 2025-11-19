import cv2
from deepface import DeepFace
import pyttsx3
import time

# ---------------------------
# TEXT TO SPEECH
# ---------------------------
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# Set female voice
for v in voices:
    if "female" in v.name.lower():
        engine.setProperty("voice", v.id)
        break

engine.setProperty("rate", 170)

last_spoken = 0
SPEAK_COOLDOWN = 5  # seconds
last_emotion = ""
stable_count = 0
STABLE_REQUIRED = 5


# Convert emotion to message
def emotion_to_message(emotion):
    mapping = {
        "sad": "You look sad today. Stay strong.",
        "happy": "You look happy today!",
        "angry": "You look angry. Try to relax.",
        "surprise": "You look surprised.",
        "fear": "You look scared. It's okay.",
        "neutral": "You look neutral.",
    }
    return mapping.get(emotion, f"You look {emotion}.")


# ---------------------------
# CAMERA
# ---------------------------
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)

        # FIX: If result is a list, take first item
        if isinstance(result, list):
            result = result[0]

        emotion = result["dominant_emotion"]
        region = result["region"]

        x, y, w, h = region["x"], region["y"], region["w"], region["h"]

        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show emotion text
        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 0, 0),
            2,
        )

        # Stability check
        if emotion == last_emotion:
            stable_count += 1
        else:
            stable_count = 0

        last_emotion = emotion
        current_time = time.time()

        # Speak when stable + cooldown passed
        if stable_count >= STABLE_REQUIRED and (current_time - last_spoken) > SPEAK_COOLDOWN:
            msg = emotion_to_message(emotion)
            engine.say(msg)
            engine.runAndWait()
            last_spoken = current_time

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
