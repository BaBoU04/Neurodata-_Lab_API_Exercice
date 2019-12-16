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

        # Write emotions on image
        yscale = 138
        for emotion in res[k]['emotions']:
            emotext = emotion[1]
            score = int(emotion[0]*10000)/100
            text = emotext + str(score) + '%'
            cv2.putText(img=image, text=text, org=(x, y-yscale),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7,
                    color=(0, 255, 0))
            yscale -= 23

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