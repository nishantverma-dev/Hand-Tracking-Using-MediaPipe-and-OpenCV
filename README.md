# Hand Tracking Using MediaPipe and OpenCV

## Experiment 5

### Computer Vision Laboratory

A real-time hand tracking system implemented using **Python, OpenCV, and MediaPipe**. The application captures video from a webcam, detects human hands, identifies 21 hand landmarks for each detected hand, and displays the landmarks and their connections in real time.

---

## Aim

To develop a real-time hand tracking system that detects and tracks hand landmarks using **MediaPipe and OpenCV**.

---

## Objectives

- To understand the concept of real-time hand tracking.
- To use OpenCV for webcam video capture and image processing.
- To use MediaPipe Hand Landmarker for hand detection.
- To detect 21 landmarks on each hand.
- To visualize hand landmarks and their connections.
- To track multiple hands in real time.
- To understand the applications of hand tracking in computer vision.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand detection and landmark tracking |
| NumPy | Numerical and image-processing support |
| VS Code | Development environment |

---

## Features

- Real-time hand detection using a webcam.
- Detection of up to two hands simultaneously.
- Detection of 21 landmarks for each hand.
- Visualization of hand landmarks.
- Visualization of connections between landmarks.
- Displays the number of detected hands.
- Mirror-style webcam display.
- Simple keyboard control to exit the application.

---

## How It Works

The system follows the following processing pipeline:

```text
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

