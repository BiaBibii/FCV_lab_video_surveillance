import cv2
import numpy as np
cap = cv2.VideoCapture(0)
last_mean = 0
detected_motion = False
frame_rec_count = 0
frame_rec_count1 = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

fourcc1 = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('output_modified.avi',fourcc1, 20.0, (640, 480))
while(True):
    ret, frame = cap.read()
    ret1, frame1 = cap.read()
    # print("Ret",ret)
    print("frame",frame.shape)
    cv2.imshow('as',ret)
    cv2.imshow('frame', frame)
    cv2.line(frame1, (0, 0), (480, 640), (0, 0, 255), 34)
    # cv2.imshow('frame1',frame1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gds",gray)
    result = np.abs(np.mean(gray) - last_mean)
    last_mean= np.mean(gray)
    frame_rec_count1 = frame_rec_count1 + 1
    if result > 0.5:
        print("Motion detected!")
        detected_motion = True
        out.write(frame)
        frame_rec_count = frame_rec_count + 1
    else:
        # cv2.imshow('frame1', frame1)
        # cv2.waitKey(150)
        # cv2.destroyWindow('frame1')
        out.write(frame1)
        out1.write(frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')) :
         break

cap.release()
cv2.destroyAllWindows()
print(frame_rec_count)
print(frame_rec_count1)