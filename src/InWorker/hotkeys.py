from threading import Thread
import keyboard
from time import sleep
from random import randint

import InWorker.config as config

_running = False
_hotkey_pressed = {}


def _check_key_state():
    global _running, _hotkey_pressed

    while _running == True:
        for hotkey, properties in config.hotkeys.items():
            if (not keyboard.is_pressed(hotkey) and _hotkey_pressed[hotkey] == True):
                _hotkey_pressed[hotkey] = False

            if (keyboard.is_pressed(hotkey) and _hotkey_pressed[hotkey] == False):
                _hotkey_pressed[hotkey] = True
                properties[0]()
        sleep(0.05)


def start():
    global _running, _hotkey_pressed
    _running = True

    for hotkey, properties in config.hotkeys.items():
        _hotkey_pressed[hotkey] = False
        if (properties[1]):
            keyboard.block_key(hotkey)

    Thread(target=_check_key_state, daemon=True).start()


def stop():
    global _running, _hotkey_pressed
    _running = False
    _hotkey_pressed = dict()

    for hotkey in config.hotkeys:
        keyboard.unblock_key(hotkey)


def send_key(scan_code):
    sleep(randint(100, 200) / 1000)
    keyboard.send(scan_code)


def get_key_state(scan_code):
    return keyboard.is_pressed(scan_code)
