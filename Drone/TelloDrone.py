import cv2
import time
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()
tello.takeoff()  # 이륙
tello.move_forward(50)  # 앞으로 50cm 이동
time.sleep(3)
cap=cv2.VideoCapture('udp://@0.0.0:11111')
ret, frame=cap.read()
if ret:
    cv2.imwrite('pic1.jpg',frame)
    cap.release()
tello.rotate_clockwise(90)  # 오른쪽으로 90도 회전
tello.move_forward(20)  # 앞으로 20cm 이동
tello.rotate_counter_clockwise(90)
time.sleep(3)
cap=cv2.VideoCapture('udp://@0.0.0:11111')
ret, frame=cap.read()
if ret:
    cv2.imwrite('pic2.jpg',frame)
    cap.release()
tello.rotate_clockwise(90)  # 오른쪽으로 90도 회전
tello.move_forward(20)  # 앞으로 20cm 이동
tello.rotate_counter_clockwise(90)
time.sleep(3)
cap=cv2.VideoCapture('udp://@0.0.0:11111')
ret, frame=cap.read()
if ret:
    cv2.imwrite('pic3.jpg',frame)
    cap.release()
tello.land()
tello.end()
