#!/usr/bin/env python
# coding=utf-8

import os
import pygame
import json

from hangman.container import Component, Event


class GameGui(Component):
    """ Игровой интерфейс.

    Служит для управления интерфесом игры и обрабатывает игровые события.
    СОдержит в себе набор параметров и методов для добавления элементов интерфеса.
    """

    COMPONENTS = {}
    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
    }
    EVENTS = {
        pygame.QUIT: 'quit',
        pygame.ACTIVEEVENT: 'activeevent',
        pygame.KEYDOWN: 'keydown',
        pygame.KEYUP: 'keyup',
        pygame.MOUSEMOTION: 'mousemotion',
        pygame.MOUSEBUTTONUP: 'mousebuttonup',
        pygame.MOUSEBUTTONDOWN: 'mousebuttondown',
        pygame.JOYAXISMOTION: 'joyaxismotion',
        pygame.JOYBALLMOTION: 'joyballmotion',
        pygame.JOYHATMOTION: 'joyhatmotion',
        pygame.JOYBUTTONUP: 'joybuttonup',
        pygame.JOYBUTTONDOWN: 'joybuttondown',
        pygame.VIDEORESIZE: 'videoresize',
        pygame.VIDEOEXPOSE: 'videoexpose',
        pygame.USEREVENT: 'userevent',
    }

    FRAMES = 30

    DOUBLEBUF = pygame.DOUBLEBUF
    FULLSCREEN = -pygame.FULLSCREEN
    HWSURFACE = pygame.HWSURFACE
    NOFRAME = pygame.NOFRAME
    OPENGL = pygame.OPENGL
    RESIZABLE = pygame.RESIZABLE
    SCALED = pygame.SCALED

    dimensions = (800, 450)
    caption = 'GuiComponent'
    icon = None
    background = 'black'
    centred = True
    font = 'Arial'
    flags = 0
    depth = 0
    display = 0

    window = None
    element_states = None
    elements = {}

    def __init__(self, app):
        Component.__init__(self, app)
        pygame.init()
        self._register_components()

        # Регистрация событий игрвого интерфейса.
        self.app.register('event', 'quit', Event('quit'))
        self.app.register('event', 'activeevent', Event('activeevent'))
        self.app.register('event', 'keydown', Event('keydown'))
        self.app.register('event', 'keyup', Event('keyup'))
        self.app.register('event', 'mousemotion', Event('mousemotion'))
        self.app.register('event', 'mousebuttonup', Event('mousebuttonup'))
        self.app.register('event', 'mousebuttondown', Event('mousebuttondown'))
        self.app.register('event', 'joyaxismotion', Event('joyaxismotion'))
        self.app.register('event', 'joyballmotion', Event('joyballmotion'))
        self.app.register('event', 'joyhatmotion', Event('joyhatmotion'))
        self.app.register('event', 'joybuttonup', Event('joybuttonup'))
        self.app.register('event', 'joybuttondown', Event('joybuttondown'))
        self.app.register('event', 'videoresize', Event('videoresize'))
        self.app.register('event', 'videoexpose', Event('videoexpose'))
        self.app.register('event', 'userevent', Event('userevent'))

    def init(self):
        """ Метод инициализации игрового интерфейса.

        Регистрирует состояния элементов.
        Устанавливает параметры отрисовки игровго интерфейса и окна.
        """

        if self.centred:
            os.environ['SDL_VIDEO_CENTERED'] = '1'

        self.window = self.component('display').set_mode(self.dimensions, flags=self.flags, depth=self.depth, display=self.display)

        return self

    def color(self, name):
        """ Мотод получения цвета из цветовой палитры. """

        if name not in self.COLORS:
            raise NameError('Unknown colour <' + str(name) + '> name. You can use only: '
                            + str.join(', ', self.COLORS.keys()) + '.')

        return self.COLORS[name]

    def component(self, name='self'):
        """ Мотод получения компонента игрвого интерфеса. """

        if name == 'self':
            return self

        if name not in self.COMPONENTS:
            raise NameError('Unknown gui <' + name + '> component. There are only '
                            + str.join(', ', self.COMPONENTS.keys()) + ' component in GUI class.')

        return self.COMPONENTS[name]

    def element(self, name=None, x=None, y=None):
        """ Возвращает элементы интерфеса.

        При переданом имени, эллемент будет возвращён из списка по имени.

        В случае указания координат позиции, в списке будет найден эллемент,
        который пересекает указанную позицию.
        """

        element = None

        if name and x is None and y is None:
            if name not in self.elements:
                raise NameError('Unknown <' + name + '> element.')

            element = self.elements[name]
        elif x >= 0 and y >= 0:
            for el in self.elements.values():
                dimensions = el.get_rect()
                position = el.position

                if position[0] < x < position[0] + dimensions.width \
                        and position[1] < y < position[1] + dimensions.height:
                    element = el

        return element

    def set_colors(self, **colors):
        """ Добавляет переданные цвета к цветовой палитре. """

        for name, color in colors.items():
            if type(color) is not tuple:
                raise TypeError('Invalid color parameters. Expected tuple, ' + str(type(color)) + ' given.')

            self.COLORS[name] = color

        pass

    def set_dimensions(self, width=800, height=450):
        """ Устаналвивает размеры окна приложения.

        Небходимо вызывать перед инициализацией интерфеса.
        """

        self.dimensions = (width, height)

        pass

    def set_centered(self, centered=True):
        """ Устаналвивает правило, что окно приложенияи необходимо отрисовывть в центре экрана.

        Небходимо вызывать перед инициализацией интерфеса.
        """

        self.centred = centered

        pass

    def set_flags(self, flags: int):
        """ Устаналвивает флаги отрисовки интерфейса.
        """

        self.flags = flags

        pass

    def set_depth(self, depth: int):
        """ Устаналвивает количество бит для цвета.

        Обычно лучше не передавать аргумент глубины. По умолчанию будет установлена
        наилучшая и самая быстрая глубина цвета для системы.
        """

        self.depth = depth

        pass

    def set_display(self, display: int):
        """ Устаналвивает флаги отрисовки интерфейса.
        """

        self.display = display

        pass

    def set_icon(self, path, size=(32, 32)):
        """ Устаналвивает иконку окна приложения. """

        if not path:
            return False

        self.icon = self.component('image').load(path).convert_alpha()  # Создаём (загружаем) иконку

        self.icon.set_colorkey(self.color('black'))
        self.icon.blit(self.icon, size)

        return self.component('display').set_icon(self.icon)

    def set_caption(self, caption):
        """ Устаналвивает заголовок окна приложения. """

        self.caption = caption if caption else self.app.NAME

        return self.component('display').set_caption(self.caption)

    def set_background(self, color):
        """ Устаналвивает фон окна приложения. """

        if not color:
            return False

        self.background = color

        return self.window.fill(self.color(self.background))

    def add(self, name, element, x=0, y=0, parent=None, area=None, flags=0):
        """ Добавляет элемент интерфеса.

        В качестве элемента принимает объект типа pygame.Surface.

        Если был передан объект типа app.gamegui.Element в список добавляется данный объект,
        а указанные параметры после него перезаписывают соответствующие параметры указанного объекта.
        """

        if isinstance(element, pygame.Surface):
            self.elements[name] = Element(name, element, x, y, area, flags, parent)
        elif isinstance(element, Element):
            element.set_position(x, y)
            element.set_parent(parent)
            element.set_area(area)
            element.set_flags(flags)

            self.elements[name] = element
        else:
            raise TypeError('Unknown type of element ' + str(type(element)) + ". Тип элемента может быть <class 'pygame.Surface'> или <class 'app.gamegui.Element'>")

        pass

    def reset_elements(self):
        """ Очищает список элементов игрового интерфейса. """

        self.elements = {}

        pass

    def draw_elements(self):
        """ Отрисовывает текущие зарегистрированые элементы интерфейса.
        """

        with open(self.app.path('resources/element_states.json'), "r") as element_states:
            states = json.load(element_states)

        for element in self.elements.values():
            surface = self.window

            if element.parent is not None:
                surface = element.parent.subsurface(element.get_rect())

            for state in states:
                if element.name not in state['name']:
                    continue

                element.set_states(state['name'].replace(element.name, '').strip('.'), state['state'])

            surface.blit(*element.surface())

        pass

    def draw(self, callback=None, *args):
        """ Отрисовывает интерфейс приложения.

        Вызывает переданный обработчик после отрисовки.
        """

        self.update()

        if callable(callback):
            callback(*args)

        pass

    def update(self, redraw_gui=True):
        """ Обновляет игрвой интерфейс.

        При указанном ложном значении параметра redraw_gui элементы интерфейса перересованны не будут.
        """

        if redraw_gui:
            if self.icon:
                self.component('display').set_icon(self.icon)
            self.component('display').set_caption(self.caption)

            self.window.fill(self.color(self.background))

            self.draw_elements()

        self.component('display').update()

        pass

    def close(self):
        """ Завершение обработки игрвых событий и очистка игрвого интерфейса. """

        self.reset_elements()

        return self.component('display').quit()

    def _register_components(self):
        """ Регистрирует используемые компоненты для быстрого доступа. """
        self.COMPONENTS = {
            "display": pygame.display,
            "image": pygame.image,
            "drawer": pygame.draw,
            "event": pygame.event,
            "time": pygame.time,
            "key": pygame.key,
        }


