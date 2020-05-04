#!/usr/bin/env python
# coding=utf-8

from pygame.constants import *

from testgame.game import Game
from testgame.layouts import GameLayout


def logic(game: Game, *args):
    if game.gui.active_layout is GameLayout:
        if game.pressed_keys[K_UP] and game.y >= game.speed + game.outset_y:
            game.pressed_key = 'Top arrow'
            game.y -= game.speed

        if game.pressed_keys[K_DOWN] and game.y <= game.gui.window.get_height() - (game.h + game.speed + game.outset_y):
            game.pressed_key = 'Down arrow'
            game.y += game.speed

        if game.pressed_keys[K_LEFT] and game.x >= game.speed + game.outset_x:
            game.pressed_key = 'Left arrow'
            game.x -= game.speed

        if game.pressed_keys[K_RIGHT] and \
                game.x <= game.gui.window.get_width() - (game.w + game.speed + (game.gui.window.get_width() - 750) - game.outset_x):
            game.pressed_key = 'Right arrow'
            game.x += game.speed

    game.gui.draw_active_layout()
