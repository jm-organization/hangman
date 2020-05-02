#!/usr/bin/env python
# coding=utf-8

from pygame.constants import *

from soigne.components.game import Game
from soigne.gamegui import Text, Field, Button, Layout


class QuitLayout(Layout):
    def elements(self):
        left_confirm = self.gui.window.get_width() / 2 - 255 / 2
        left_cancel = left_confirm + 135

        return [
            ('quit_question', Text('Are you sure that want to quit?', self.gui.color('black'), 20), 525, 180),

            ('quit_confirm_button', Button(text='Yes', width=120, height=40,
                                           background=self.app.path('resources/assets/button.png')), left_confirm, 225),
            ('quit_cancel_button', Button(text='No', width=120, height=40,
                                          background=self.app.path('resources/assets/button.png')), left_cancel, 225)
        ]

    def events(self):
        self.app.dispatch('off_quit_cancel_button_lclick', off_quit_cancel_button_lclick)
        self.app.dispatch('off_quit_confirm_button_lclick', off_quit_confirm_button_lclick)


class GameLayout(Layout):
    def elements(self):
        return [
            ('player_field', Field(750, 750, self.gui.color('gray')), 50, 50),

            ('player', Field(w, h, self.gui.color('red')), x, y),

            ('quit_button_label', Text('Quit button: ', self.gui.color('black'), 20), 850, 55),
            ('quit_button', Button(text='Quit', width=120, height=40,
                                   background=self.app.path('resources/assets/button.png')), 850, 80),

            ('pressed_key', Text('Last pressed key: ' + pressed_key, self.gui.color('black'), 20), 55, 55),
            ('position', Text('Current position: x' + str(x) + ', y' + str(y), self.gui.color('black'), 20), 55, 80),
        ]

    def events(self):
        self.app.dispatch('off_quit_button_lclick', off_quit_button_lclick)


x, y, = 50, 50
w, h = 40, 60
speed = 5
outset_x, outset_y = 50, 50

pressed_key = ''

active_layout = GameLayout


def logic(game: Game, *args):
    global x, y, speed, pressed_key

    if active_layout is GameLayout:
        if game.pressed_keys[K_UP] and y >= speed + outset_y:
            pressed_key = 'Top arrow'
            y -= speed

        if game.pressed_keys[K_DOWN] and y <= game.gui.window.get_height() - (h + speed + outset_y):
            pressed_key = 'Down arrow'
            y += speed

        if game.pressed_keys[K_LEFT] and x >= speed + outset_x:
            pressed_key = 'Left arrow'
            x -= speed

        if game.pressed_keys[K_RIGHT] and \
                x <= game.gui.window.get_width() - (w + speed + (game.gui.window.get_width() - 750) - outset_x):
            pressed_key = 'Right arrow'
            x += speed

    active_layout(game.gui).draw()

    pass


def off_quit_button_lclick(*args):
    global active_layout

    active_layout = QuitLayout

    pass


def off_quit_cancel_button_lclick(*args):
    global active_layout

    active_layout = GameLayout

    pass


def off_quit_confirm_button_lclick(*args):
    game, game_event = args[2], args[3]

    game.stopped = True

    pass
