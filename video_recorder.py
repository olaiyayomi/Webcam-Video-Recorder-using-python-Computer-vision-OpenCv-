import cv2
import sys

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('D:/YOMTECH PROJECTS/my python/test/output2.avi',fourcc, 20.0, (640,480))

if not capture.isOpened():
    sys,exit("Unable to read camera")

while True:
    rel, frame = capture.read()

    if not rel:
        print("Unable to read all frame")
        break
    out.write(frame)

    cv2.imshow("my video", frame)

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        
        break

capture.release
cv2.destroyAllWindows()
