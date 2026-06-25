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
            if (not get_key_state(hotkey) and _hotkey_pressed[hotkey] == True):
                _hotkey_pressed[hotkey] = False

            if (get_key_state(hotkey) and _hotkey_pressed[hotkey] == False):
                _hotkey_pressed[hotkey] = True
                properties[0]()
        sleep(0.01)


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


def get_key_state(scan_code):
    return keyboard.is_pressed(scan_code)


def key_send(scan_code):
    sleep(randint(140, 200) / 1000)
    keyboard.send(scan_code)


def key_press(scan_code):
    sleep(0.05)
    keyboard.press(scan_code)


def key_release(scan_code):
    keyboard.release(scan_code)
