import cv2
import numpy as np

#a = 1

#for i in cv2:

    #if "COLOR" in i:

       #print(a,"= ",i)
       #a += 1


cap = cv2.VideoCapture(0)

def nothing(X):
    
    pass

cv2.namedWindow("frame")

cv2.createTrackbar("h1","frame",0,359,nothing)
cv2.createTrackbar("h2","frame",0,359,nothing)
cv2.createTrackbar("s1","frame",0,255,nothing)
cv2.createTrackbar("s2","frame",0,255,nothing)
cv2.createTrackbar("v1","frame",0,255,nothing)
cv2.createTrackbar("v2","frame",0,255,nothing)

while cap.isOpened():

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h1 = cv2.getTrackbarPos("h1","frame") / 2
    h2 = cv2.getTrackbarPos("h2","frame") / 2
    s1 = cv2.getTrackbarPos("s1","frame")
    s2 = cv2.getTrackbarPos("s2","frame")
    v1 = cv2.getTrackbarPos("v1","frame")
    v2 = cv2.getTrackbarPos("v2","frame")

    lower = np.array([h1,s2,v1])
    upper = np.array([h2,s2,v2])

    mask = cv2.inRange(hsv,lower,upper)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    if cv2.waitKey() & 0xFF == ord("q"): break


cv2.destroyAllWindows()