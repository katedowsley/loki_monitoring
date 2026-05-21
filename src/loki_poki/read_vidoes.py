from moviepy import VideoFileClip
import argparse
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import librosa

# TODO - use ffmpeg to get the date and timestamp

# TODO - get audio information for all videos and find times with noise. Save those videos separately for review

# maybe use librosa or scipy for audio analysis

def find_edge_indexes(mask, min_high = 0, min_low = 441000*3): # min_low is 3 consequetive seconds
    #TODO
    idx = np.array([])
    
    return idx

def main(video_file_path):
    sr = 44100
    print(video_file_path)
    clip = VideoFileClip(video_file_path)
    audio = clip.audio.to_soundarray()[:,0] # videos are all monostereo

    audio_mask = audio > (audio.mean()+audio.std())
    diff = np.diff(audio_mask.astype(int))
    rising_edges = np.where(diff == 1)[0]
    falling_edges = np.where(diff == -1)[0]

    relative_time_stamps = np.linspace(0,clip.duration, len(audio))

    relative_time_stamps[audio_mask]

    S = librosa.feature.melspectrogram(y=audio.T, sr=44100)
    S_db_mel = librosa.amplitude_to_db(S, ref=np.max)


    # Plot the Log-Scaled Mel Spectrogram
    fig, ax = plt.subplots(figsize=(12, 7))  # Increase figure size for better clarity

    # Display the Mel Spectrogram in Decibels
    img = librosa.display.specshow(
        S_db_mel,               # Spectrogram data (in dB scale)
        sr=sr,                  # Sampling rate for accurate time display
        x_axis='time',          # X-axis: Time (seconds)
        y_axis='mel',           # Y-axis: Mel-frequency scale
        cmap='magma',           # Use a perceptually uniform colormap
        ax=ax                   # Plot on the specified subplot
    )

    # Add Title and Axis Labels
    ax.set_title("Mel Spectrogram (Log Scale in Decibels)", fontsize=18, fontweight="bold")
    ax.set_xlabel("Time (s)", fontsize=14)
    ax.set_ylabel("Mel Frequency (Hz)", fontsize=14)

    # Add a Color Bar to Show the Decibel Range
    cbar = fig.colorbar(img, ax=ax, format="%+2.0f dB")
    cbar.set_label("Amplitude (dB)", fontsize=12)

    # Adjust Layout for Better Visualization
    plt.tight_layout()
    plt.show()


    a = 1
    input()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Read video file.", description = "Imports video file using moviepy")
    parser.add_argument("video", type = str)
    args = parser.parse_args()
    main(args.video)