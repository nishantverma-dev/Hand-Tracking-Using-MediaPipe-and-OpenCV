"""
Experiment 5 - Hand Tracking Using MediaPipe and OpenCV

This script supports two MediaPipe APIs depending on the installed
MediaPipe version:
 - If `mp.solutions.hands` is available it uses that (no external model file).
 - Otherwise it uses the MediaPipe Tasks API and requires a
   `hand_landmarker.task` file in the same folder.

Features:
 - Real-time webcam capture (mirrored view)
 - Detect up to two hands
 - Draw 21 landmarks per hand and connections
 - Display number of detected hands
 - Press 'Q' to quit cleanly

Keep the implementation readable for viva explanation.
"""

import os
import sys
import cv2

try:
    import mediapipe as mp
except Exception as e:
    print("ERROR: mediapipe is not installed. Install with: python -m pip install mediapipe")
    raise


HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17)
]


def draw_landmarks_opencv(frame, landmark_points):
    """Draw landmarks and connections on the BGR `frame`.

    landmark_points: list of (x, y) tuples in pixel coordinates.
    """
    # Draw points
    for (x, y) in landmark_points:
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Draw connections
    for start, end in HAND_CONNECTIONS:
        if start < len(landmark_points) and end < len(landmark_points):
            cv2.line(frame, landmark_points[start], landmark_points[end], (255, 0, 0), 2)


def main():
    # Open webcam (device 0)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("ERROR: Cannot open webcam. Check camera and permissions.")
        sys.exit(1)

    # Choose API: prefer mp.solutions.hands when available (no model file needed)
    use_solutions_hands = hasattr(mp, "solutions") and hasattr(mp.solutions, "hands")

    model_path = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")

    if not use_solutions_hands:
        # Tasks API branch requires the model file
        if not os.path.exists(model_path):
            print("ERROR: hand_landmarker.task model not found.")
            print("If your MediaPipe installation uses the Tasks API, download the official")
            print("MediaPipe `hand_landmarker.task` model and place it in this folder:")
            print(f"  {os.path.dirname(__file__)}")
            cap.release()
            sys.exit(1)

    try:
        print("================================")
        print("   HAND TRACKING STARTED")
        print("================================")
        print("Press Q to exit")

        if use_solutions_hands:
            # Using mp.solutions.hands (no external model)
            with mp.solutions.hands.Hands(
                static_image_mode=False,
                max_num_hands=2,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            ) as hands:

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        print("ERROR: Unable to read from webcam.")
                        break

                    # Mirror view
                    frame = cv2.flip(frame, 1)

                    # Convert BGR to RGB
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Process frame
                    results = hands.process(rgb)

                    hand_count = 0
                    if results.multi_hand_landmarks:
                        hand_count = len(results.multi_hand_landmarks)
                        h, w, _ = frame.shape
                        for hand_landmarks in results.multi_hand_landmarks:
                            points = []
                            for lm in hand_landmarks.landmark:
                                x_px = int(lm.x * w)
                                y_px = int(lm.y * h)
                                points.append((x_px, y_px))

                            draw_landmarks_opencv(frame, points)

                    # Overlay status text and show
                    cv2.putText(frame, f"Hands Detected: {hand_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                    cv2.putText(frame, "Press Q to Exit", (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.imshow("Experiment 5 - Hand Tracking", frame)

                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        print("Exiting on user request")
                        break

        else:
            # Using MediaPipe Tasks API (Hand Landmarker)
            BaseOptions = mp.tasks.BaseOptions
            HandLandmarker = mp.tasks.vision.HandLandmarker
            HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
            VisionRunningMode = mp.tasks.vision.RunningMode

            options = HandLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=model_path),
                running_mode=VisionRunningMode.IMAGE,
                num_hands=2,
                min_hand_presence_confidence=0.5,
                min_hand_detection_confidence=0.5,
                min_tracking_confidence=0.5,
            )

            with HandLandmarker.create_from_options(options) as landmarker:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        print("ERROR: Unable to read from webcam.")
                        break

                    frame = cv2.flip(frame, 1)
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

                    result = landmarker.detect(mp_image)

                    hand_count = 0
                    if result.hand_landmarks:
                        hand_count = len(result.hand_landmarks)
                        h, w, _ = frame.shape
                        for hand in result.hand_landmarks:
                            points = []
                            for lm in hand:
                                x_px = int(lm.x * w)
                                y_px = int(lm.y * h)
                                points.append((x_px, y_px))

                            draw_landmarks_opencv(frame, points)

                    cv2.putText(frame, f"Hands Detected: {hand_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                    cv2.putText(frame, "Press Q to Exit", (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.imshow("Experiment 5 - Hand Tracking", frame)

                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        print("Exiting on user request")
                        break

    except Exception as ex:
        print("An unexpected error occurred:", ex)
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Hand Tracking Stopped.")


if __name__ == "__main__":
    main()
