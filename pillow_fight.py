#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
A small script to create the required pillow code to display graphics.
Eventually this will become a helper that allows you to test scripts before integrating them into your main code.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import helpers

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 pillow_fight.py <script_to_import>")
        print("Example: python3 pillow_fight.py hello_world.epd.py")
        sys.exit(1)

    module_name = "main"
    script_to_import = sys.argv[1]

    module = helpers.load_module_safely(module_name, script_to_import)

    if hasattr(module, 'main'):
        image = module.main()
    else:
        print("The module must have a 'main' function.")
        sys.exit(1)

    file_name = "temp_pillow_fight.bmp"
    image.save(file_name)
    # Use ImageMagick's sixel support for faster display in terminal if available
    if os.name == 'posix' and os.system("which magick 2>&1 > /dev/null") == 0 :
        print("\n") # VS Code Terminal eats up images
        os.system(f"magick {file_name} sixel:-")
        print("\n") # VS Code Terminal eats up images
    else:
        image.show() # this may not work on all systems
