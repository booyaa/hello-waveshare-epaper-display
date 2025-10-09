# Waveshare e-Paper Display

I've got a 2.13 inch e-Paper [HAT][ws_main] by Waveshare. I've created this
repo for experimenting on the best ways to push data onto it.

## Specification

- Resolution: 250 x 122 pixels

## Resources

- Waveshare [wiki][ws_main] page for the hat
- [Pillow](https://pillow.readthedocs.io/en/stable/) PIL's successor

## Set up

> [!IMPORTANT]
> This repo assume you have already set up your display and verified it's
> working. If you're still trying to set up your device, please refer to the
> [troubleshooting](#troubleshooting) section below.

```sh
git clone git@github.com:booyaa/hello-waveshare-epaper-display.git
cd hello-waveshare-epaper-display
git submodule update # see troubleshooting if this fails
uv venv # initialise environment
# follow on screen instructons for your operating system to activate environment
uv sync # pull in deps - if you're not using uv then use `pip install -r requirements.txt'
```

Try out examples!

## Creating new graphics without an e-Paper

If you've been playing around with e-Paper displays you'll not very quick. On
average refresh the display can take up to 50 seconds on a Pi Zero 2 (with all
4 cores enabled).

Or maybe you want to develop on a different computer to the one that runs the
code. Since most of the heavy lifting is done by Pillow all you need to do is
modularise your code and with a bit of importlib magick you can develop
"offline" and reuse the same script when you go "live".

An example of how to do this can be found in the following scripts:

- hello_world.py - This script is pure Pillow and has a single function called
main that will return an image. You don't run this script directly, instead you
wrap it in a stand alone script like main.py
- main.py - This script will drive the e-Paper display using the image generated
by the hello_world script.
- pillow_fight.py - This script to test your new Pillow scripts

## Troubleshooting

### Verifying device works

Use this set up to verify you have a working display before proceeding to examples. If Waveshare's own example script doesn't work, you're not going to be able to run the examples in this repo

I'm looking to simplify this, the original [instructions][ws_setup] are both confusing and don't work. Also they're using the terrible practice of install python modules as system dependencies. Always use virtual environments unless you're in a container!`</soapbox>`.

```sh
git clone https://github.com/waveshare/e-Paper.git
cd e-Paper/
uv venv --python 3.13 # tested against 3.13.6
source .venv/bin/activate
sudo apt install swig liblgpio-dev
uv pip install pillow spidev rpi-lgpio gpiozero
python RaspberryPi_JetsonNano/python/examples/epd_2in13b_V4_test.py
```

### Git submodules

Depending on how you authenticate to GitHub you may need to create a ssh key and add it to [GitHub](https://github.com/settings/keys). That or switch the submodule to HTTP (if you're using the GitHub CLI to authenticate).

<!-- linkies -->
[ws_main]: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Resources
[ws_setup]: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Python
