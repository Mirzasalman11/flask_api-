from flask import Flask,request,Response
from main import LaneDetectionAPI
import cv2
import numpy as np


app = Flask(__name__)


@app.route('/both',methods=['POST'])

def both():
    # Check if the POST request contains a file named 'video'
    if 'video' not in request.files:
        return "No video found in the request", 400

    video_file = request.files['video']
 
    # Convert the video data to OpenCV format
    nparr = np.frombuffer(video_file.read(), np.uint8)
    source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the received video stream 
    api = LaneDetectionAPI(video_path=source)
    both=api.process_video()

    # Here, we encode it back into JPEG for simplicity
    ret, buffer = cv2.imencode('.jpg', both)
    processed_data = buffer.tobytes()
    
    # Return the processed video data back to the mobile app
    return Response(processed_data, mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/line_detect', methods=['POST'])

def line():
    # Check if the POST request contains a file named 'video'
    if 'video' not in request.files:
        return "No video found in the request", 400

    video_file = request.files['video']

    # Convert the video data to OpenCV format
    nparr = np.frombuffer(video_file.read(), np.uint8)
    source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the received video stream 
    api = LaneDetectionAPI(video_path=source)
    line=api.line()

    # Here, we encode it back into JPEG for simplicity
    ret, buffer = cv2.imencode('.jpg', line)
    processed_data = buffer.tobytes()
    
    # Return the processed video data back to the mobile app
    return Response(processed_data, mimetype='multipart/x-mixed-replace; boundary=frame')


    
@app.route('/sign_detect', methods=['POST'])

def sign_detect():
    # Check if the POST request contains a file named 'video'
    if 'video' not in request.files:
        return "No video found in the request", 400

    video_file = request.files['video']

    # Convert the video data to OpenCV format
    nparr = np.frombuffer(video_file.read(), np.uint8)
    source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    
    # Process the received video stream 
    api = LaneDetectionAPI(video_path=source)
    sin=api.sign_detect()

    # Here, we encode it back into JPEG for simplicity
    ret, buffer = cv2.imencode('.jpg', sin)
    processed_data = buffer.tobytes()
    
    # Return the processed video data back to the mobile app
    return Response(processed_data, mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



