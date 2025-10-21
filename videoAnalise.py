import cv2

cap = cv2.VideoCapture("C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python/Proposta-de-IC/Passes cortados/24-1.mp4")

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()
else:
    print("Vídeo aberto com sucesso.")

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Número total de frames: {frame_count}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro ao ler o frame.")
        break

    cv2.imshow("Frame do Vídeo", frame)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()