import cv2

cap = cv2.VideoCapture("C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python/Proposta-de-IC/Passes cortados/24-1.mp4")
if not cap.isOpened():
    print("Erro ao abrir o vídeo."); exit()

fps = cap.get(cv2.CAP_PROP_FPS)
scale = 0.5  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized = cv2.resize(frame, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    cv2.imshow("Video", resized)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
