#!/usr/bin/env python
# coding=utf-8

import os

from hangman.components.configs import Configs
from hangman.components.game import Game
from hangman.components.l10n import Translation
from hangman.container import App
from hangman.gamegui import GameGui

from testgame.events import application_build, game_gui_drawn, game_initialization


def register_configs(app, configs, *args):
    return configs(app.path('configs/')).read()


def register_translator(app, translator, *args):
    return translator(app.path('resources/lang/'), app.get('config').l10n['default_language'])


# Инициализируем приложение
app = App(os.path.dirname(__file__))

app.NAME = 'testgame'
app.DESCRIPTION = 'Test game'
app.URL = ''
app.VERSION = '0.1.0.test'

# Регистрируем дополнительные атрибуты приложения, необходимые для игры.
app.register('config', Configs, registerer=register_configs)
app.register('translator', Translation, registerer=register_translator)
app.register('component', 'gui', GameGui)
app.register('component', 'game', Game)

# Регистрируем обработчики событий приложения.
app.dispatch('application_build', application_build)
app.dispatch('game_gui_drawn', game_gui_drawn)
app.dispatch('game_initialization', game_initialization)


def logic(*args):
    pass


game_application: Game = app.build('game')
game_application.start(logic)
