#!/usr/bin/env python
# coding=utf-8

import os

from soigne.components.game import Game
from soigne.container import App
from soigne.gamegui import GameGui, Image, Field

# Инициализируем приложение
app = App(os.path.dirname(__file__))

app.NAME = 'guielements'
app.DESCRIPTION = 'Test game gui elements drawing'
app.URL = ''
app.VERSION = '0.1.0.test'

# Регистрируем дополнительные атрибуты приложения, необходимые для игры.
app.register('component', 'gui', GameGui)
app.register('component', 'game', Game)


app.dispatch('application_build', lambda *args: args[0].get('component', 'gui').set_flags(GameGui.RESIZABLE))


def logic(game: Game, *args):
    game.gui.add('background', *Image(app.path('resources/perlin-noise.jpg'))
                 .fill(game.gui.window.get_width(), game.gui.window.get_height()))

    game.gui.add('mouse', Image(app.path('resources/mouse.jpg')), 210, 25)
    game.gui.add('earth-image1', Image(app.path('resources/earth.jpg'), width=128), 120, 25)
    game.gui.add('earth-image2', Image(app.path('resources/earth.jpg'), height=80), 210, 25)
    game.gui.add('earth-image3', Image(app.path('resources/earth.jpg'), width=150, height=80), 410, 25)

    game.gui.add('alpha-field', Field(background=(0, 0, 255), alpha=60, width=150, height=80), 410, 25)

    pass


game_application: Game = app.build('game')
game_application.start(logic)
