# DrawerBot

Is a bot that searches monochromatic cliparts in duckduckgo, transforms it into segments, and draws it using the mouse.
May be useful for online drawing games like skribbl or gartic.io.

## Dependences

You'll need to install potrace and geckodriver.
Also the follow python packages, that may be installed throw pip:

- pillow
- pynput
- pypotrace
- requests
- selenium

## How to use

python main.py <word_to_search>

Ex: python main.py horse.

It will pop a window, so you select which picture do you want to be drawn. After selected you have 6 seconds to place the mouse in the window you want to draw the picture. The mouse position will be the most top-left of the picture.

## TODO

[ ] Add parameters to image size and sleep time between points
[ ] Improve readme.
