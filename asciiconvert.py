import numpy as np
from math import sqrt
from PIL import Image, ImageDraw, ImageFont


density = '       .:-i|=+%O#@' #16x16 pixels characters
density = ' .,-~:;=!*#$@'
#density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.     "
STEP = 10
verdana_font = ImageFont.truetype("verdana.ttf", STEP, encoding="unic") #FONT

def getAverageL(image,w,h):
 
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)
 
    # get shape
    
# img = img.sum(2) / (255*3) # converting to grayscale
 
    # get average
    res = np.dot(im[...,:3], [0.2989, 0.5870, 0.1140])
    return res
    #return im.sum(2) / (255*3)

def meanBrightness(avrgIMG,i,j,step): #returns meanBrightness value of the [i,j,i+step,j+step] square
    meanBright = 0
    pixelCount = 0 #to avoid counting too many pixels on borders
    for ki in range(i,i+step):
        for kj in range(j,j+step):
            try:
                meanBright += avrgIMG[i][j]
                pixelCount +=1
            except:
                pass
    if pixelCount == 0:
        return 0
    else:
        return meanBright/(255*pixelCount)

def mapBrightToCharacter(brightValue,density):
    return density[int((len(density)-1)*brightValue)]

def dist(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def replaceColor(oldC,palette):
    minDist = dist(oldC,palette[0])
    minC = palette[0]
    for color in palette:
        if dist(oldC,color) <= minDist:
            minDist = dist(oldC,color)
            minC = color
    return minC
   
def convertToAscii(image,density,h,w):
    resgray = getAverageL(image,h,w)
    res = Image.new("RGB", (w,h), (0,0,0))
    for i in range(0,w,STEP):
        for j in range(0,h,STEP):
            draw = ImageDraw.Draw(res)
            txt = mapBrightToCharacter(meanBrightness(resgray,i,j,STEP),density)
            draw.text((i,j), txt, font=verdana_font)
    res = res.transpose(Image.ROTATE_270)
    #pil_img = Image.fromarray(res)
    res.save('res.png')
    print("SAVED")
    return 'res.png'
