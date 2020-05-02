import os
import unittest

from soigne.components.game import Game
from soigne.container import App
from soigne.gamegui import GameGui

application = App(os.path.dirname(__file__))

application.NAME = 'application'
application.DESCRIPTION = 'Test application'
application.URL = ''
application.VERSION = '0.1.0.test'


class AppTestCase(unittest.TestCase):

    def test_app(self):
        self.assertIsInstance(application, App)

    def test_app_path(self):
        self.assertEqual(os.path.dirname(__file__), application.path(''))

    @staticmethod
    def register_game_components():
        application.register('component', 'gui', GameGui)
        application.register('component', 'game', Game)

    def test_app_build(self):
        self.register_game_components()

        self.assertIsInstance(application.build('game'), Game)


if __name__ == '__main__':
    unittest.main()
