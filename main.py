# main.py

import cv2
from ultralytics import YOLO

from detection import detect_people
from surveillance import surveillance_system
from visualization import (
    draw_detection,
    draw_surveillance
)
from state_manager import StateManager
from tracker import Tracker


# Load YOLO model
model = YOLO("models/yolov8n.pt")

# Open video
cap = cv2.VideoCapture("videos/CCTV_lobby.mp4")

if not cap.isOpened():
    print("Unable to open video file!")
    exit()

# Create managers
tracker = Tracker()
state_manager = StateManager()

while True:

    ret, frame = cap.read()

    if not ret:
        print("End of video or failed to read frame.")
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # Current timestamp
    current_time = (
        cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
    )

    # -----------------------------------
    # Reset match flags for this frame
    # -----------------------------------
    tracker.reset_matches()

    # -----------------------------------
    # Run detection
    # -----------------------------------
    detections = detect_people(
        model,
        frame
    )

    # -----------------------------------
    # Process detections
    # -----------------------------------
    for detection in detections:

        bbox = detection["bbox"]
        conf = detection["conf"]

        # Assign tracking ID
        person_id = tracker.assign_ID(
            bbox,
            current_time
        )

        # Draw detection
        draw_detection(
            bbox,
            frame,
            conf,
            person_id
        )

        # Update state
        person_state = (
            state_manager.update_person(
                person_id,
                current_time,
                detected=True
            )
        )

        # Surveillance logic
        alert_triggered = (
            surveillance_system(
                person_state
            )
        )

        # Draw alert
        if alert_triggered:

            draw_surveillance(
                bbox,
                frame
            )

    # -----------------------------------
    # Update missing tracks
    # -----------------------------------
    tracker.update_missing_tracks()

    # -----------------------------------
    # Debug output
    # -----------------------------------
    print("\nTracked Objects:")
    print(tracker.tracked_objects)

    # -----------------------------------
    # Show frame
    # -----------------------------------
    cv2.imshow(
        "AI Surveillance System",
        frame
    )

    # Exit on Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()