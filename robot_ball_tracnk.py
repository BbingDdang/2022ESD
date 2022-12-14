import cv2
import numpy as np
import serial
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#통신
with serial.Serial('/dev/ttyUSB0', 56700, timeout=3) as ser:
    

    while True:
        
        line = [0, 0, 0, 0, 0, 0]
        retval, frame = cap.read()
        if not retval:
            break

        frame2 = frame.copy()
        #화면5분할
        frame_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        blr = cv2.GaussianBlur(frame_gray, (5, 5), 0)
        # roi1
        x1 = 0
        y1 = 0
        w1 = 426
        h1 = 350
        roi1 = blr[y1:y1 + h1, x1:x1 + w1]
        #roi11
        x11 = 0
        y11 = 350
        w11 = 426
        h11 = 720
        roi11 = blr[y11:y11 + h11, x11:x11 + w11]
        # roi2
        x2 = 426
        y2 = 0
        w2 = 852
        h2 = 720
        roi2 = blr[y2:y2 + h2, x2:x2 + w2]
        # roi3
        x3 = 852
        y3 = 0
        w3 = 1280
        h3 = 350
        roi3 = blr[y3:y3 + h3, x3:x3 + w3]
        # roi13
        x13 = 852
        y13 = 350
        w13 = 1280
        h13 = 720
        roi13 = blr[y13:y13 + h13, x13:x13 + w13]
        # cv2.imshow('frame', frame)
        #받은값 로봇으로 
        circles1 = cv2.HoughCircles(roi1, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
        if circles1 is not None:
            for i in circles1[0]:
                print(1)
                s=3
                i = i.astype(int)
                cx, cy, radius = i
                cv2.circle(roi1, (cx, cy), radius, (0, 0, 255), 5)
                
                b = [b'\xff', b'U', bytes([s]), bytes([255-s]), b'\x00', b'\xff']
                for i in range(1):
                    for item in b:
                        ser.write(item)
                time.sleep(0.5)

        circles11 = cv2.HoughCircles(roi11, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=35, minRadius=80, maxRadius=150)
        if circles11 is not None:
            for i in circles11[0]:
                print(11)
                s=13
                i = i.astype(int)
                cx, cy, radius = i
                cv2.circle(roi11, (cx, cy), radius, (0, 0, 255), 5)
                
                b = [b'\xff', b'U', bytes([s]), bytes([255-s]), b'\x00', b'\xff']
                for i in range(1):
                    for item in b:
                        ser.write(item)
                time.sleep(0.5)

        circles2 = cv2.HoughCircles(roi2, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=35, minRadius=80, maxRadius=150)
        if circles2 is not None:
            for i in circles2[0]:
                print(22)
                s=2
                i = i.astype(int)
                cx, cy, radius = i
                cv2.circle(roi2, (cx, cy), radius, (0, 0, 255), 5)
                b = [b'\xff', b'U', bytes([s]), bytes([255-s]), b'\x00', b'\xff']
                #for i in range(1):
                 #   for item in b:
                  #      ser.write(item)S
                time.sleep(0.5)

        circles3 = cv2.HoughCircles(roi3, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=30, minRadius=80, maxRadius=150)
        if circles3 is not None:
            for i in circles3[0]:
                print(3)
                s=4
                i = i.astype(int)
                cx, cy, radius = i
                cv2.circle(roi3, (cx, cy), radius, (0, 0, 255), 5)
                b = [b'\xff', b'U', bytes([s]), bytes([255-s]), b'\x00', b'\xff']
                for i in range(1):
                    for item in b:
                        ser.write(item)
                time.sleep(0.5)
        
        circles13 = cv2.HoughCircles(roi13, cv2.HOUGH_GRADIENT, 1, 20, param1=250, param2=35, minRadius=80, maxRadius=150)
        if circles13 is not None:
            for i in circles13[0]:
                print(33)
                s=14
                i = i.astype(int)
                cx, cy, radius = i
                cv2.circle(roi13, (cx, cy), radius, (0, 0, 255), 5)
                b = [b'\xff', b'U', bytes([s]), bytes([255-s]), b'\x00', b'\xff']
                for i in range(1):
                    for item in b:
                        ser.write(item)
                time.sleep(0.5)
        
        cv2.imshow('original', blr)
        
        cv2.imshow('roi1',roi1)
        cv2.imshow('roi3',roi3)
        cv2.imshow('roi11',roi11)
        cv2.imshow('roi13',roi13)

        key = cv2.waitKey(25)
        if key == 27:
            break

if cap.isOpened():
    cap.release()
    cv2.destroyAllWindows()
