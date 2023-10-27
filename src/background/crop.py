import moviepy.editor as mpy
from moviepy.video.fx.all import crop

target = "trackmania.webm"

# Load your video
video = mpy.VideoFileClip(target)

# Calculate the new dimensions for the 9:16 aspect ratio
print(video.size)
new_height = video.size[1]
new_width = int(new_height * 9/16)


# Calculate the position to center the video
x_center = (video.size[0]) // 2
y_center = (video.size[1] - new_height) // 2

# Crop the video to the new dimensions

cropped_video = crop(video, width=new_width, height=new_height, x_center=x_center, y_center=y_center)


# Save the cropped video to a new file
cropped_video.write_videofile("cropped_"+target)
