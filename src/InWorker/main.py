from threading import Thread
from time import sleep
from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from psutil import Process

import InWorker.screen_scan as screen_scan
import InWorker.hotkeys as hotkeys
import InWorker.spheres as spheres
import InWorker.spells as spells
import InWorker.user_actions as user_actions

_runing = False


def check_active_process():
    global _runing

    while True:
        try:
            process_name = Process(GetWindowThreadProcessId(GetForegroundWindow())[1]).name().lower()
        except:
            process_name = ''

        if (process_name == 'dota2.exe' and _runing == False):
            _runing = True
            screen_scan.start()
            hotkeys.start()
            spheres.init()
            spells.init()
            user_actions.start()
            print('Start')
        elif (process_name != 'dota2.exe' and _runing == True):
            _runing = False
            screen_scan.stop()
            hotkeys.stop()
            user_actions.stop()
            print('Stop')
        sleep(0.2)


Thread(target=check_active_process).start()
