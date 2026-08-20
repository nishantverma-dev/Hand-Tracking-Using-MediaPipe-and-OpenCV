Hand Tracking Using MediaPipe and OpenCV
Overview
This small project demonstrates real-time hand tracking using MediaPipe and OpenCV. It detects up to two hands from the webcam feed, draws 21 landmarks per hand and connecting lines, and displays the total number of detected hands on-screen.

Aim
To develop a hand tracking system that detects and tracks hand landmarks in real time using MediaPipe and OpenCV.

Features
Real-time hand tracking
Detection of up to two hands
21 landmarks per hand
Landmark connections drawn on the image
Webcam-based input (mirrored view)
Hands detected counter
Easy Q-key exit
Technologies Used
Python
OpenCV
MediaPipe
How It Works
Pipeline:

Webcam → OpenCV captures frame → BGR to RGB conversion → MediaPipe Hand Landmarker → Detect 21 hand landmarks → Draw landmarks and connections → Display output

Implementation notes:

The script supports both mp.solutions.hands (no extra model file) and the MediaPipe Tasks API (hand_landmarker.task). The code automatically selects the available API.
If the Tasks API is used, you must download the hand_landmarker.task model and place it in this project folder.
Note: This workspace already contains a hand_landmarker.task file in the original experiment5/ folder. If you prefer to use the standalone experiment5-hand-tracking folder, copy that file into this folder so the Tasks API branch can run:

copy ..\experiment5\hand_landmarker.task .
Project Structure
experiment5-hand-tracking/
├── exp5.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── hand_tracking_output.png
Installation (Windows / VS Code)
Create a virtual environment and activate it (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Install requirements:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
(Optional) If the script reports that hand_landmarker.task is missing and your MediaPipe expects the Tasks API, download the official model and place it in this folder. See MediaPipe docs for the correct model release for your mediapipe version: https://developers.google.com/mediapipe
Run the Project
From the project folder run:

python exp5.py
Controls

Press Q to exit the program and close the webcam.
Hand Landmarks (major points)
0 Wrist
4 Thumb tip
8 Index finger tip
12 Middle finger tip
16 Ring finger tip
20 Pinky tip
MediaPipe detects 21 landmarks per hand (indexed 0..20). The script draws circles for each landmark and lines for common anatomical connections.

Applications
Gesture recognition
Sign language recognition
Virtual mouse / pointer
Human-computer interaction
Augmented reality overlays
Sample Output
Place a screenshot named hand_tracking_output.png in the screenshots/ folder. A placeholder file is included.

Viva Questions (with short answers)
Q: What is MediaPipe? A: A cross-platform library by Google for building perception pipelines (hands, face, pose, etc.).
Q: What does OpenCV provide here? A: Webcam capture and image display/manipulation utilities.
Q: How many landmarks per hand are detected? A: 21 landmarks per hand.
Q: Why convert BGR to RGB? A: MediaPipe expects images in RGB color order while OpenCV reads frames in BGR.
Q: How is the webcam view presented (mirrored or not)? A: The script shows a mirrored view using cv2.flip(frame, 1).
Q: What is max_num_hands / num_hands used for? A: It limits the number of hands MediaPipe will detect (the script uses 2).
Q: What is HAND_CONNECTIONS? A: A list of index pairs that define which landmarks should be connected with lines.
Q: What is detection confidence? A: A threshold to consider a detection valid (usually between 0 and 1).
Q: How do you stop the program? A: Press Q — the code releases the camera and closes windows.
Q: What are common applications of hand landmarks? A: Gesture control, sign language, AR filters, input devices.
Q: What is FPS and why might it matter? A: Frames per second — higher FPS yields smoother tracking but requires more CPU.
Q: Where do you put hand_landmarker.task if required? A: In the same folder as exp5.py (project root).
Q: What does min_detection_confidence do? A: Controls the detection threshold; higher value reduces false positives.
Q: What happens if the webcam is not available? A: The script prints an error and exits gracefully.
Result
The hand tracking system is implemented using MediaPipe and OpenCV to detect and display hand landmarks in real time.

