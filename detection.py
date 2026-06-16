# detection.py

PERSON_CLASS_ID = 0
CONFIDENCE_THRESHOLD = 0.5


def detect_people(model, frame):

    detections = []

    # Run YOLO inference
    results = model(frame)

    # Process detections
    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # Detect persons only
            if (
                cls == PERSON_CLASS_ID
                and conf > CONFIDENCE_THRESHOLD
            ):

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                bbox = (
                    x1,
                    y1,
                    x2,
                    y2
                )

                detection = {

                    "bbox": bbox,
                    "conf": conf

                }

                detections.append(
                    detection
                )

    return detections