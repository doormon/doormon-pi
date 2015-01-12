""" Doormon module
"""

from doormon.input import Input
from doormon.post import send_message

class Doormon:
    """ Door monitoring system
    """

    input = None

    def __init__(self):
        def on_open():
            send_message('open')

        def on_close():
            send_message('close')

        self.input = Input(on_open, on_close)

    def start(self):
        self.input.start()
