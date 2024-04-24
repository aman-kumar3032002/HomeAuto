An **OpenCV-based Home Automation** system has been developed to automatically control appliances based on detected parameters. This project entails an OpenCV system that regulates a fan according to the user's location within a room, utilizing a [caffe](https://github.com/BVLC/caffe) model to detect human presence.
Upon detecting a human presence in the room, the system verifies whether the detected point falls within the designated region. If the individual is located within the specified area, the functionality will activate, turning the system ON; otherwise, it will remain OFF.

I am utilizing the **Raspberry Pi 5** for hardware, in conjunction with relay modules that function as switches. The camera setup comprises a Lenovo FHD webcam, with the Raspberry Pi Cam or ESP32 Cam serving as viable alternatives.

##Circuit Diagram
![ckt diagram](https://github.com/aman-kumar3032002/HomeAuto/blob/main/HomeAuto_ckt_diag.pdf)

##Flow Chart 
![Flow chart](https://github.com/aman-kumar3032002/HomeAuto/blob/main/flow_chart.png)

##Advantages
-Saves Electricity
-Better than the sensor based systems as they have low area of vision
-better accuracy than pir sensor

##Disadvantages
-Doesn't work in low light condition.
-Fake Detections

#Further Advancement
-Minimizing the Fake detections
-Gesture recognition
-Adding other appliances
