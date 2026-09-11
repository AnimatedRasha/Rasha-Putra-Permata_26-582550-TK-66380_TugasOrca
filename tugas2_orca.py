class MissionManager:
    def __init__(self):
        self.state = "IDLE"

    def update_status(self, object_name, confidence, distance):
        if confidence < 0.70:
            self.state = "SEARCHING"
            action = "SEARCH TARGET"
        elif distance > 2.0:
            self.state = "DETECTED"
            action = "APPROACH TARGET"
        elif distance > 0.5:
            self.state = "APPROACHING"
            action = "CLOSING IN"
        else:
            self.state = "MISSION_COMPLETE"
            action = "TARGET REACHED"

        print(f"Object detected : {object_name}")
        print(f"Confidence : {confidence}")
        print(f"Distance : {distance} m")
        print()
        print(f"Mission State : {self.state}")
        print(f"Action : {action}")

obj = input().replace("INPUT Object : ", "").strip()
conf = float(input().replace("Confidence: ", "").strip())
dist = float(input().replace("Distance : ", "").strip())

manager = MissionManager()
manager.update_status(obj, conf, dist)