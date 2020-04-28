#!/usr/bin/env python
# coding=utf-8
from gamegui import GameGui
from hangman.container import Component, Event


class Game(Component):
    """ Главный класс игры.
    Точка вхождения для взаимодействия пользователя с игрой.
    """
    resources = 'resources/assets/'

    gui: GameGui = None

    pressed_keys = {}
    need_redraw_gui = True
    stopped = True

    def __init__(self, app):
        super().__init__(app)

        self.app.register('event', 'game_initialization', Event('game_initialization'))
        self.app.register('event', 'game_gui_drawn', Event('game_gui_drawn'))

        self.app.dispatch('quit', on_quit)
        self.app.dispatch('activeevent', on_activeevent)
        self.app.dispatch('keydown', on_keydown)
        self.app.dispatch('keyup', on_keyup)
        self.app.dispatch('mousemotion', on_mousemotion)
        self.app.dispatch('mousebuttonup', on_mousebuttonup)
        self.app.dispatch('mousebuttondown', on_mousebuttondown)
        self.app.dispatch('joyaxismotion', on_joyaxismotion)
        self.app.dispatch('joyballmotion', on_joyballmotion)
        self.app.dispatch('joyhatmotion', on_joyhatmotion)
        self.app.dispatch('joybuttonup', on_joybuttonup)
        self.app.dispatch('joybuttondown', on_joybuttondown)
        self.app.dispatch('videoresize', on_videoresize)
        self.app.dispatch('videoexpose', on_videoexpose)
        self.app.dispatch('userevent', on_userevent)

        self.resources = self.app.path(self.resources)

    def build(self):
        """ """
        self.gui = self.app.get('component', 'gui')

        # Отрисовываем окно игры.
        self.gui.init()

        self.trigger_event('game_initialization', self)

        self.gui.draw(self._handle_drawn_gui)

        return self

    def start(self, handler=None, *args):
        """ Метод запуска цикла обработки игровых событий.
        Обновляет окно игры, запускает обработчики событий.

        :param handler: Обработчик событий
        """
        gui_events = self.gui.component('event')

        self.stopped = False
        while not self.stopped:
            self.gui.component('time').Clock().tick(self.gui.FRAMES)

            for event in gui_events.get():
                if event.type not in self.gui.EVENTS:
                    continue

                self.trigger_event(self.gui.EVENTS[event.type], self, event)

            self.pressed_keys = self.gui.component('key').get_pressed()

            if handler:
                handler(*args)

            self.gui.update(self.need_redraw_gui)

        # Завершаем игру при нажатии клавиши выхода из игры (или закрытия окна).
        self.gui.close()

    def stop(self):
        self.stopped = True

        # self.gui.close()

    def _handle_drawn_gui(self, *args):
        self.trigger_event('game_gui_drawn', self, *args)


def on_quit(app, event, game, game_event):
    game.stopped = True
    pass


def on_activeevent(app, event, game, game_event):
    pass


def on_keydown(app, event, game, game_event):
    pass


def on_keyup(app, event, game, game_event):
    pass


def on_mousemotion(app, event, game, game_event):
    game.need_redraw_gui = True

    element = game.gui.element(None, *game_event.pos)
    if not element:
        return

    element.on_hover(game, game.gui.window)


def on_mousebuttonup(app, event, game, game_event):
    game.need_redraw_gui = True

    element = game.gui.element(None, *game_event.pos)
    if not element:
        return

    element.on_click(game, game.gui.window)
    pass


def on_mousebuttondown(app, event, game, game_event):
    pass


def on_joyaxismotion(app, event, game, game_event):
    pass


def on_joyballmotion(app, event, game, game_event):
    pass


def on_joyhatmotion(app, event, game, game_event):
    pass


def on_joybuttonup(app, event, game, game_event):
    pass


def on_joybuttondown(app, event, game, game_event):
    pass


def on_videoresize(app, event, game, game_event):
    pass


def on_videoexpose(app, event, game, game_event):
    pass


def on_userevent(app, event, game, game_event):
    pass

