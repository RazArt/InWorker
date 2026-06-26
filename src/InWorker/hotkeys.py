import keyboard
import queue
from threading import Thread
from time import sleep
from random import randint

import InWorker.spells as spells
import InWorker.config as config

_running = False
_hotkey_pressed = {}
_keys_queue = None
_stop_keys_queue = False


def start():
    global _running, _hotkey_pressed, _keys_queue
    _running = True
    _keys_queue = queue.Queue(maxsize=100)

    for hotkey, properties in config.user_hotkeys.items():
        _hotkey_pressed[hotkey] = False
        if (properties[1]):
            keyboard.block_key(hotkey)

    Thread(target=_check_key_state, daemon=True).start()
    Thread(target=_send_keys_queue, daemon=True).start()


def stop():
    global _running, _keys_queue
    _running = False

    for hotkey in config.user_hotkeys:
        keyboard.unblock_key(hotkey)

    clear_keys_queue()


def _check_key_state():
    global _running, _hotkey_pressed, _stop_keys_queue

    while _running == True:
        if (get_key_state(config.key_binds['actions_exit_1']) or get_key_state(config.key_binds['actions_exit_2'])):
            _stop_keys_queue = True
            clear_keys_queue()

        for hotkey, properties in config.user_hotkeys.items():
            if (not get_key_state(hotkey) and _hotkey_pressed[hotkey] == True):
                _hotkey_pressed[hotkey] = False

            if (get_key_state(hotkey) and _hotkey_pressed[hotkey] == False):
                _hotkey_pressed[hotkey] = True
                Thread(target=properties[0], daemon=True).start()
        sleep(0.05)


def _send_keys_queue():
    global _stop_keys_queue

    while _running == True:
        try:
            key = _keys_queue.get()
            _keys_queue.task_done()
            sleep(randint(100, 200) / 1000)
            if (_running and not _stop_keys_queue):
                keyboard.send(int(key))
            print(f'{key=} отправили')
        finally:
            _stop_keys_queue = False
            sleep(0.05)


def clear_keys_queue():
    global _keys_queue

    while not _keys_queue.empty():
        try:
            _keys_queue.get(block=False)
            _keys_queue.task_done()
        except queue.Empty:
            continue
    print(f'Очередь очищена')


def get_key_state(scan_code):
    return keyboard.is_pressed(scan_code)


def key_send(scan_code):
    try:
        _keys_queue.put(scan_code)
        print(f'{scan_code=} поставлена в очередь')
    except queue.Full:
        return


def key_press(scan_code):
    sleep(0.05)
    keyboard.press(scan_code)


def key_release(scan_code):
    keyboard.release(scan_code)
