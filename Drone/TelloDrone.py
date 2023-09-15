import cv2
from djitellopy import Tello
tello = Tello()
tello.connect()
tello.streamon()
tello.takeoff()  # 이륙
tello.move_forward(50)  # 앞으로 50cm 이동
cap=cv2.VideoCapture('udp://@0.0.0:11111')
ret, frame=cap.read()
if ret:
    cv2.imwrite('pic1.jpg',frame)
tello.rotate_clockwise(90)  # 오른쪽으로 90도 회전
tello.move_forward(20)  # 앞으로 20cm 이동
tello.rotate_counter_clockwise(90)
cap2=cv2.VideoCapture('udp://@0.0.0:11111')
ret2, frame2=cap2.read()
if ret2:
    cv2.imwrite('pic2.jpg',frame2)
tello.rotate_clockwise(90)  # 오른쪽으로 90도 회전
tello.move_forward(20)  # 앞으로 20cm 이동
tello.rotate_counter_clockwise(90)
cap3=cv2.VideoCapture('udp://@0.0.0:11111')
ret3, frame3=cap3.read()
if ret3:
    cv2.imwrite('pic3.jpg',frame3)
tello.land()
tello.end()