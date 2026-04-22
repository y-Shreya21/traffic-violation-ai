import sys
import os
import cv2
from ultralytics import YOLO
# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tracking.tracker import track_objects

# Load model
model = YOLO("yolov8n.pt")

# Vehicle classes
vehicle_classes = [2, 3, 5, 7]

# Overlap function
def is_overlapping(box1, box2):
    x1, y1, x2, y2 = box1
    x1_p, y1_p, x2_p, y2_p = box2

    return not (x2 < x1_p or x2_p < x1 or y2 < y1_p or y2_p < y1)

def is_near(bike, person):
    x1, y1, x2, y2 = bike
    px1, py1, px2, py2 = person

    # bike center
    bike_cx = (x1 + x2) // 2

    # person center
    person_cx = (px1 + px2) // 2
    person_cy = (py1 + py2) // 2

    # 🔥 conditions
    horizontal_close = abs(bike_cx - person_cx) < 80

    # person should be in upper half of bike
    vertical_position = y1 < person_cy < (y1 + y2)

    return horizontal_close and vertical_position

# 📁 Video folder
video_folder = "dataset/videos"

video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

for video_file in video_files:

    video_path = os.path.join(video_folder, video_file)
    print(f"Processing: {video_file}")

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (1280, 720))

        results = model(frame)

        # Reset every frame
        persons = []
        motorcycles = []
        detections = []

        # Class IDs
        person_class = 0
        motorcycle_class = 3

        # Detection
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if conf < 0.5:
                    continue

                if (x2 - x1) < 40 or (y2 - y1) < 40:
                    continue

                if cls == person_class:
                    persons.append((x1, y1, x2, y2))

                elif cls == motorcycle_class:
                    motorcycles.append((x1, y1, x2, y2))

                if cls in vehicle_classes:
                    detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'vehicle'))

        # Tracking
        tracked_objects = track_objects(detections, frame)

        # 🚨 Triple Riding Detection
        for bike in motorcycles:
            x1, y1, x2, y2 = bike

            people_near = 0

            for person in persons:
                px1, py1, px2, py2 = person

        # relaxed region check
                if px1 > x1 - 60 and px2 < x2 + 60 and py1 < y2 and py2 > y1:
                    people_near += 1

            print("People near:", people_near)

            if people_near >= 1:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.putText(frame, "POSSIBLE TRIPLE RIDING", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Draw tracking
        for obj in tracked_objects:
            x, y, w, h = obj["bbox"]
            track_id = obj["id"]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Traffic Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()