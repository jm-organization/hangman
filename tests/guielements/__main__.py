#!/usr/bin/env python
# coding=utf-8

import os

from soigne.components.game import Game
from soigne.container import App
from soigne.gamegui import GameGui, Image

# Инициализируем приложение
app = App(os.path.dirname(__file__))

app.NAME = 'guielements'
app.DESCRIPTION = 'Test game gui elements drawing'
app.URL = ''
app.VERSION = '0.1.0.test'

# Регистрируем дополнительные атрибуты приложения, необходимые для игры.
app.register('component', 'gui', GameGui)
app.register('component', 'game', Game)


def logic(game: Game, *args):
    game.gui.set_background('white')

    # game.gui.add('circle1', Circle(15, (255, 0, 0)), 25, 25)
    # game.gui.add('circle2', Circle(10, (175, 79, 136)), 65, 25)

    game.gui.add('mouse', Image(app.path('resources/mouse.jpg')), 210, 25)
    game.gui.add('earth-image1', Image(app.path('resources/earth.jpg'), width=128), 120, 25)
    game.gui.add('earth-image2', Image(app.path('resources/earth.jpg'), height=80), 210, 25)

    pass


game_application: Game = app.build('game')
game_application.start(logic)
