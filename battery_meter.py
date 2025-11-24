#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
import logging
import time
import helpers

picdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python','pic')
libdir = os.path.join((os.path.dirname(os.path.realpath(__file__))), 'lib', 'waveshare-epd', 'RaspberryPi_JetsonNano', 'python', 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)


# DEBUG can be noisy
logging.basicConfig(level=logging.WARNING)

def main():
    from waveshare_epd import epd2in13b_V4 # pyright: ignore[reportMissingImports] # added manually (see above)
    module_name = "get_image"
    this_script_file_name = os.path.basename(__file__)
    script_to_import = f"_pillow_{this_script_file_name}"
    if not os.path.isfile(script_to_import):
        exit(f"Error: {script_to_import} not found.")

    module = helpers.load_module_safely(module_name, script_to_import)
    params = sys.argv[1:] # FIXME: battery %

    if not hasattr(module, module_name):
        print(f"The module must have a '{module_name}' function.")
        sys.exit(1)

    try:
        logging.info("Initialize the display")
        epd = epd2in13b_V4.EPD()
        epd.init()
        epd.Clear()

        logging.info("Create a new bitmap")
        image = module.main(*params)

        logging.info("Push the bitmap to the display")

        # how to make the image black instead of red
        from PIL import Image, ImageDraw, ImageFont
        image2 = Image.new('1', (250, 122), 255) # create blank 1-bit white image

        image = image.rotate(180) # display orientation is wrong when in box
        epd.display(epd.getbuffer(image),epd.getbuffer(image2)) # black, red

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
