import ffmpeg
import numpy as np
import exception_handlers as eh


def extract_audio_from_video(video_filepath):
    try:
        # Extract audio with ffmpeg
        out, err = ffmpeg.input(video_filepath) \
            .output('pipe:1', format='wav') \
            .run(capture_stdout=True, capture_stderr=True)

        # Convert audio data to numerical values
        audio_data = np.frombuffer(out, np.int16)
        return audio_data

    except ffmpeg.Error as e:
        eh.show_error("ffmpeg is unable to open the video")
        return None
    except PermissionError:
        eh.show_error("Unable to access video file")
        return None


def save_db_values(video_filepath, audio_data):
    audio_data = extract_audio_from_video(video_filepath)

    if audio_data is not None:
        print("Audio data successfully extracted")
        epsilon = 1e-10
        audio_data_db = 20 * np.log10(np.abs(audio_data) + epsilon)

        try:
            with(open("db_values.txt", "w")) as f:
                f.writelines(str(audio_data_db))
        except PermissionError:
            eh.show_error("Unable to write to db values to a text file")


if __name__ == "__main__":
    extract_audio_from_video("video.mp4")