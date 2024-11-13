import time
import wave

import numpy as np
import pyaudio
import pyautogui
import cv2
import soundcard as sc
import soundfile as sf

# Set video resolution
resolution = pyautogui.size()
codec = cv2.VideoWriter_fourcc(*'mp4v')
filename = "video.mp4"
fps = 5
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 640, 480)

def record_video():
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        time.sleep(1 / fps)

    close_video_recorder()

def close_video_recorder():
    out.release()
    cv2.destroyAllWindows()


