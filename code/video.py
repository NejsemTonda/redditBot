import moviepy.editor as mpy
from moviepy.video.fx.all import crop
import random
import os

def crop(video):
    new_height = video.size[1]
    new_width = int(new_height * 9/16)
    
    x_center = (video.size[0]) // 2
    y_center = (video.size[1] - new_height) // 2
    return  crop(video, width=new_width, height=new_height, x_center=x_center, y_center=y_center)
    

def get_random_interval(clip, t=60):
    duration = clip.duration
    if duration < t:
        raise ValueError("tried to get {t} seconds interval from {duration} seconds clip")

    start = random.uniform(0, duration-t)
    end = start+t

    return clip.subclip(start, end)

def word_animation(word, start_time, ats):
    txt_clip = mpy.TextClip(word, font="Amiri-Bold", fontsize=100, color='white')
    txt_clip = txt_clip.set_duration(ats)
    txt_clip = txt_clip.set_start(start_time)
    return txt_clip


def get_text(name):
    with open(f"../src/text/{name}", 'r') as file:
        return list(map(str.strip, file.readlines()))



background = mpy.VideoFileClip("../src/background/cropped_trackmania.webm")
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

background = get_random_interval(background, time_offset)
video = mpy.CompositeVideoClip([background]+videos)

video.write_videofile("word_animation.mp4", codec='libx264', fps=6)
