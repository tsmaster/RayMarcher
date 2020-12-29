import cv2
import numpy as np

DRAW_CIRCLES = False

img = cv2.imread("raytest.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

cv2.imwrite('edges.png', edges)

rho = 1 # resolution of r in pixels
theta = np.pi / 720
minIntersections = 100

lines = cv2.HoughLines(edges, rho, theta, minIntersections)

for lineX in lines:
    for rho,theta in lineX:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img, (x1,y1),(x2,y2),(255,0,0),2)

minLineLength = 40
maxLineGap = 20

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

for lineX in lines:
    for x1, y1, x2, y2 in lineX:
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

if DRAW_CIRCLES:
    circles = cv2.HoughCircles(gray,
                               cv2.HOUGH_GRADIENT,
                               1,20,
                               param1=50,
                               param2=30,
                               minRadius=0,
                               maxRadius=0)
    
    circles = np.uint16(np.around(circles))
    print("circles:", circles)
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(gray, (i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(gray, (i[0],i[1]),2,(0,0,255),3)


cv2.imwrite('lines.png', img)    
