#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small script to create the required pillow code to display graphics.
Eventually this will become a helper that allows you to test scripts before integrating them into your main code.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def hello_world():
    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    image = Image.new('1', (250, 122), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Hello, World!", font=font, fill=0)
    draw.text((10, 30), "1234567890123456789", font=font, fill=0)

    return image

if __name__ == "__main__":
    image = hello_world()
    file_name ="temp_pillow_fight_output.bmp"
    image.save(file_name)
    # check if we are running on MacOS or Linux based operating system
    if os.name == 'posix' and os.system("which magick") == 0 :
        os.system(f"magick {file_name} sixel:-")
    else:
        image.show() # this may not work on all systems
