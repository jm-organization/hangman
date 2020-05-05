#!/usr/bin/env python
# coding=utf-8


class App:
    """ Main application class.
    """

    NAME = 'python-application'
    DESCRIPTION = 'Python application'
    URL = ''
    VERSION = 'v0.1.0'

    _unknown_event_error = 'Unknown <%d> event.'

    _path = './'

    _components = {}
    _events = {}

    def __init__(self, path='./'):
        self.register('event', 'application_build', Event('application_build'))
        self.register('event', 'application_built', Event('application_built'))

        self._path = path

    def path(self, path):
        return self._path + '/' + path

    def get(self, attr, name=None):
        """ Returns application attribute.

        :param attr - attribute type.
        :param name - attribute name.
        """

        attribute = '_' + attr + 's'

        if attribute not in dir(self):
            raise NameError('Unknown application attribute <' + attr + '>.')

        attribute = self.__getattribute__(attribute)

        if name is None:
            return attribute

        if name not in attribute:
            raise NameError('Unknown application ' + attr + ' <' + name + '>.')

        return attribute[name]

    def build(self, component):
        """ Build application method.

        You should provide your primary component name that
        has build method for start your app.

        :returns result of component build method.
        """

        self.trigger_event('application_build')

        component = self.get('component', component)
        component = component.build()

        self.trigger_event('application_built')

        return component

    def register(self, t, *options, registerer=None):
        """ Registers application attributes.

        Attribute name can be string with latin letters? numbers and underscores.
        """

        attribute = '_register_' + t + 's'

        # Raise an error if attribute registerer not defined in app and it wasn't given.
        if attribute not in dir(App) and not callable(registerer):
            raise NameError('Unknown registration name <' + t + '>.')

        # Register attribute if registerer is callable.
        # Custom registerer has high priority and we check and call it firstly.
        if callable(registerer):
            self.__setattr__('_' + t + 's', registerer(self, options[0], *options))
            return

        # Otherwise we call defined app attribute registerer.
        registerer = self.__getattribute__(attribute)
        registerer(options)

    def dispatch(self, event, handler):
        """ Sets event handler.
        """

        if event not in self._events:
            raise SystemError(self._unknown_event_error % event)

        self._events[event].append_handler(handler)

    def is_triggerable(self, name):
        return name in self._events

    def trigger_event(self, name, *args, **kwargs):
        if name not in self._events:
            raise SystemError(self._unknown_event_error % name)

        self._events[name].trigger(self, *args, **kwargs)

    def remove_event(self, name, no_errors=False):
        if name not in self._events and not no_errors:
            raise SystemError(self._unknown_event_error % name)

        del self._events[name]

    def _register_events(self, options):
        if type(options[1]) is not Event:
            raise TypeError('Registered event mast be type of app.container.Event')

        self._events[options[0]] = options[1]

    def _register_components(self, options):
        component = options[1]

        if not issubclass(component, Component):
            raise TypeError('Registered component mast be type of app.container.Component')

        self._components[options[0]] = component(self)


class Component:
    app = App

    def __init__(self, app):
        self.app = app

    def trigger_event(self, name, *args, **kwargs):
        self.app.trigger_event(name, *args, **kwargs)


class Event:
    name = ''
    handlers = []

    data = None

    def __init__(self, name):
        self.name = name
        self.handlers = []

    def append_handler(self, handler):
        self.handlers.append(handler)

    def trigger(self, app, *args, **kwargs):
        for handler in self.handlers:
            handler(app, self, *args, **kwargs)
