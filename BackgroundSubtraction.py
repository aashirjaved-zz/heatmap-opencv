import numpy as np
import cv2
cap = cv2.VideoCapture('data.mp4')
fgbg = cv2.createBackgroundSubtractorKNN()
fgb = cv2.createBackgroundSubtractorMOG2(varThreshold=800, detectShadows=False)
fg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmas = fgb.apply(frame)
    fgma = fg.apply(frame)
    cv2.imshow('frame',fgmask)
    cv2.imshow('frame1',fgmas)
    cv2.imshow('frame2',fgma)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()