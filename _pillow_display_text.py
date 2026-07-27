#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Send text to paper display
"""

import os
from PIL import Image, ImageDraw, ImageFont

def get_image(text="Hello, World!"):
    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')

    fontsize = 30
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), fontsize)
    image = Image.new('1', (250, 122), 255)
    draw = ImageDraw.Draw(image)
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    while w > 250:
        fontsize -= 1
        font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), fontsize)
        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        

    draw.text(((250 - w) / 2, (122 - h) / 2), text, font=font, fill=0)
    
    return image

if __name__ == "__main__":
    print("Don't run this directly test using pillow_fight.py")
