Hand Tracking Using MediaPipe and OpenCV
Experiment 5 – Computer Vision Laboratory

A real-time hand tracking system implemented using Python, OpenCV, and MediaPipe. The application captures video from a webcam, detects human hands, identifies 21 hand landmarks for each detected hand, and displays the landmarks and their connections in real time.

Aim

To develop a real-time hand tracking system that detects and tracks hand landmarks using MediaPipe and OpenCV.

Objectives
To understand the concept of real-time hand tracking.
To use OpenCV for webcam video capture and image processing.
To use MediaPipe Hand Landmarker for hand detection.
To detect 21 landmarks on each hand.
To visualize hand landmarks and their connections.
To track multiple hands in real time.
To understand applications of hand tracking in computer vision.
Technologies Used
Technology	Purpose
Python	Programming language
OpenCV	Webcam capture and image processing
MediaPipe	Hand detection and landmark tracking
VS Code	Development environment
Features
Real-time hand detection using a webcam.
Detection of up to two hands simultaneously.
Detection of 21 landmarks for each hand.
Visualization of hand landmarks.
Visualization of connections between landmarks.
Displays the number of detected hands.
Mirror-style webcam display.
Simple keyboard control to exit the application.
How It Works
Webcam
   ↓
OpenCV Video Capture
   ↓
Frame Acquisition
   ↓
BGR → RGB Conversion
   ↓
MediaPipe Hand Landmarker
   ↓
Hand Detection
   ↓
21 Hand Landmark Detection
   ↓
Draw Landmarks and Connections
   ↓
Display Processed Frame
Hand Landmarks

MediaPipe Hand Landmarker detects 21 landmarks for each hand.

ID	Landmark
0	Wrist
1	Thumb CMC
2	Thumb MCP
3	Thumb IP
4	Thumb Tip
5	Index Finger MCP
6	Index Finger PIP
7	Index Finger DIP
8	Index Finger Tip
9	Middle Finger MCP
10	Middle Finger PIP
11	Middle Finger DIP
12	Middle Finger Tip
13	Ring Finger MCP
14	Ring Finger PIP
15	Ring Finger DIP
16	Ring Finger Tip
17	Pinky MCP
18	Pinky PIP
19	Pinky DIP
20	Pinky Tip
Project Structure
hand-tracking-mediapipe-opencv/
│
├── exp5.py
├── hand_landmarker.task
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    └── hand_tracking_output.png
Requirements
Python 3.x
OpenCV
MediaPipe
Working webcam
Visual Studio Code or another Python-compatible IDE
Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd hand-tracking-mediapipe-opencv
2. Create a Virtual Environment

For Windows:

python -m venv .venv

Activate the virtual environment:

.venv\Scripts\Activate.ps1
3. Install Dependencies
python -m pip install -r requirements.txt
MediaPipe Model

The Hand Landmarker API requires the hand_landmarker.task model file.

Download the official MediaPipe Hand Landmarker model and place it in the same directory as exp5.py.

The project should contain:

hand-tracking-mediapipe-opencv/
│
├── exp5.py
├── hand_landmarker.task
└── requirements.txt
Running the Application

Run the following command:

python exp5.py

The webcam will open and the system will start detecting hands.

Press Q to exit the application.

Sample Output

The application displays the webcam feed with detected hand landmarks and their corresponding connections.

Code Workflow
Import the required Python libraries.
Initialize the MediaPipe Hand Landmarker.
Open the system webcam using OpenCV.
Capture frames continuously from the webcam.
Flip the frame horizontally for a mirror view.
Convert the frame from BGR to RGB.
Convert the frame into a MediaPipe image.
Process the image using the Hand Landmarker.
Detect the hands present in the frame.
Extract the 21 landmarks for each detected hand.
Draw landmarks and connections on the frame.
Display the number of detected hands.
Display the processed video.
Exit when the user presses Q.
Release the webcam and close the application.
BGR to RGB Conversion

OpenCV captures images in BGR (Blue, Green, Red) format, whereas MediaPipe expects images in RGB (Red, Green, Blue) format.

Therefore, the captured frame is converted before processing:

rgb_frame = cv2.cvtColor(
    frame,
    cv2.COLOR_BGR2RGB
)
Applications
Gesture Recognition
Sign Language Recognition
Virtual Mouse
Virtual Keyboard
Human-Computer Interaction
Augmented Reality
Gaming Interfaces
Touchless User Interfaces
Robotics Control
Educational Applications
Advantages
Real-time hand tracking.
Contactless interaction.
Supports multiple hands.
Detects detailed hand structure.
Suitable for gesture-based applications.
Can be integrated with other computer vision systems.
Limitations
Performance depends on webcam quality.
Poor lighting can affect hand detection.
Heavily occluded hands may not be detected correctly.
Very fast hand movements can sometimes reduce tracking accuracy.
Performance depends on available system resources.
Viva Questions and Answers
1. What is MediaPipe?

MediaPipe is a framework developed by Google for building real-time computer vision and machine learning applications.

2. What is OpenCV?

OpenCV is an open-source computer vision library used for image and video processing.

3. What is hand tracking?

Hand tracking is the process of detecting a hand and continuously tracking its position and landmarks in images or video.

4. How many landmarks are detected on one hand?

MediaPipe Hand Landmarker detects 21 landmarks on each hand.

5. How many hands can this application detect?

The application is configured to detect up to two hands.

6. Why is OpenCV used?

OpenCV is used to capture webcam frames, process images, draw information, and display the output.

7. Why is MediaPipe used?

MediaPipe is used to detect hands and identify their 21 landmarks.

8. Why is BGR converted to RGB?

OpenCV uses BGR image format, while MediaPipe expects RGB input. Therefore, the frame is converted from BGR to RGB.

9. What is a hand landmark?

A hand landmark is a specific point on the hand, such as the wrist, fingertip, or finger joint.

10. What is landmark 0?

Landmark 0 represents the wrist.

11. What is landmark 4?

Landmark 4 represents the thumb tip.

12. What is landmark 8?

Landmark 8 represents the index finger tip.

13. What is landmark 12?

Landmark 12 represents the middle finger tip.

14. What is landmark 16?

Landmark 16 represents the ring finger tip.

15. What is landmark 20?

Landmark 20 represents the pinky finger tip.

16. What is a webcam?

A webcam is an imaging device used to capture live video.

17. What does cv2.VideoCapture(0) do?

It opens the default webcam for capturing video.

18. Why do we use cv2.flip()?

It horizontally flips the webcam image to provide a mirror-like view.

19. What does cv2.imshow() do?

It displays the processed image or video frame in an OpenCV window.

20. How is the program terminated?

The program terminates when the user presses the Q key.

Result

The hand tracking system was successfully implemented using Python, OpenCV, and MediaPipe. The system captures real-time video through a webcam, detects up to two hands, identifies 21 landmarks on each detected hand, and displays the landmarks and their connections on the video stream.

Future Enhancements

The system can be further extended to implement:

Finger counting.
Hand gesture recognition.
Sign language recognition.
Virtual mouse control.
Virtual keyboard control.
Gesture-based volume control.
Gesture-based presentation control.
Human-computer interaction systems.
Author

Nishant Verma
B.E. Computer Science and Engineering – Artificial Intelligence & Machine Learning
Chandigarh University

License

This project is intended for educational and academic purposes.
