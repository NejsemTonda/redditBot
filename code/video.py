import moviepy.editor as mpy
from moviepy.video.fx.all import crop
import random
import os

def get_random_interval(clip, t=60):
    duration = clip.duration
    if duration < t:
        raise ValueError("tried to get {t} seconds interval from {duration} seconds clip")

    start = random.uniform(0, duration-t)
    end = start+t

    return clip.subclip(start, end)


def word_animation(word, start_time, ats):
    text = mpy.TextClip(word, font="URWBookman-Demi", fontsize=100, color='white')
    text = text.set_pos('center')

    shadow = mpy.TextClip(word, font="URWBookman-Demi", fontsize=100, color='black')
    shadow = shadow.set_pos(('center', 5))

    final = mpy.CompositeVideoClip([shadow,text])
    final = final.set_duration(ats)
    final = final.set_start(start_time)
    final = final.resize(lambda t: min(1, 1 - 6*(1/6*ats - t)))

    return final


def get_text(name):
    with open(f"../src/text/{name}", 'r') as file:
        return list(map(str.strip, file.readlines()))

def texts_to_videos(texts, audios, size=(606,1080)):
    videos = []
    time_offset = 0
    for i, post in enumerate(texts):
        words = post.split()
        audio = audios[i]
        ats = audio.duration / len(words)
        
        clips = [word_animation(word, time_offset + j*ats, ats) for j, word in enumerate(words)]
        video = mpy.CompositeVideoClip([c.set_pos('center') for c in clips], size=size)
    
        audio = audio.set_start(time_offset)
        video = video.set_audio(audio)
        time_offset += audio.duration + 0.5
        
        videos.append(video)
 
    return mpy.CompositeVideoClip(videos)

def get_random_background():
    return random.choice([mpy.VideoFileClip("../src/background/"+file) for file in os.listdir("../src/background") if "cropped_" in file]).volumex(0.05)

def create_video(name):
    print("getting background")
    background = get_random_background()

    print("generating text video")
    texts = get_text(name+".txt")
    audios = list(map(mpy.AudioFileClip, sorted(["../src/voices/"+file for file in os.listdir("../src/voices") if name in file])))
    text_video = texts_to_videos(texts, audios, size=background.size)

    print("getting music")
    music = mpy.AudioFileClip("../src/background/jazz.m4a").volumex(0.04)
    
    print("Composing everithung together")
    background = get_random_interval(background, text_video.duration)
    music = get_random_interval(music, text_video.duration)

    video = mpy.CompositeVideoClip([background, text_video])
    audio = mpy.CompositeAudioClip([text_video.audio, music])

    video = video.set_audio(audio)

    print("saving")
    video.write_videofile(f"../videos/{name}.mp4", fps=60)
