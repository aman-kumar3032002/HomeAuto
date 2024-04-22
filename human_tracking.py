import cv2
import imutils
import numpy as np

protopath = "E:\Data Science\OpenCV\HomeAutomation\MobileNetSSD_deploy.prototxt"
modelpath = "E:\Data Science\OpenCV\HomeAutomation\MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)


CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

boundry_start_x,boundry_start_y = 150,30
boundry_end_x,boundry_end_y = 420,380


def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=600)
        cv2.rectangle(frame, (boundry_start_x,boundry_start_y), (boundry_end_x,boundry_end_y) , (0, 0, 255), 2)
        
        (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

        detector.setInput(blob)
        person_detections = detector.forward()

        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.2:
                idx = int(person_detections[0, 0, i, 1])

                if CLASSES[idx] != "person":
                    continue

                person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = person_box.astype("int")

                detected_x =int((startX+endX)/2)                                            #detected_x: the x coordinate of the centroid of the box 
                detected_y =int((startY+endY)/2)                                            #detected_y: the y coordinate of the centroid of the box 
                
                inside_area(detected_x,detected_y)
                #drwaing a rectangle around the person
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

                #drawing a point on the centre of the box
                cv2.circle(frame,(detected_x,detected_y),3,(255,0,0),-1)

        cv2.imshow("Application", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

def inside_area(x,y):
    if x in range(boundry_start_x,boundry_end_x) and y in range(boundry_start_y,boundry_end_y):
        print("ON")
    else:
        print("OFF")

main()