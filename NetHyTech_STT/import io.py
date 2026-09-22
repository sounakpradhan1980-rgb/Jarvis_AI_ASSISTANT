import io
import wave
import pyaudio
from faster_whisper import WhisperModel


model = WhisperModel("tiny.en", device="cpu", compute_type="int8")

def listen():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 16000
    seconds = 5 

    p = pyaudio.PyAudio()
    print("Listening...")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []
    for _ in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

  
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
    
    wav_buffer.seek(0)

  
    segments, _ = model.transcribe(wav_buffer)
    recognized_text = " ".join([segment.text for segment in segments]).strip()
    
    print(f"Recognized: {recognized_text}")
    return recognized_text

if __name__ == "__main__":
    listen()