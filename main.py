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
ret1, background = cap.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
consecutive_frame=4
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame_rec_count += 1
        orig_frame = frame.copy()
        # IMPORTANT STEP: convert the frame to grayscale first
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        motion=0
        if frame_rec_count % consecutive_frame == 0 or frame_rec_count == 1:
            frame_diff_list = []
        # find the difference between current frame and base frame
        frame_diff = cv2.absdiff(gray, background)
        # thresholding to convert the frame to binary
        ret, thres = cv2.threshold(frame_diff, 50, 255, cv2.THRESH_BINARY)
        # dilate the frame a bit to get some more white area...
        # ... makes the detection of contours a bit easier
        dilate_frame = cv2.dilate(thres, None, iterations=2)
        # append the final result into the `frame_diff_list`
        frame_diff_list.append(dilate_frame)
        # if we have reached `consecutive_frame` number of frames
        if len(frame_diff_list) == consecutive_frame:
            # add all the frames in the `frame_diff_list`
            sum_frames = sum(frame_diff_list)
            # find the contours around the white segmented areas
            contours, hierarchy = cv2.findContours(sum_frames, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # draw the contours, not strictly necessary
            # for i, cnt in enumerate(contours):
            #     cv2.drawContours(frame, contours, i, (0, 0, 255), 3)
            for contour in contours:
                motion=1
            #     # continue through the loop if contour area is less than 500...
            #     # ... helps in removing noise detection
            #     if cv2.contourArea(contour) < 500:
            #         continue
            #     # get the xmin, ymin, width, and height coordinates from the contours
            #     (x, y, w, h) = cv2.boundingRect(contour)
            #     # draw the bounding boxes
            #     cv2.rectangle(orig_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if motion==1:
                cv2.line(frame, (0, 0), (480, 640), (0, 0, 255), 34)
            # cv2.line(orig_frame, (0, 0), (480, 640), (0, 0, 255), 34)
            cv2.imshow('Detected Objects', orig_frame)
            out.write(orig_frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
    else:
        break
cap.release()
cv2.destroyAllWindows()