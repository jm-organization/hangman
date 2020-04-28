#!/usr/bin/env python
# coding=utf-8
from gamegui import GameGui
from hangman.components.game import Game
from hangman.components.l10n import __


def application_build(app, event):
    """ Метод обработки события при сборке приложения.

    Вы можете сдесь предустановить какие либо параметры.
    К примеру это могут быть размеры окна интерфейса вашего приложения.

    Изменения параметров интерфейса на этом этапе не доступны.
    """

    app.get('component', 'gui').set_dimensions(1300, 850)
    app.get('component', 'gui').set_flags(GameGui.RESIZABLE | GameGui.SCALED)

    pass


def game_initialization(app, event, game):
    """ Метод обработки события инициализации игры.

    Вы можете сдесь предустановить какие либо параметры отображаения интерфеса игрового приложения.
    К примеру это могут быть заголовок окна, его иконка, фон.
    """

    game.gui.set_colors(
        red=(255, 0, 0)
    )

    game.gui.set_background('white')
    game.gui.set_caption('Hello World!')
    # game.gui.set_icon(game.app.path('icon.ico'))

    pass


def game_gui_drawn(app, event, game: Game):
    """ Метод обработки события завершения отрисовки интерфейса.

    Укажите какие элементы интерфейса необходимо отрисовать на данном этапе.
    """

    pass
