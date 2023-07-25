import cv2
import time

def kare_ciz(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeft_clicked == True and botRight_clicked == True:
            topLeft_clicked = False
            botRight_clicked = False
            pt1 = (0, 0)
            pt2 = (0, 0)

        if topLeft_clicked == False:
            pt1 = (x, y)
            topLeft_clicked = True

        elif botRight_clicked == False:
            pt2 = (x, y)
            botRight_clicked = True


pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FPS hesaplamak için değişkenler
fps_count = 0
start_time = time.time()
fps = 0

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', kare_ciz)

while True:
    ret, frame = cap.read()

    if topLeft_clicked == True:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeft_clicked == True and botRight_clicked == True:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)

    # FPS hesaplama
    fps_count += 1
    elapsed_time = time.time() - start_time

    if elapsed_time > 1:
        fps = fps_count / elapsed_time
        fps_count = 0
        start_time = time.time()

    # FPS değerini ekrana yazdırma
    fps_text = f"FPS: {round(fps, 2)}"
    cv2.putText(frame, fps_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

