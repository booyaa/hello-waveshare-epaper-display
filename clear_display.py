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

from waveshare_epd import epd2in13b_V4 # pyright: ignore[reportMissingImports] # added manually (see above)

# DEBUG is noisy
logging.basicConfig(level=logging.WARNING)

def main():
    try:
        logging.info("Clear the display to avoid burn in")
        epd = epd2in13b_V4.EPD()
        epd.init()
        epd.Clear()

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
