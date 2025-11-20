#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small test script for use with pillow_fight helper script.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def main(percentage=None):
    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    image = Image.new('1', (250, 122), 255)
    draw = ImageDraw.Draw(image)
    draw.text((7, 1), "Veh Smol Meshtastic Node", font=font, fill=0)

    # battery outline
    draw.rectangle((5, 30, 220, 100), outline=0, width=5)
    draw.rectangle((220, 50, 235, 80), outline=0, width=5, fill=0)

    if percentage is None:
        draw.text((20, 50), "Err: missing % param!", font=font, fill=0)
        return image

    percentage = int(percentage)
    # FIXME: refactor this ugly mess
    if percentage < 10:
        draw.text((20, 50), "Battery Empty!", font=font, fill=0)
        return image
    elif percentage > 10 and percentage < 26:
        draw.rectangle((15, 40, 60, 90), outline=0, width=0, fill=0)
    elif percentage >= 25 and percentage < 51:
        draw.rectangle((15, 40, 60, 90), outline=0, width=0, fill=0)
        draw.rectangle((65, 40, 110, 90), outline=0, width=0, fill=0)
    elif percentage >= 50 and percentage < 76:
        draw.rectangle((15, 40, 60, 90), outline=0, width=0, fill=0)
        draw.rectangle((65, 40, 110, 90), outline=0, width=0, fill=0)
        draw.rectangle((115, 40, 160, 90), outline=0, width=0, fill=0)
    elif percentage >= 75:
        draw.rectangle((15, 40, 60, 90), outline=0, width=0, fill=0)
        draw.rectangle((65, 40, 110, 90), outline=0, width=0, fill=0)
        draw.rectangle((115, 40, 160, 90), outline=0, width=0, fill=0)
        draw.rectangle((165, 40, 210, 90), outline=0, width=0, fill=0)

    return image

if __name__ == "__main__":
    current_script = os.path.basename(__file__)
    driver_script = current_script.replace("_pillow_", "")
    print(f"Don't run this script directly. Test using pillow_fight.py {current_script} or run the {driver_script} script")
