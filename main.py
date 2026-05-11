import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Não foi possível abrir a webcam.")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        print("Erro ao capturar frame.")
        break

    cv2.imshow("CubeAnalyzer", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()