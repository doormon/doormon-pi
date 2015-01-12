""" Input system module
"""

import RPi.GPIO as GPIO
import time


DOOR_OPEN = 1
DOOR_CLOSED = 0
PIN = 9
BOUNCE_LENGTH = 5
POLL_TIME = 0.1


def check_all_equal(lst):
    try:
        iterator = iter(lst)
        first = next(iterator)
        return all(first == rest for rest in iterator)
    except StopIteration:
        return True


class Input:
    """ Receives data in from the GPIO pins.
    """

    state = DOOR_CLOSED
    on_open = None
    on_close = None

    def __init__(self, on_open, on_close):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9, GPIO.IN)
        self.on_open = on_open
        self.on_close = on_close


    def start(self):
        # Detects a long period of open or close
        past_input = [DOOR_CLOSED]
        while True:
            input = GPIO.input(PIN)

            past_input.append(input)

            if len(past_input) > BOUNCE_LENGTH:
                # Remove old element to keep size to 5
                past_input.pop(0)

            # Check if we are currently transitioning states
            if not check_all_equal(past_input):
                continue

            if past_input[0] == DOOR_CLOSED:
                # Door currently closed
                if self.state == DOOR_OPEN:
                    # Was open, notify
                    self.on_close()
                    self.state = DOOR_CLOSED
            else:
                # Door currently open
                if self.state == DOOR_CLOSED:
                    # Was open, notify
                    self.on_open()
                    self.state = DOOR_OPEN

            # Wait for a bit
            time.sleep(POLL_TIME)
