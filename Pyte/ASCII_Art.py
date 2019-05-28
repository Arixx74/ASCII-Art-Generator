#   ASCII Art:
#       Convert an image to a collection of ascii symbols to be perceived as the image

import sys, random, argparse
import numpy as np
import math
from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " 
# 10 levels of gray
gscale2 = "@%#*+=-:. "

gscale3 = "-:. "

def getAverage(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))

def convertImageToAscii(file_name, cols, scale, more_levels):
    global gscale1, gscale2
    image = Image.open(file_name).convert('L')
    W, H = image.size[0], image.size[1]
    print("input image dimensions: %d x %d" % (W, H))
    w = W / cols
    #print(scale)
    h = w / scale
    rows = int(H / h)
    print("columns: %d, rows: %d" % (cols, rows))
    print("tile dimensions: %d x %d" %(w, h))
    
    aimg = []
    #check if image size is too small
    if cols > W or rows > H:
        #print("image size is too small for specified number of columns!")
        aimg.append('Image size is too small!')
        return aimg

    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j+1) * h)
        if j == rows - 1:
            y2 = H
        aimg.append("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = getAverage(img)
            if more_levels:
                gsval = gscale1[int((avg / 255) * 69)]
            else:
                gsval = gscale2[int((avg / 255) * 9)]
                #gsval = gscale3[int(avg / 255) * 3]
            aimg[j] += gsval
    return aimg

def main(imgPath, res = 500, mode = True, scale = 0.43):
    #print(type(scale))
    #print(scale)
    #res = int(res)
    aimg = convertImageToAscii(imgPath, res, scale, mode)
    print("OK")
    art = ''
    #fout = open(outFilePath, 'w')
    for row in aimg:
        #fout.write(row + '\n')
        art += row + '\n'
    #fout.close()

    #print("the ASCII art is generated at file %s" % outFilePath)
    return art

if __name__ == '__main__':
    print(main('def.jpg', 300, True))