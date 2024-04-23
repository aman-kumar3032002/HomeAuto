import cv2
from imutils import imutils
import numpy as np
#library for using Pi gpio pins
from gpiozero import LED     

light = LED(14)                                                                            #light : stores the gpio pin number, with which light is connected
fan = LED(15)                                                                              #fan   : stores the gpio pin number, with which the fan is connected

protopath = "/home/Pi/Desktop/Projects/MobileNetSSD_deploy.prototxt"
modelpath = "/home/Pi/Desktop/Projects/MobileNetSSD_deploy.caffemodel"
#using a pretrained model-------------------------------------------------------------------
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
        # cv2.rectangle(frame, (boundry_start_x,boundry_start_y), (boundry_end_x,boundry_end_y) , (0, 0, 255), 2)

        (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame,  0.007843, (W, H), 127.5)                       #blob: stores the 4d array for the input image

        #setting the input layer as the costme
        detector.setInput(blob)
        person_detections = detector.forward()
        # print(person_detections)
        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.4:
                idx = int(person_detections[0, 0, i, 1])
                if CLASSES[idx] != "person":
                    continue

                person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = person_box.astype("int")

                detected_x =int((startX+endX)/2)                                            #detected_x: the x coordinate of the centroid of the box 
                detected_y =int((startY+endY)/2)                                            #detected_y: the y coordinate of the centroid of the box 
                
                inside_area(detected_x,detected_y)

                #drwaing a rectangle around the person
                # cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

                #drawing a point on the centre of the box
                # cv2.circle(frame,(detected_x,detected_y),3,(255,0,0),-1)

        cv2.imshow("Application", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

def inside_area(x,y):
    if x in range(boundry_start_x,boundry_end_x) and y in range(boundry_start_y,boundry_end_y):
        light.on()
        fan.on()
    else:
        light.off()
        fan.off()

main()