# -*- coding: utf-8 -*-
"""
Pixel Color Extractor
This algorithm converts each pixel color from an image to an arduino code.
Just import the code into the arduino template, under a function, and
call that function to get the image on the display.

Esse programa converte a cor de cada pixel de imagem em um código de arduino.
Cole o código dentro do template do arduino, dentro de uma função, e chame
essa função para ter a imagem aparecendo no monitor.

@author: Pena
"""
from PIL import Image

### Convert RGB to Hex color 
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

#filename = "emoji_beijinho_08"
#filename = "emoji_passando_mal_03"
#filename = "emoji_piscadela_04"
#filename = "emoji_oohhh_03"
#filename = "emoji_grito_02"
#filename = "emoji_grito_05"
#filename = "emoji_risada_03"
filename = "cat_05"

### Open image file (should be 30x20 pixels, no transparency)
im = Image.open("imgs/"+filename+".png")
file = open("txts/"+filename+".txt", 'w')
pixel = im.load()
column, row = im.size

### Iterate over image and write each pixel color on txt file.
n = 0
for j in range(row): 
    for i in range(column):
        r, g, b = pixel[i, j]
        string = rgb2hex(r, g, b)
        if j % 2:
            x = j*column + (column - i) - 1
        else:
            x = n
        file.write(string.replace("#", "leds["+str(x)+"] = 0x")+";")
        n += 1
    file.write("\n")
file.close()
