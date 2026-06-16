# visualization.py

import cv2


def draw_detection(
    bbox,
    frame,
    conf, person_id
):

    x1, y1, x2, y2 = bbox

    # Green detection box
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    # Label
    text = (
        f"{person_id}: Person {conf:.2f}"
    )

    cv2.putText(
        frame,
        text,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )


def draw_surveillance(
    bbox,
    frame
):

    x1, y1, x2, y2 = bbox

    # Alert text
    cv2.putText(
        frame,
        "SUSPICIOUS ACTIVITY",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    # Red alert box
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        (0, 0, 255),
        3
    )