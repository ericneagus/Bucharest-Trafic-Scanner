import cv2, time


STREAM = "https://s5.webcamromania.ro/piataromanab/index.m3u8"
cap = cv2.VideoCapture(STREAM)

ok, frame = cap.read()
h, w = frame.shape[:2]
fps = cap.get(cv2.CAP_PROP_FPS)
print(w, h, fps)

out = cv2.VideoWriter("clip.mp4", cv2.VideoWriter_fourcc(*"mp4v"),fps or 25, (w,h))
start = time.time()
while time.time() - start < 30:
    ok,frame = cap.read()
    if not ok:
        break
    out.write(frame)
out.release()
cap.release()
