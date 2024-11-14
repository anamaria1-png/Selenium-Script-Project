# import soundcard as sc
# import soundfile as sf
#
# def record_audio():
#     OUTPUT_FILE_NAME = "out.wav"
#     SAMPLE_RATE = 44100  # [Hz]. sampling rate.
#     RECORD_SEC = 90  # [sec]. duration recording audio.
#
#     with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
#             samplerate=SAMPLE_RATE) as mic:
#         # record audio with loopback from default speaker.
#         data = mic.record(numframes=SAMPLE_RATE * RECORD_SEC)
#
#         # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
#         sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
#
# if __name__ == '__main__':
#     record_audio()


import soundcard as sc
import soundfile as sf

def record_audio(sec):
    """Records audio from the default speaker using loopback."""
    OUTPUT_FILE_NAME = "out.wav"
    SAMPLE_RATE = 44100
    RECORD_SEC = sec

    try:
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
            samplerate=SAMPLE_RATE
        ) as mic:
            audio_data = mic.record(numframes=SAMPLE_RATE * RECORD_SEC)
            sf.write(file=OUTPUT_FILE_NAME, data=audio_data[:, 0], samplerate=SAMPLE_RATE)
            print("Audio recording complete.")
    except Exception as e:
        print(f"Error recording audio: {e}")
