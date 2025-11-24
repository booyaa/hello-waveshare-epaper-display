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

logging.basicConfig(level=logging.DEBUG)

def main():
    from waveshare_epd import epd2in13b_V4 # pyright: ignore[reportMissingImports] # added manually (see above)

    module_name = "get_image"
    script_to_import = "_pillow_hello_world.py"
    module = helpers.load_module_safely(module_name, script_to_import)

    if not hasattr(module, module_name):
        print(f"The module must have a '{module_name}' function.")
        sys.exit(1)

    try:
        logging.info("Initialize the display")
        epd = epd2in13b_V4.EPD()
        epd.init()
        epd.Clear()

        logging.info("Create a new bitmap")
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
