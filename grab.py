import cv2

STREAM = "https://s5.webcamromania.ro/piataromanab/index.m3u8"
cap = cv2.VideoCapture(STREAM)
print("opened:", cap.isOpened())

ok, frame = cap.read()
print("got frame:", ok, frame.shape if ok else None)
if ok:
    cv2.imwrite("stream_frame.jpg", frame)
cap.release()