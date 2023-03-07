import cv2

def Draw(frame, box):
    cv2.rectangle(frame,box.p1,box.p2,(0,255,0),2)
    return frame