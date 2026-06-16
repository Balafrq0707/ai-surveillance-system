# ai-surveillance-system
Real-time AI surveillance system using YOLOv8, custom multi-object tracking, and loitering detection.
## Project Overview

This project implements a real-time AI-powered surveillance system capable of detecting, tracking, and monitoring individuals in video streams.

The system uses YOLOv8 for person detection and a custom centroid-based multi-object tracker to assign persistent IDs to individuals across video frames. It further incorporates loitering detection to identify suspicious behavior when a person remains in the monitored area beyond a configurable threshold.

The project demonstrates key concepts in computer vision, object tracking, state management, and event-driven surveillance systems.

## Features

* Real-time person detection using YOLOv8
* Multi-person tracking with persistent IDs
* Custom centroid-based object tracker
* Missing-frame handling for temporary occlusions
* Automatic cleanup of inactive tracks
* Loitering detection using temporal analysis
* Real-time suspicious activity alerts
* Modular and extensible architecture

## System Architecture

Video Stream
      ↓
YOLOv8 Detection
      ↓
Centroid Tracker
      ↓
State Manager
      ↓
Surveillance Logic
      ↓
Visualization & Alerts

## Project Structure

project/
│
├── main.py
├── detection.py
├── tracker.py
├── state_manager.py
├── surveillance.py
├── visualization.py
│
├── videos/
├── models/
└── README.md

## Tracking Strategy

The system employs a custom centroid-based multi-object tracker.

For each detected person:

1. Compute the centroid of the bounding box.
2. Compare it against existing tracked centroids using Euclidean distance.
3. Match the detection to the nearest track within a configurable threshold.
4. Update the matched track's position and timestamp.
5. Create a new track if no suitable match exists.

To improve robustness against temporary detector failures and occlusions, tracks maintain a missing-frame counter before being removed.

## Surveillance Logic

Person Detected
      ↓
Assign Tracking ID
      ↓
Update Person State
      ↓
Compute Time in Scene
      ↓
Loitering Threshold Exceeded?
      ↓
Generate Alert

## Challenges Faced

- Frequent ID switching during crowd crossings.
- Occlusions causing temporary tracking failures.
- Selecting an optimal centroid matching threshold.
- Preserving identities across missed detections.
- Balancing track persistence with false matches.

## Future Improvements

- Kalman Filter integration
- DeepSORT or ByteTrack support
- Crowd density estimation
- Restricted zone intrusion detection
- Heatmap generation
- Multi-camera tracking
- Web dashboard for monitoring

  ## Technologies Used

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Computer Vision
- Object Tracking
