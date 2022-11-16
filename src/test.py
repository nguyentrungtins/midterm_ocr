import cv2 as cv
import numpy as np

def nothing(x):pass

cap = cv.VideoCapture(0)
cv.namedWindow('videoUI', cv.WINDOW_NORMAL)
cv.createTrackbar('T','videoUI',0,255,nothing)

while(True):
    img = cv.imread("src/image.png")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, frame = cap.read()
    thresh = cv.getTrackbarPos('T','videoUI')
    vid_bw = cv.threshold(gray, thresh, 255, cv.THRESH_BINARY_INV)[1]

    cv.imshow('videoUI',cv.flip(vid_bw,1))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()