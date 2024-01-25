import cv2
import requests
import numpy as np

def capture_and_send_video():
    cap = cv2.VideoCapture(0)  # Access the mobile camera, 0 for default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, img_encoded = cv2.imencode('.jpg', frame)

        url = 'http://127.0.0.1:5000/line_detect'  # Replace with your Flask server endpoint
        files = {'video': ('video_feed.jpg', img_encoded.tobytes())}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            received_frame = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('Received Stream', received_frame)
        
        # Press 'q' to quit the streaming window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Call the function to continuously capture and send the video stream
capture_and_send_video()
