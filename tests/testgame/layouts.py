#!/usr/bin/env python
# coding=utf-8

from soigne.gamegui import Layout, Field, Text, Button
from testgame.game import Game


class QuitLayout(Layout):
    def resize(self, width, height):
        pass

    def elements(self):
        left_confirm = self.gui.window.get_width() / 2 - 255 / 2
        left_cancel = left_confirm + 135

        return [
            ('quit_question', Text('Are you sure that want to quit?', self.gui.color('black'), 20), 525, 180),

            ('button:quit_confirm_button', Button(text='Yes', width=120, height=40,
                                           background=self.app.path('resources/assets/button.png')), left_confirm, 225),
            ('button:quit_cancel_button', Button(text='No', width=120, height=40,
                                          background=self.app.path('resources/assets/button.png')), left_cancel, 225)
        ]

    def events(self):
        self.app.dispatch('off_quit_cancel_button_lclick', self.off_quit_cancel_button_lclick)
        self.app.dispatch('off_quit_confirm_button_lclick', self.off_quit_confirm_button_lclick)

    def off_quit_cancel_button_lclick(self, *args):
        self.gui.set_layout(GameLayout)

    def off_quit_confirm_button_lclick(self, *args):
        self.app.get('component', 'game').stopped = True


class GameLayout(Layout):
    def resize(self, width, height):
        pass

    def elements(self):
        game = self.app.get('component', 'game')

        return [
            ('player_field', Field(750, 750, self.gui.color('gray')), 50, 50),

            ('player', Field(game.w, game.h, self.gui.color('red')), game.x, game.y),

            ('quit_button_label', Text('Quit button: ', self.gui.color('black'), 20), 850, 55),
            ('button:quit_button', Button(text='Quit', width=120, height=40,
                                   background=self.app.path('resources/assets/button.png')), 850, 80),

            ('pressed_key', Text('Last pressed key: ' + game.pressed_key, self.gui.color('black'), 20), 55, 55),
            ('position', Text('Current position: x' + str(game.x) + ', y' + str(game.y), self.gui.color('black'), 20), 55, 80),
        ]

    def events(self):
        self.app.dispatch('off_quit_button_lclick', self.off_quit_button_lclick)

    def off_quit_button_lclick(self, *args):
        self.gui.set_layout(QuitLayout)
