from moviepy import VideoFileClip
import argparse
import numpy as np

# TODO - use ffmpeg to get the date and timestamp

# TODO - get audio information for all videos and find times with noise. Save those videos separately for review

# maybe use librosa or scipy for audio analysis

def main(video_file_path):
    clip = VideoFileClip(video_file_path)
    audio = clip.audio.to_soundarray()[:,0] # videos are all monostereo

    audio_mask = audio > (audio.mean()+audio.std())
    diff = np.diff(audio_mask.astype(int))
    rising_edges = np.where(diff == 1)[0]
    falling_edges = np.where(diff == -1)[0]

    relative_time_stamps = np.linspace(0,clip.duration, len(audio))

    relative_time_stamps[audio_mask]

    a = 1
    input()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Read video file.", description = "Imports video file using moviepy")
    parser.add_argument("video", type = str)
    args = parser.parse_args()
    main(args.video)