class Element:
    """ Элемент интерфейса.
    """
    _surface = None
    name = ''
    position = (0, 0)
    area = None
    flags = 0
    parent = 0

    states = {}

    inited = False

    def __init__(self, name, surface, x=0, y=0, area=None, flags=0, parent=None):
        self._surface = surface
        self.name = name
        self.position = (x, y)
        self.area = area
        self.flags = flags
        self.parent = parent

        self.inited = True

    def surface(self):
        return [self._surface, self.position, self.area, self.flags]

    def get_rect(self):
        return self._surface.get_rect()

    def get_dimensions(self):
        return self.get_rect().width, self.get_rect().height

    def set_position(self, x, y):
        self.position = (x, y)
        pass

    def set_area(self, area):
        self.area = area
        pass

    def set_flags(self, flags):
        self.flags = flags
        pass

    def set_parent(self, parent):
        self.parent = parent
        pass

    def set_states(self, name, state):
        self.states[name] = state

        pass

    def change_state(self, **options):
        if len(options) != 0:
            pass

        pass

    def get_state(self, name):
        if name in self.states:
            return self.states[name]

        return {}

    def on_hover(self, game, window):
        self.change_state(**self.get_state('hovered'))
        pass

    def on_click(self, game, window):
        self.change_state(**self.get_state('clicked'))
        pass


