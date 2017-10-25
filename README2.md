# IoT Car
Internet-controlled Robot Car (semi-autonomous)
Below I will describe the project and steps to take.

## Materials
You'll need the following materials to get started:

LSM9DS1 9DoF (accelerometer, gyro, and magnetometer in one chip used for determining speed and heading) - [part here](https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide?_ga=2.140200437.734737643.1508941937-1881043274.1507820070)
Raspberry Pi 3 (the brains) - [part here](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
Chassis (the structure) - I used [this one](https://www.amazon.com/Wheels-Robot-Chassis-Encoder-Arduino/dp/B01N3PCWHC/ref=sr_1_5?ie=UTF8&qid=1508942240&sr=8-5&keywords=robot+chassis) but you can use any chassis. This chassis came with motors.
Soldering Iron and solder (tools) - You'll need a soldering iron to solder a motor shield and the motors. I use lead free solder.
Motor shield - I used an Adafruit PiHat, which you can fine [here](https://www.amazon.com/Adafruit-16-Channel-PWM-Servo-Raspberry/dp/B00SI1SPHS/ref=sr_1_3?s=industrial&ie=UTF8&qid=1508942339&sr=1-3&keywords=motor+shield+raspberry+pi)
Webcam - for streaming video from the robot. Again, you can really use any webcam you'd like. I used a basic logitech USB webcam similar to this [one](https://www.amazon.com/Ausdom-Webcam-Camera-Microphone-Sliver/dp/B01CZROAT2/ref=sr_1_18_sspa?ie=UTF8&qid=1508942467&sr=8-18-spons&keywords=logitech+usb+webcam&psc=1). The form factor works well for the chassis, since it fits between the two platforms of the chassis perfectly.
Computer / Phone - You will use the computer and phone for client side control. The phone UI will have no video streaming, but the computer will be able to receive a HTTP video stream from the robot using VLC.

Total cost: assuming you already own a computer, phone, and soldering iron, the total cost of this project will be roughly 35+25+18+23=$101 without the webcam and $124 with the camera. Again, this is assuming you don't have any Raspberry Pi or webcam. Generally, I've found most people have a webcam that is suitable for this application.

## Steps
