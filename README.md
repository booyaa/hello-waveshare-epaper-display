# Waveshare e-Paper Display

I've got a 2.13 inch e-Paper [HAT][ws_main] by Waveshare. I've created this repo for experimenting on the best ways to push data onto it.

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

## Troubleshooting

### Verifying device works

Use this set up to verify you have a working display before proceeding to examples. If Waveshare's own example script doesn't work, you're not going to be able to run the examples in this repo

I'm looking to simplify this, the original [instructions][ws_setup] are both confusing and don't work. Also they're using the terrible practice of install python modules as system dependencies. Always use virtual environments unless you're in a container!`</soapbox>`.

```sh
git clone https://github.com/waveshare/e-Paper.git
cd e-Paper/
uv venv
source .venv/bin/activate
sudo apt install swig liblgpio-dev
uv pip install pillow numpy spidev rpi-lgpio lgpio swig gpiozero
python RaspberryPi_JetsonNano/python/examples/epd_2in13b_V4_test.py
```

### Git submodules

Depending on how you authenticate to GitHub you may need to create a ssh key and add it to [GitHub](https://github.com/settings/keys). That or switch the submodule to HTTP (if you're using the GitHub CLI to authenticate).

<!-- linkies -->
[ws_main]: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Resources
[ws_setup]: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Python
