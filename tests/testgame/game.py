#!/usr/bin/env python
# coding=utf-8

from soigne.components.game import Game as BaseGame

from testgame.layouts import GameLayout


class Game(BaseGame):
    """ The game.
    """

    x, y, = 50, 50
    w, h = 40, 60
    speed = 5
    outset_x, outset_y = 50, 50

    pressed_key = ''

    def start(self, handler: callable = None, *args):
        self.gui.set_layout(GameLayout)

        super().start(handler, *args)
