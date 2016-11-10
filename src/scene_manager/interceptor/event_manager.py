"""
Groups of functions in a module for all intents and purposes act like singletons in python
"""
from context import Context

instance = None
scene_manager = None
dispatchers = {}


def report_event(event):
    new_context = Context(scene_manager, event)
    for name, dispatcher in dispatchers.iteritems():
        if dispatcher.event_present(event.type):
            print name
            dispatcher.notify(new_context)


def register(dispatcher, name):
    dispatchers.update({
        name: dispatcher
    })


def unregister(name):
    dispatchers.pop(name, None)
