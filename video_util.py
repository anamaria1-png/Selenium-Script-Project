import ffmpeg

def video_audio_mux(path_audiosource, path_imagesource, out_video_path):
    video = ffmpeg.input(path_imagesource).video
    audio = ffmpeg.input(path_audiosource).audio
    ffmpeg.output(audio, video, out_video_path, vcodec='copy', acodec='copy').run()

if __name__ == '__main__':
    video_audio_mux("out.wav", "video.mp4", "out.mp4")