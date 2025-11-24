#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small test script for use with pillow_fight helper script.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def get_image():
    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    image = Image.new('1', (250, 122), 255)
    draw = ImageDraw.Draw(image)
    draw.text((1, 1), "Hello, World!", font=font, fill=0)
    # if rendering offline and you can't see all the lines, it's probably vscode terminal
    for i in range(1, 6, 1):
        draw.text((1, 20 * i), "1234567890123456789012", font=font, fill=0)

    return image

if __name__ == "__main__":
    print("Don't run this directly test using pillow_fight.py")
