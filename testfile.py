import numpy as np
import cv2 as cv

binaryImage = np.array(cv.imread('binary.png', 0),dtype=np.uint8);
staticImage = np.array(cv.imread('img1.jpg', 0),dtype=np.uint8);
objectImage = np.array(cv.imread('img2.jpg', 0),dtype=np.uint8);
multipliedImage = np.multiply(staticImage,binaryImage);

cv.imshow('Multiplied',multipliedImage)
cap = cv.VideoCapture('video1.avi')
cap.set(cv.cv.CV_CAP_PROP_FRAME_WIDTH, 857)
cap.set(cv.cv.CV_CAP_PROP_FRAME_HEIGHT, 701)
while (1):

    _, frame = cap.read()
    frame=     cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.resize(frame, (857, 701))

    frameArray = np.array(frame);
    frameArray=frameArray-multipliedImage;
    newImage = frameArray*binaryImage;
    cv.imshow('Output', newImage)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
cap.release()





