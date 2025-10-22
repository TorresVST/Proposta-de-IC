import cv2
from ultralytics import YOLO

model = YOLO('yolov8x.pt')

BALL_CLASS_ID = 32

cap = cv2.VideoCapture("C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python/Proposta-de-IC/Passes cortados/17.mp4")
if not cap.isOpened():
    print("Erro ao abrir o vídeo."); exit()

fps = cap.get(cv2.CAP_PROP_FPS)
scale = 0.5  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[BALL_CLASS_ID],
        conf=0.1,  
        iou=0.5    
    )

    if results[0].boxes is not None and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            label = f'ID: {track_id}'
            cv2.putText(
                frame, 
                label, 
                (x1, y1 - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, 
                (0, 0, 255), 
                2
            )

    resized = cv2.resize(frame, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    cv2.imshow("Video", resized)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
