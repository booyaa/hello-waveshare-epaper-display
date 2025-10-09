#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small test script for use with pillow_fight helper script.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import qrcode

def main():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data('https://github.com/booyaa/hello-meshtastic/blob/main/MINTY_MOBILE_BBS.md')
    qr.make(fit=True)

    image_qr_code = qr.make_image(fill_color="black", back_color="white")
    image_qr_code = image_qr_code.resize((125, 125)) # type: ignore

    picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')
    image = Image.open(os.path.join(picdir, '2in13b_V4b.bmp'))
    image.paste(image_qr_code, (130, 0))

    return image

if __name__ == "__main__":
    print("Don't run this directly test using pillow_fight.py")
