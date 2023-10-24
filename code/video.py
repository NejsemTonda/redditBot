import moviepy.editor as ed
import random

def get_random_interval(clip, t=60):
    duration = clip.duration
    if duration < t:
        raise ValueError("tried to get {t} seconds interval from {duration} seconds clip")

    start = random.uniform(0, duration-t)
    end = start+t

    return clip.subclip(start, end)





clip = ed.VideoFileClip("../src/background/trackmaina.webm")
#clip.write_videofile("001.mp4")

