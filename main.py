import moviepy.editor as mp

video = mp.VideoFileClip("Pexels Videos 4703.mp4")

logo = (mp.ImageClip("alatoo.png")
          .set_duration(video.duration)
          .resize(height=150) # if you need to resize...
          .margin(right=8, bottom =8, opacity=0) # (optional) logo-border padding
          .set_pos(("right","bottom")))

final = mp.CompositeVideoClip([video, logo])
final.write_videofile("test.mp4")