import numpy as np
import cv2
import time
from src import sprayer
from src import camera


# video stream path
video = "../res/belt.mp4"

# load video
mp4 = cv2.VideoCapture(video)

# start in middle of video (frame 200)
start_frame = 400
# start_frame = 500
mp4.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

while True:

    # reduce video frames-per-second for analysis
    # time.sleep(0.03)

    # Get next frame in video
    _, frame = mp4.read()

    # Check to see if at last frame of video
    if frame is None:
        break

    # copy frame for drawing visuals
    draw = np.copy(frame)

    # crop frame to region where camera would be looking
    current_frame = frame[150:210, 190:230]


    # find position of box in current frame
    results = camera.scan(current_frame)

    sprayer.queue_spray(results)

    # Draw visuals onto frame
    cv2.rectangle(draw, (190, 150), (230, 210), (255, 0, 0), 2)
    sprayer.update(draw)

    # Display the resulting frame
    cv2.imshow('visual', draw)
    cv2.imshow('camera', current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    last_frame = current_frame

# When everything done, release the capture
mp4.release()
cv2.destroyAllWindows()
