import cv2
import numpy as np
cap = cv2.VideoCapture(0)
last_mean = 0
detected_motion = False
frame_rec_count = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

ret_init, frame_init = cap.read()
frame_number = 4
while (cap.isOpened()):
    if frame_rec_count == 0:
        ret, prev_frame = cap.read()
        if ret == True:
            prev = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    detected_motion = False
    ret, frame = cap.read()
    if ret:
        frame_rec_count = frame_rec_count + 1
        orig_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if frame_rec_count % frame_number == 0 or frame_rec_count == 1:
            frame_list = []
        dif_frames = cv2.absdiff(gray, prev)
        # print(dif_frames)
        ret, threshold = cv2.threshold(dif_frames, 80, 255, cv2.THRESH_BINARY)
        # print(threshold)

        dilate_frame = cv2.dilate(threshold, None, iterations=2)
        prev = gray
        # print(threshold)
        # print(dif_frames)
        dif_frames=np.append(dif_frames,dilate_frame)
        if len(frame_list) == frame_number:
            sum_fr = sum(frame_list)

            cv2.line(orig_frame, (0, 0), (480, 640), (0, 0, 255), 34)
            print(sum)

            cv2.imshow('frame1', orig_frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                 break

cap.release()
cv2.destroyAllWindows()
print(frame_rec_count)
# print(frame_rec_count1)
