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
