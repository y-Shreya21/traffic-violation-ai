from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=50, n_init=3)

def track_objects(detections, frame):
    tracks = tracker.update_tracks(detections, frame=frame)

    tracked_objects = []

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = track.to_ltrb()

        tracked_objects.append({
            "id": track_id,
            "bbox": (int(l), int(t), int(w), int(h))
        })

    return tracked_objects