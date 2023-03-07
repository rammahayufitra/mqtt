import cv2

path = './weights/cascade.xml'
face_detector = cv2.CascadeClassifier(path)

def Detector(frames):
    """ FETCH frame
        @params
            frames - frames from camera webcam 
        @return 
            results - coordinates face's bounding box
    """
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    results = face_detector.detectMultiScale(gray, 1.3, 5) 
    return results