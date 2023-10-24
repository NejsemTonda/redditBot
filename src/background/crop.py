from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, clips_array

target = "trackmania.webm"

# Load your video
video = VideoFileClip(target)

# Calculate the new dimensions for the 9:16 aspect ratio
print(video.size)
new_height = video.size[1]
new_width = int(new_height * 9/16)



# Calculate the position to center the video
x_center = (video.size[0] - new_width) // 2
y_center = (video.size[1] - new_height) // 2

# Crop the video to the new dimensions
cropped_video = video.crop(x_center, y_center, new_width, new_height)

# Save the cropped video to a new file
cropped_video.write_videofile("cropped_"+target)
