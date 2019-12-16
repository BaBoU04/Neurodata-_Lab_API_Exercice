import cv2
import json
import time
import os

def visualize_result(image, res, i):

    # Visualize each faces in result
    for k in range(len(res)):

        # Get face coordinates
        x = res[k]['x']
        y = res[k]['y']
        w = res[k]['w']
        h = res[k]['h']

        # Draw rectangle on image
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255))

        # Assign an emotion to an emoji
        if res[k]['emotions'][0][1] == 'Neutral':
            emoji = neutral
        if res[k]['emotions'][0][1] == 'Sadness':
            emoji = sadness
        if res[k]['emotions'][0][1] == 'Happiness':
            emoji = happy
        if res[k]['emotions'][0][1] == 'Disgust':
            emoji = disgust
        if res[k]['emotions'][0][1] == 'Surprise':
            emoji = surprise
        if res[k]['emotions'][0][1] == 'Anger':
            emoji = anger
        if res[k]['emotions'][0][1] == 'Anxiety':
            emoji = anxious

        # Resize emoji to stay within the border of the frame
        emoji = cv2.resize(emoji, (100, 100))
        image[y:y+emoji.shape[0], x:x+emoji.shape[1]] = emoji

    return image

# Json files path
face_json_path = os.path.join('ndlapi_results', 'video.mp4_FaceDetector_result.json')
face_json = os.path.join(face_json_path)
emo_json_path = os.path.join('ndlapi_results','video.mp4_EmotionRecognition_result.json')
emo_json = os.path.join(emo_json_path)
# Open and load json files
with open(face_json) as face_data:
    face_json = json.load(face_data)

with open(emo_json) as emo_data:
    emo_json = json.load(emo_data)

# Emojis png path
anger_path = os.path.join('graphics', 'anger.png')
anger = cv2.imread(anger_path)
disgust_path = os.path.join('graphics', 'disgust.png')
disgust = cv2.imread(disgust_path)
happy_path = os.path.join('graphics', 'happy.png')
happy = cv2.imread(happy_path)
neutral_path = os.path.join('graphics', 'neutral.png')
neutral = cv2.imread(neutral_path)
sadness_path = os.path.join('graphics', 'sadness.png')
sadness = cv2.imread(sadness_path)
surprise_path = os.path.join('graphics', 'surprise.png')
surprise = cv2.imread(surprise_path)
anxious_path = os.path.join('graphics', 'anxious.png')
anxious = cv2.imread(anxious_path)

# Open the mp4 video
video_mp4_path = os.path.join('video.mp4')
cap = cv2.VideoCapture(video_mp4_path)

for i in range (len(emo_json)):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Visualize result on frame
    i = str(i)
    last_result = emo_json[i]
    vis_frame = visualize_result(frame, last_result, i)

    # Display the resulting frame
    cv2.imshow('video', frame)

    # Wait 50ms for any key pressed. Stops system if 'q' was pressed
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
    time.sleep(0.05)

# Release webcam
cap.release()
print('Webcam capture released')