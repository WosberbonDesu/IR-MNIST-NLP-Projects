import cv2
import numpy as np

img = cv2.read("image.jpg")

print(img.shape)

rows,cols = img.shape[:2]

click_count = 0
a = []

dst_point = np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]])

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.namedWindow("output",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):

    global click_count,a

    if click_count < 4:

        if event == cv2.EVENT_LBUTTONDBLCLK:

            print(x,y)
            print("Click Num",click_count)
            click_count += 1
            a.append((x,y))

    else:

        

        src = np.float32([
            [a[0][0],[0][1]],
            [a[1][0],[1][1]],
            [a[2][0],[2][1]],
            [a[3][0],[3][1]]])

        click_count = 0

        a = []

        m = cv2.getPerspectiveTransform(src,dst_point)
        img_output = cv2.warpPerspective(img,m,(cols,rows))
        cv2.imshow("output",img_output)

    # print(x,y)
    pass



cv2.setMouseCallback("img",draw)
while(1):
    cv2.imshow("img",img)

    # cv2.imshow("img_output",img_output)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cv2.destroyAllWindows()







