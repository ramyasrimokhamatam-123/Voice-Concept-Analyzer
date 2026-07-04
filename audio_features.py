import librosa
import numpy as np

def extract_audio_features(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Calculate RMS Energy
    rms = librosa.feature.rms(y=y)[0]
    rms_energy = float(np.mean(rms))

    # Calculate Pause Ratio
    threshold = 0.01
    silent_samples = np.sum(np.abs(y) < threshold)
    pause_ratio = silent_samples / len(y)

    return {
        "rms_energy": rms_energy,
        "pause_ratio": pause_ratio
    }