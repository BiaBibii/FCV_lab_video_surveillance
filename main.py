import cv2
import numpy as np
#capture the video from the camera
cap = cv2.VideoCapture(0)

last_mean = 0
detected_motion = False
frame_rec_count = 0
frame_rec_count1 = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = np.abs(np.mean(gray) - last_mean)
    last_mean= np.mean(gray)
    frame_rec_count1 = frame_rec_count1 + 1
    if result > 0.3:
        print("Motion detected!")
        detected_motion = True
        out.write(frame)
        frame_rec_count = frame_rec_count + 1
    else:
        cv2.line(frame, (0, 0), (480, 640), (0, 0, 255), 34)

    cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')) :
         break

cap.release()
cv2.destroyAllWindows()
print(frame_rec_count)
