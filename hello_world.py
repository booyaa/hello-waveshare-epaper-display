#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small test script for use with pillow_fight helper script.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def main():
    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    image = Image.new('1', (250, 122), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Hello, World!", font=font, fill=0)
    draw.text((10, 30), "1234567890123456789", font=font, fill=0)

    return image

if __name__ == "__main__":
    print("Don't run this directly test using pillow_fight.py")
