import moviepy.editor as mpy
from moviepy.video.fx.all import crop

target = "trackmania.webm"
video = mpy.VideoFileClip(target)

#new_height = video.size[1]
#new_width = int(new_height * 9/16)


# hard set the video size, beacause moviepy can deal with odd integers
new_height = 1080
new_width = 606

x_center = (video.size[0]) // 2
y_center = (video.size[1] - new_height) // 2


cropped_video = crop(video, width=new_width, height=new_height, x_center=x_center, y_center=y_center)


cropped_video.write_videofile("cropped_"+target)
