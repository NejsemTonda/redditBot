import moviepy.editor as mpy
from moviepy.video.fx.all import crop
import random
import os
from moviepy.video.fx import resize

def anim(t,ats):
    print(f"----> {t-ats}")
    val = max(1, 1.5-0.5*(t-ats))
    print(val)
    return val


def get_random_interval(clip, t=60):
    duration = clip.duration
    if duration < t:
        raise ValueError("tried to get {t} seconds interval from {duration} seconds clip")

    start = random.uniform(0, duration-t)
    end = start+t

    return clip.subclip(start, end)

def word_animation(word, start_time, ats):
    text = mpy.TextClip(word, font="URWBookman-Demi", fontsize=100, color='white')
    text = text.set_duration(ats)
    text = text.set_start(start_time)
    
    #text = text.resize(lambda t: max(1, 1.5-0.5*(3*t)))
    text = text.resize(lambda t: anim(t, ats))
    

    return text


def get_text(name):
    with open(f"../src/text/{name}", 'r') as file:
        return list(map(str.strip, file.readlines()))



background = mpy.VideoFileClip("../src/background/cropped_trackmania.webm").volumex(0.1)
audios = [mpy.AudioFileClip("../src/voices/"+name) for name in os.listdir("../src/voices") if "001-" in name]
videos = []
time_offset = 0
for i, post in enumerate(get_text("001.txt")):
    words = post.split()
    audio = audios[i]
    ats = audio.duration / len(words)
    
    clips = [word_animation(word, time_offset + j*ats, ats) for j, word in enumerate(words)]
    video = mpy.CompositeVideoClip([c.set_pos('center') for c in clips], size=background.size)

    audio = audio.set_start(time_offset)
    video = video.set_audio(audio)
    time_offset += audio.duration + 0.5
    
    videos.append(video)
    break

background = get_random_interval(background, time_offset)
video = mpy.CompositeVideoClip([background]+videos)
#video = video.fl_image(blur)

video.write_videofile("word_animation.mp4", codec='libx264', fps=60)
