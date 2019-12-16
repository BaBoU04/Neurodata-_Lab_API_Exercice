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

    return image

# Json file path
json_file_path = os.path.join('ndlapi_results', 'video1111.mp4_FaceDetector_result.json')
json_file = os.path.join(json_file_path)

# Open and load json file
with open(json_file) as json_data:
    json_file = json.load(json_data)

# Open the mp4 video
video1111_mp4 = os.path.join('video1111.mp4')
cap = cv2.VideoCapture(video1111_mp4)

for i in range (len(json_file)):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Visualize result on frame
    i = str(i)
    last_result = json_file[i]
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