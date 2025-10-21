import cv2

cap = cv2.VideoCapture("C:/Users/rafae/Desktop/UTFPR/Extensão/IC/Esportes Python/Proposta-de-IC/Passes cortados/24-1.mp4")

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()
else:
    print("Vídeo aberto com sucesso.")

ret, frame = cap.read()

if ret:
    cv2.imshow("Primeiro Frame", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erro ao ler o primeiro frame do vídeo.")

cap.release()