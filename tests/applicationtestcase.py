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

    def test_app_has_flags(self):
        self.register_game_components()
        application.get('component', 'gui').set_flags(GameGui.OPENGL | GameGui.DOUBLEBUF | GameGui.RESIZABLE)

        self.test_app_has_flag1()
        self.test_app_has_flag2()
        self.test_app_has_flag3()
        self.test_app_has_flag4()
        self.test_app_has_flag5()

    def test_app_has_flag1(self):
        self.assertTrue(application.get('component', 'gui').has_flag(GameGui.OPENGL))

    def test_app_has_flag2(self):
        self.assertFalse(application.get('component', 'gui').has_flag(GameGui.HWSURFACE))

    def test_app_has_flag3(self):
        self.assertTrue(application.get('component', 'gui').has_flag(GameGui.RESIZABLE))

    def test_app_has_flag4(self):
        self.assertTrue(application.get('component', 'gui').has_flag(GameGui.DOUBLEBUF))

    def test_app_has_flag5(self):
        self.assertFalse(application.get('component', 'gui').has_flag(GameGui.FULLSCREEN))


if __name__ == '__main__':
    unittest.main()
