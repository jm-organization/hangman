#!/usr/bin/env python
# coding=utf-8

from soigne.components.game import Game as BaseGame


class Game(BaseGame):
    x, y, = 50, 50
    w, h = 40, 60
    speed = 5
    outset_x, outset_y = 50, 50

    pressed_key = ''
