#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
import logging
import time
from PIL import Image,ImageDraw,ImageFont
import helpers

picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')
libdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python', 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13b_V4 # pyright: ignore[reportMissingImports] # added manually (see above)

logging.basicConfig(level=logging.DEBUG)

def main():
    module_name = "main"
    script_to_import = "hello_world.py"
    module = helpers.load_module_safely(module_name, script_to_import)

    if not hasattr(module, 'main'):
        print("The module must have a 'main' function.")
        sys.exit(1)

    try:
        # font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)

        logging.info("Initialize the display")
        epd = epd2in13b_V4.EPD()
        epd.init()
        epd.Clear()

        logging.info("Create a new bitmap")
        # image = Image.new('1', (250, 122), 255)  # 255: clear the frame
        # draw = ImageDraw.Draw(image)
        # draw.text((10, 10), "Hello, World!", font=font, fill=0)
        image = module.main()

        logging.info("Push the bitmap to the display")
        epd.display(epd.getbuffer(image),epd.getbuffer(image))

        logging.info("Goto Sleep...")
        epd.sleep()
        time.sleep(3)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13b_V4.epdconfig.module_exit(cleanup=True)
        exit()


if __name__ == "__main__":
    main()
