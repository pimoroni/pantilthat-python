# Pan-Tilt HAT

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/pantilthat-python/test.yml?branch=main)](https://github.com/pimoroni/pantilthat-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/pantilthat-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/pantilthat-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/pantilthat.svg)](https://pypi.python.org/pypi/pantilthat)
[![Python Versions](https://img.shields.io/pypi/pyversions/pantilthat.svg)](https://pypi.python.org/pypi/pantilthat)


https://shop.pimoroni.com/products/pan-tilt-hat

Pan-Tilt HAT is a two-channel servo driver designed to control a tiny servo-powered Pan/Tilt assembly. It also controls either PWM-dimmed lights or WS2812 pixels; up to 24 RGB or 18 RGBW.

# Installing

We'd recommend using this library with Raspberry Pi OS Bookworm or later. It requires Python ≥3.7.

## Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get you up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the commands exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
git clone https://github.com/pimoroni/pantilthat-python
cd pantilthat-python
./install.sh
```

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

## Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you can install the development version like so:

```bash
git clone https://github.com/pimoroni/pantilthat-python
cd pantilthat-python
./install.sh --unstable
```

## Install stable library from PyPi and configure manually

* Set up a virtual environment: `python3 -m venv --system-site-packages $HOME/.virtualenvs/pimoroni`
* Switch to the virtual environment: `source ~/.virtualenvs/pimoroni/bin/activate`
* Install the library: `pip install pantilthat`

In some cases you may need to us `sudo` or install pip with: `sudo apt install python3-pip`.

This will not make any configuration changes, so you may also need to enable:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

Some of the examples have additional dependencies. You can install them with:

```bash
pip install -r requirements-examples.txt
```

## Breakout Header Pinout

The breakout header on Pan Tilt HAT is connected directly to the GPIO pins.

Below is a map of the breakout functions and corresponding BCM pins:

| SDA | SCL | TX | RX | PWM | MOSI | MISO | SCLK | CEO |
| --- | --- | -- | -- | --- | ---- | ---- | ---- | --- |
| 2   | 3   | 14 | 15 | 18  | 10   | 9    | 11   | 8   |

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/pan-tilt-hat
* Function reference - http://docs.pimoroni.com/pantilthat/
* GPIO Pinout - https://pinout.xyz/pinout/pan_tilt_hat
* Get help - http://forums.pimoroni.com/c/support
