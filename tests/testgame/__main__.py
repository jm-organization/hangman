#!/usr/bin/env python
# coding=utf-8

import os

from soigne.components.configs import Configs
from soigne.components.l10n import Translation
from soigne.container import App
from soigne.gamegui import GameGui

from testgame.events import application_build, game_gui_drawn, game_initialization
from testgame.layouts import GameLayout
from testgame.logic import logic
from testgame.game import Game


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

game_application: Game = app.build('game')
game_application.gui.set_layout(GameLayout)
game_application.start(logic)
