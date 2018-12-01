import cv2
import numpy as np
cam = cv2.VideoCapture('data.mp4');

id=raw_input('enter user id')
sampleNumber = 0;

while(True):
    ret,img=cam.read();
    sampleNumber=sampleNumber+1
    cv2.imwrite("User"+str(id)+"."+str(sampleNumber)+".jpg",img);
    print "Writing Images"


cam.release()
cv2.destroyAllWindows()