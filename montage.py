from moviepy.editor import *
import numpy as np
import matplotlib.pyplot as plt
from asciiconvert import convertToAscii, density
from PIL import Image, ImageDraw, ImageFont

FPS = 30



def montage():
    clip = VideoFileClip("clip.mp4")
    duration = clip.duration
    audioclip = clip.audio

    newClips = []
    dt = 1/FPS
    t = 0

    while t < clip.duration:
        print(int(t/duration*1000)/1000)
        frame = clip.get_frame(t)
        image = Image.fromarray(frame)
        plt.imshow(image)
        print(convertToAscii(image,density,image.size[0],image.size[1]))
        newClips.append(ImageClip('res.png').set_duration(dt))
        t += dt
    final = concatenate_videoclips(newClips).set_audio(audioclip)
    final.write_videofile("final.mp4",fps=FPS)