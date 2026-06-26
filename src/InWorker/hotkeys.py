import keyboard
from threading import Thread
from time import sleep
from random import randint

import InWorker.config as config
import InWorker.user_actions as user_actions

_running = False
_hotkey_pressed = {}


def start():
    global _running, _hotkey_pressed
    _running = True

    for hotkey in config.key_binds['actions_exit']:
        _hotkey_pressed[hotkey] = False
    for hotkey, properties in config.user_hotkeys.items():
        _hotkey_pressed[hotkey] = False
        if (properties[1]):
            keyboard.block_key(hotkey)

    Thread(target=_check_key_state, daemon=True).start()


def stop():
    global _running
    _running = False

    for hotkey in config.user_hotkeys:
        keyboard.unblock_key(hotkey)


def _check_key_state():
    global _running, _hotkey_pressed

    while _running == True:
        for hotkey in config.key_binds['actions_exit']:
            if (not get_key_state(hotkey) and _hotkey_pressed[hotkey] == True):
                _hotkey_pressed[hotkey] = False
            if (get_key_state(hotkey) and _hotkey_pressed[hotkey] == False):
                _hotkey_pressed[hotkey] = True
                user_actions.clear_task_queue()

        for hotkey, properties in config.user_hotkeys.items():
            if (not get_key_state(hotkey) and _hotkey_pressed[hotkey] == True):
                _hotkey_pressed[hotkey] = False
            if (get_key_state(hotkey) and _hotkey_pressed[hotkey] == False):
                _hotkey_pressed[hotkey] = True
                Thread(target=user_actions.add_task,
                       args=(properties[0], get_key_state(config.key_binds['preparation_cast_mode'])),
                       daemon=True).start()
        sleep(0.05)


def get_key_state(scan_code):
    return keyboard.is_pressed(scan_code)


def key_send(scan_code):
    for hotkey in config.key_binds['actions_exit']:
        if (get_key_state(hotkey)):
            return
    keyboard.send(scan_code)
    sleep(randint(100, 200) / 1000)


def key_send_alt(scan_code):
    keyboard.press(56)
    keyboard.send(scan_code)
    keyboard.release(56)
    keyboard.send(scan_code)
    sleep(randint(100, 200) / 1000)
