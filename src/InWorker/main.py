from threading import Thread
from time import sleep
from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from psutil import Process

import keyboard

import InWorker.screen_scan as screen_scan
import InWorker.hotkeys as hotkeys
import InWorker.spheres as spheres

_runing = False
_thread = None


def check_active_process():
    global _runing

    while True:
        process_name = ''
        try:
            process_name = Process(GetWindowThreadProcessId(GetForegroundWindow())[1]).name()
        except:
            process_name = ''

        if (process_name == 'dota2.exe' and _runing == False):
            _runing = True
            screen_scan.start()
            hotkeys.start()
            spheres.init()
            print('Start')
        elif (process_name != 'dota2.exe' and _runing == True):
            _runing = False
            screen_scan.stop()
            hotkeys.stop()
            print('Stop')

        sleep(0.5)


def start():
    global _runing
    _runing = False

    Thread(target=check_active_process).start()


start()