class Text(Element):
    """ Текстовый элемент игрового интерфейса <app.gamegui.Text(Element)>.
    """

    text = ''
    color = ()
    fontsize = 0
    font = None

    def __init__(self, name, text, color, fontsize=60, font='Arial'):
        self.text = text
        self.fontsize = fontsize
        self.color = color

        self.font = pygame.font.SysFont(font, self.fontsize)

        super().__init__(name, self.font.render(self.text, 1, self.color))


class Button(Text):
    """ Кнопка игрового интерфейса <app.gamegui.Button(Element)>

    Для инициализации кнопки первым параметром необходимо передать обработчик нажатия кнопки.
    Помимо него указать следующие параметры:
        *name* - имя элемента
        *text* - отображаемый текст на кнопке
        *color* - цвет текста
        *font* - шрифт текста
        *fontsize* - размер текста
    """

    handler = None

    def __init__(self, handler=None, *args, **kwargs,):
        if handler is None:
            raise SyntaxError("Button mast have handler. There aren't in " + str(self) + '.')

        self.handler = handler

        super().__init__(*args, **kwargs)

    def on_hover(self, game, window):
        start = (self.position[0], self.position[1] + self._surface.get_rect().height)
        end = (self.position[0] + self._surface.get_rect().width, self.position[1] + self._surface.get_rect().height)

        pygame.draw.line(window, self.color, start, end)
        game.need_redraw_gui = False

        pass

    def on_click(self, game, window):
        game.need_redraw_gui = False
        handler = self.handler

        handler(game)

        pass


class Image(Element):
    def __init__(self, name, filename):
        super().__init__(name, pygame.image.load(filename))

    def convert_alpha(self):
        self._surface.convert_alpha()
