# state_manager.py

class StateManager:

    def __init__(self):

        # Stores tracked people
        self.tracked_people = {}

    def update_person(

        self,
        person_id,
        current_time,
        detected

    ):

        # New person
        if person_id not in self.tracked_people:

            self.tracked_people[
                person_id
            ] = {

                "first_seen_time":
                current_time,

                "last_seen_time":
                current_time,

                "alert_triggered":
                False

            }

        # Existing person
        else:

            self.tracked_people[
                person_id
            ][
                "last_seen_time"
            ] = current_time

        return self.tracked_people[
            person_id
        ]

    def remove_person(
        self,
        person_id
    ):

        if (
            person_id
            in self.tracked_people
        ):

            del self.tracked_people[
                person_id
            ]