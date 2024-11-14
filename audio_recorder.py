import soundcard as sc
import soundfile as sf

def record_audio():
    OUTPUT_FILE_NAME = "out.wav"  # file name.
    SAMPLE_RATE = 44100  # [Hz]. sampling rate.
    RECORD_SEC = 90  # [sec]. duration recording audio.

    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(
            samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE * RECORD_SEC)

        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

if __name__ == '__main__':
    record_audio()