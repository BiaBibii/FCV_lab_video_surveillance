import cv2
import numpy as np

cap = cv2.VideoCapture(0)
last_mean = 0
detected_motion = False
frame_rec_count = 0
frame_rec_count1 = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

ret_init, frame_init = cap.read()

while (True):
    ret, frame = cap.read()
    ret1, frame1 = cap.read()

    if frame_rec_count == 0:
        gray = cv2.cvtColor(frame_init, cv2.COLOR_BGR2GRAY)
        first_mean = np.mean(gray)
        result = np.abs(np.mean(gray) - first_mean)
        print("first res", result)
        last_mean = np.mean(gray)


    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = np.abs(np.mean(gray) - last_mean)

        last_mean = np.mean(gray)

    frame_rec_count = frame_rec_count + 1
    if result > 0.3:
        print("Motion detected!")
        detected_motion = True
        out.write(frame)
        frame_rec_count = frame_rec_count + 1
    else:
        print("NOOOOO motion!")
        cv2.line(frame, (0, 0), (480, 640), (0, 0, 255), 34)
        frame_rec_count1 = frame_rec_count1 + 1

    cv2.imshow('frame1', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
print(frame_rec_count)
print(frame_rec_count1)
