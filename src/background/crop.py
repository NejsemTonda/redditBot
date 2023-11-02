import moviepy.editor as mpy
from moviepy.video.fx.all import crop
from argparse import ArgumentParser

def crop(target, remove_sound=False):
    video = mpy.VideoFileClip(target)
    video = video.resize((1920, 1080))
     
    if remove_sound:
        video = video.set_audio(None)
    # hard set the video size, beacause moviepy can deal with odd integers
    new_height = 1080
    new_width = 606
    
    x_center = (video.size[0]) // 2
    y_center = (video.size[1] - new_height) // 2
    
    
    cropped_video = video.crop(width=new_width, height=new_height, x_center=x_center, y_center=y_center)
    cropped_video.write_videofile("cropped_"+target)


parser = ArgumentParser()
parser.add_argument("-r", "--remove-sound", default=False, action="store_true", help="remove sound from the original video")
parser.add_argument("videos", nargs="*", help="List of vidoes to crop")
args = parser.parse_args()

for t in args.videos:
    crop(t, args.remove_sound)

