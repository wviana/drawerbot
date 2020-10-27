import sys
import tkinter

from io import BytesIO
from time import sleep

import numpy as np
import potrace
import requests

from PIL import Image, ImageTk
from ddg_image_selenium import search
from pynput.mouse import Button, Controller

def open_image(file_path):
    img = Image.open(file_path)
    img = img.convert('1')
    return np.array(img)

def image2paths(img_data):
    bmp = potrace.Bitmap(img_data)
    trace = bmp.trace()
    return list(map(lambda p: p.tesselate(), trace))

def find_maxXY(paths):
    maxX = max(map(lambda p: p[:, 0].max(), paths))
    maxY = max(map(lambda p: p[:, 1].max(), paths))
    return maxX, maxY

def draw(event):
    widget = event.widget
    paths = image2paths(widget.img_data)
    widget.root.destroy()

    paths.sort(reverse=True, key=lambda p: len(p))

    maxX, maxY = find_maxXY(paths)
    max_size = (350, 350)
    scale = min(max_size[0] / maxX, max_size[1] / maxY)

    print('Counting...')
    sleep(6)
    m = Controller()
    currentX, currentY = m.position
    for curve in paths:
        m.release(Button.left)
        for points in curve:
            # Scales and transpose points relative to mouse position
            x, y = np.array(points) * scale + np.array([currentX, currentY])
            m.position = (x, y)
            sleep(0.01)
            m.press(Button.left)
    m.release(Button.left)


if __name__ == '__main__':
    res = search(sys.argv[1])
    root = tkinter.Tk()

    row = 0
    columns = 6
    imgs = []
    for i, url in enumerate(res):
        img_data = BytesIO(requests.get(url).content)
        img = Image.open(img_data).resize((150, 150))
        img = ImageTk.PhotoImage(img)
        imgs.append(img)

        label = tkinter.Label(root, image=img)
        label.grid(row=row, column=i%columns)
        label.img_data = open_image(img_data) # Add image date for draw when click
        label.root = root # Add root element to destroy windows after select a image
        label.bind('<Button-1>', draw)

        # Every time fill a columns create a new line
        if i % columns == columns - 1:
            row+=1

        # Shows up just two rows
        if row == 2:
            break

    root.mainloop()
    sys.exit()


