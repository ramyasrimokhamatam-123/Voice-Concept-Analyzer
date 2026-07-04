import os
import librosa
import librosa.display
import matplotlib.pyplot as plt


def plot_waveform(audio_path):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    y, sr = librosa.load(audio_path, sr=None)

    plt.figure(figsize=(10,3))
    librosa.display.waveshow(y, sr=sr)

    plt.title("Audio Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    image_path = "reports/waveform.png"

    plt.savefig(image_path)
    plt.close()

    return image_path