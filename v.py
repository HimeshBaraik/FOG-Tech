from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# Load your audio file
audio1 = AudioFileClip("4sec.mp3")
audio4 = AudioFileClip("jadu.mp3")
audio5 = AudioFileClip("papa.mp3")
audiolast = AudioFileClip("mario.mp3")

# Define the start and end timestamps (in seconds) for the audio clips you want to select
start_time = 0  # Example start time
end_time = 4    # Example end time

# Extract the audio clip between the specified timestamps
audio1 = audio1.subclip(start_time, end_time)
audio4 = audio4.subclip(0,6)
audio5 = audio5.subclip(2,8)
audiolast = audiolast.subclip(0,5)

# Load the video file
video_path = "meeee.mp4"
video = VideoFileClip(video_path)


# Extract the clips
clip1 = video.subclip(6, 10)
clip2 = video.subclip(20,24)
clip3 = video.subclip(56,61)
clip4 = video.subclip(152,158)
clip5 = video.subclip(109,115)
cliplast = video.subclip(211,216)


# Define the frame size for YouTube Shorts (9:16 aspect ratio)
frame_width = 1080
frame_height = 1920

# Calculate the new width and height to maintain the aspect ratio
new_height = frame_height
new_width = int(clip1.w * (frame_height / clip1.h))

# Resize the clip to fit the YouTube Shorts frame size
resized_clip1 = clip1.resize(width=new_width, height=new_height)
resized_clip2 = clip2.resize(width=new_width, height=new_height)
resized_clip3 = clip3.resize(width=new_width, height=new_height)
resized_clip4 = clip4.resize(width=new_width, height=new_height)
resized_clip5 = clip5.resize(width=new_width, height=new_height)
resized_cliplast = cliplast.resize(width=new_width, height=new_height)

# Calculate the position to center the resized clip
x_pos = (frame_width - new_width) // 2
y_pos = (frame_height - new_height) // 2

# Place the resized clip on a black background to fill the frame size
final_clip1 = resized_clip1.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))
final_clip2 = resized_clip2.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))
final_clip3 = resized_clip3.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))
final_clip4 = resized_clip4.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))
final_clip5 = resized_clip5.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))
final_cliplast = resized_cliplast.on_color((frame_width, frame_height), color=(0, 0, 0), pos=(x_pos, y_pos))

# Audio setting
final_clip1 = final_clip1.set_audio(audio1)
final_clip4 = final_clip4.set_audio(audio4)
final_clip5 = final_clip5.set_audio(audio5)
final_cliplast = final_cliplast.set_audio(audiolast)




text = "Going to Play Valorant"
text_clip = TextClip(text, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_clip1.duration)
text_clip = text_clip.set_position(('center', 'bottom'))
final_clip1 = CompositeVideoClip([final_clip1, text_clip])

text2 = "Playing Single"
text_clip2 = TextClip(text2, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_clip2.duration)
text_clip2 = text_clip2.set_position(('center', 'bottom'))
final_clip2 = CompositeVideoClip([final_clip2, text_clip2])

text3 = "Playing with friends"
text_clip3 = TextClip(text3, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_clip3.duration)
text_clip3 = text_clip3.set_position(('center', 'bottom'))
final_clip3 = CompositeVideoClip([final_clip3, text_clip3])

text4 = "YORU & its CLONE"
text_clip4 = TextClip(text4, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_clip4.duration)
text_clip4 = text_clip4.set_position(('center', 'bottom'))
final_clip4 = CompositeVideoClip([final_clip4, text_clip4])



text5 = "5 KILLS"
text_clip5 = TextClip(text5, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_clip5.duration)
text_clip5 = text_clip5.set_position(('center', 'bottom'))
final_clip5 = CompositeVideoClip([final_clip5, text_clip5])

text6 = "YOU LOSE"
text_clip6 = TextClip(text6, fontsize=100, color='white', font='Arial', align='center', stroke_width=5).set_duration(final_cliplast.duration)
text_clip6 = text_clip6.set_position(('center', 'bottom'))
final_cliplast = CompositeVideoClip([final_cliplast, text_clip6])




# merging the clips
final_clip = concatenate_videoclips([final_clip1, final_clip2,final_clip3,final_clip4,final_clip5,final_cliplast])

# Save the extracted clips
final_clip.write_videofile("q1.mp4")

##############################





###############################
# Close the original video file
video.close()
