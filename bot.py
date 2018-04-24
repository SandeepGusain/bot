import time
import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *


class Coord:
    replay_btn = (1037, 387)
    dino_duck = (880, 408)


def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


def duck():
    pyautogui.keyDown('down')


def jump_obstacle():
    box = (Coord.dino_duck[0] + 80, Coord.dino_duck[1], Coord.dino_duck[0] + 120, Coord.dino_duck[1] + 10)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    return a.sum()


def duck_obstacle():
    box = (Coord.dino_duck[0] - 54, Coord.dino_duck[1], Coord.dino_duck[0] + 30, Coord.dino_duck[1] + 10)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = array(grayimage.getcolors())
    return a.sum()


def main():
    pyautogui.click(Coord.replay_btn)
    while True:
        print(duck_obstacle())
        if jump_obstacle() != 647:
            jump()
        if duck_obstacle() == 1087:
            duck()


main()
