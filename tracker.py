# tracker.py
import math

THRESHOLD = 70

CLEANUP_THRESHOLD = 15


class Tracker:

    def __init__(self):

        self.tracked_objects = {}
        self.next_id = 1

    def assign_ID(self, bbox, current_time):

        matches = []

        x1, y1, x2, y2 = bbox

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        c = (cx, cy)

        # First object
        if not self.tracked_objects:

            object_id = f"T{self.next_id}"

            self.tracked_objects[object_id] = {

                "centroid" : c, 
                "last_seen_time" : current_time, 
                "matched" : True, 
                "missing_frames": 0
       }

            self.next_id += 1

            return object_id

        # Compare with tracked objects
        for object_id, data in self.tracked_objects.items():

            print("\nTracked Objects:")

            centroid = data["centroid"]

            distance = math.dist(c, centroid)

            if distance <= THRESHOLD:

                matches.append((object_id, distance))

                
        # Existing object
        if matches:

            print(f"Detection centroid={c}")

            print(f"Matches={matches}")

            closest = min(matches, key=lambda x: x[1])

            closest_id = closest[0]

            # Update coordinate
            self.tracked_objects[closest_id]["centroid"] = c
            self.tracked_objects[closest_id]["last_seen_time"] = current_time
            self.tracked_objects[closest_id]["matched"] = True
            self.tracked_objects[closest_id]["missing_frames"] = 0

            print(f"Matched with {closest_id}")

            return closest_id
            

        # New object
        else:

            object_id = f"T{self.next_id}"

            self.tracked_objects[object_id] = {

                "centroid" : c, 
                "last_seen_time" : current_time, 
                "matched" : True, 
                "missing_frames": 0
            }


            self.next_id += 1

            print(f"Created {object_id}")

            return object_id
        
    def update_missing_tracks(self):

        inactive_tracks = []

        for object_id, data in self.tracked_objects.items():

            if data["matched"] == False:

                data["missing_frames"] += 1

                missing_frames = data["missing_frames"]

                if missing_frames > 5:

                    inactive_tracks.append(object_id)

            elif data["matched"] == True:

                data["missing_frames"] = 0

        for object_id in inactive_tracks: 

            del self.tracked_objects[object_id]


    def reset_matches(self):

        for object_id, data in self.tracked_objects.items():

            data["matched"] = False

