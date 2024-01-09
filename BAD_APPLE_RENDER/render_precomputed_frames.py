import time
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("BAD_APPLE_RENDER/sound.wav")
if_inverted = input("Enter 'e' if you want the video inverted else just press enter: ")

def display_ascii_frames(file_path):
    with open(file_path, 'r') as file:
        all_frames_ascii = file.read().split('\n\n')
        if len(all_frames_ascii) <= 1:
            print("You haven't precomputed the file!")
            exit(1)
        play_obj = wave_obj.play()
        for frame in all_frames_ascii:
            time.sleep(1/35)
            print(frame)

ascii_frames_file = 'BAD_APPLE_RENDER/ascii_frames_reverse.txt' if if_inverted.lower() == 'e' else 'BAD_APPLE_RENDER/ascii_frames.txt'

display_ascii_frames(ascii_frames_file)