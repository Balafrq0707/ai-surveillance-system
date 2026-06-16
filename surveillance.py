# surveillance.py

ALERT_THRESHOLD = 3


def surveillance_system(person_state):

    first_seen_time = (
        person_state[
            "first_seen_time"
        ]
    )

    last_seen_time = (
        person_state[
            "last_seen_time"
        ]
    )

    elapsed_time = (
        last_seen_time
        - first_seen_time
    )

    # Trigger alert
    if elapsed_time > ALERT_THRESHOLD:

        person_state[
            "alert_triggered"
        ] = True

    return person_state[
        "alert_triggered"
    ]