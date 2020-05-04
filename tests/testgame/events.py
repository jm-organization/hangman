#!/usr/bin/env python
# coding=utf-8

from soigne.components.game import Game
from soigne.gamegui import GameGui


def application_build(app, event):
    app.get('component', 'gui').set_dimensions(1300, 850)
    app.get('component', 'gui').set_flags(GameGui.RESIZABLE)

    app.get('component', 'gui').FRAMES = 30


def game_initialization(app, event, game):
    game.gui.set_colors(
        red=(255, 0, 0),
        gray=(144, 144, 144)
    )

    game.gui.set_background('white')
    game.gui.set_caption('Hello World!')


def game_gui_drawn(app, event, game: Game):
    pass
