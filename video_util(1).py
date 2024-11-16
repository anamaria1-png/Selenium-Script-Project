import ffmpeg
import exception_handlers as eh

def video_audio_mux(path_audiosource, path_videosource, out_video_path):
    try:
        video = ffmpeg.input(path_videosource).video
        audio = ffmpeg.input(path_audiosource).audio
        ffmpeg.output(audio, video, out_video_path, vcodec='copy', acodec='copy').run()
    except ffmpeg.Error as e:
        eh.show_error("Unable to open video file")
    except PermissionError:
        eh.access_denied_error()

if __name__ == '__main__':
    video_audio_mux("out.wav", "video.mp4", "out.mp4")