#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small test script for use with pillow_fight helper script.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import qrcode

def get_image():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data('https://github.com/booyaa/hello-meshtastic/blob/main/MINTY_MOBILE_BBS.md')
    qr.make(fit=True)

    image_qr_code = qr.make_image(fill_color="black", back_color="white")
    image_qr_code = image_qr_code.resize((125, 125)) # type: ignore

    image = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets', 'snooze.bmp'))
    image.paste(image_qr_code, (130, 0))

    return image

if __name__ == "__main__":
    current_script = os.path.basename(__file__)
    driver_script = current_script.replace("_pillow_", "")
    print(f"Don't run this script directly. Test using pillow_fight.py {current_script} or run the {driver_script} script")
