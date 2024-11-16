import cv2
import numpy as np
import pyautogui
import time
import mss
import exception_handlers as eh


resolution = pyautogui.size()
codec = cv2.VideoWriter_fourcc(*'mp4v')
filename = "video.mp4"
fps = 20
out = cv2.VideoWriter(filename, codec, fps, resolution)

#added for mss
monitor = {"top": 0, "left": 0, "width": resolution[0], "height": resolution[1]}

def record_video(sec):
    # Video settings
    RECORD_SEC = sec  # Specify how many seconds to record
    """Records the screen as video for a specified duration."""
    cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Recording", 640, 480)

    start_time = time.time()  # Track the start time
    try:
        with mss.mss() as sct:
            while time.time() - start_time < RECORD_SEC:
                frame = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                out.write(frame)
                cv2.imshow("Recording", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    except Exception as e:
        eh.show_error(f"Error during video recording: {e}")
    finally:
        close_video_recorder()


def close_video_recorder():
    """Closes the video recording resources."""
    out.release()
    cv2.destroyAllWindows()
    print("Video recording complete.")

if __name__ == "__main__":
    record_video(15)