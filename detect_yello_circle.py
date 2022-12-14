
import cv2
import time
import numpy as np

cap=cv2.VideoCapture(0)
time.sleep(1)
hsv_lower = np.array([30, 20, 80])
hsv_upper = np.array([62, 255, 255])
while cap.isOpened():
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(frame, hsv_lower, hsv_upper)
    result = cv2.bitwise_and(frame, frame, mask=img_mask)

    gray = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 40, maxRadius = 150)
    try:
        for i in circles[0]:
            cv2.circle(frame, (int(i[0]), int(i[1])), int(i[2]), (255,255,255), 5)
            print("center x : ", int(i[0]), "center y : ", int(i[1]), "radius : ", int(i[2]))
            break
        cv2.rectangle(frame,(640//2-30,480//2-30),
                     (640//2+30,480//2+30),
                      (255,255,255),3)
    except:
        pass

    cv2.imshow('img',frame)
    cv2.imshow('mask', result)

    if cv2.waitKey(10)&0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
