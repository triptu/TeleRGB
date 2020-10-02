This is a simple working project to demonstrate linking Telegram Bot to arduino via a Python bridge. [Ardupy](https://github.com/tushutripathi/ardupy) is used to interface between Python and Arduino which allows Python to interact with Arduino which further interacts with the connected device.

# TeleRGB
Control on/off state and color of a RGB LED using Telegram Messenger. You can set any color in HTML/CSS color definitions. You can also send RGB values.

## How to use
* Upload the code in ardupy to arduino.
* Create a telegram bot. Don't know how to do that? Don't Worry, go [here.](https://core.telegram.org/bots#botfather)
* Change the variable token in rgbTelegram to the token you got.
* You are all set. Run rgbTelegram.py.
* You can send any color directly.
* For sending rgb values format is "rgb <rValue> <gValue> <bValue>" (without quotes or the comparison operators).
* Enjoy!

### Requirements
* Python2
* [Python-telegram-bot api](https://github.com/python-telegram-bot/python-telegram-bot)
* [Ardupy](https://github.com/tushutripathi/ardupy)
* [Webcolors](https://pypi.python.org/pypi/webcolors/)
* Arduino with a RGB LED connected to pin 9(red), 10(blue), 11(green).
