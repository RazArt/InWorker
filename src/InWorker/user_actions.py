import queue
from threading import Thread
from time import sleep

import InWorker.spheres as spheres
import InWorker.spells as spells
import InWorker.screen_scan as screen_scan
import InWorker.hotkeys as hotkeys

_tasks_queue = None
_running = False
_stop_tasks_queue = False


def start():
    global _running, _tasks_queue
    _running = True
    _tasks_queue = queue.Queue(maxsize=100)
    Thread(target=do_tasks, daemon=True).start()


def stop():
    global _running, _tasks_queue
    _running = False

    clear_task_queue()


def do_tasks():
    while _running == True:
        try:
            task = _tasks_queue.get()
            print(f'Начали задачу {task=}')
            task[0](task[1])
            print(f'Выполнили задачу {task=}')
            _tasks_queue.task_done()
        finally:
            sleep(0.05)


def add_task(task, preparation_mode):
    try:
        _tasks_queue.put((task, preparation_mode))
        print(f'Задача {task=} поставлена в очередь')
    except queue.Full:
        return


def clear_task_queue():
    while not _tasks_queue.empty():
        try:
            _tasks_queue.get(block=False)
            _tasks_queue.task_done()
        except queue.Empty:
            continue
    print(f'Очередь задач очищена')


def use_quas(preparation_mode):
    spheres.prepare('quas')


def use_wex(preparation_mode):
    spheres.prepare('wex')


def use_exort(preparation_mode):
    spheres.prepare('exort')


def use_cold_snap(preparation_mode):
    spells.use('cold_snap', preparation_mode)


def use_ghost_walk(preparation_mode):
    spells.use('ghost_walk', preparation_mode)


def use_ice_wall(preparation_mode):
    spells.use('ice_wall', preparation_mode)


def use_emp(preparation_mode):
    spells.use('emp', preparation_mode)


def use_tornado(preparation_mode):
    spells.use('tornado', preparation_mode)


def use_alacrity(preparation_mode):
    spells.use('alacrity', preparation_mode)


def use_deafening_blast(preparation_mode):
    spells.use('deafening_blast', preparation_mode)


def use_sun_strike(preparation_mode):
    spells.use('sun_strike', preparation_mode)


def use_forge_spirit(preparation_mode):
    spells.use('forge_spirit', preparation_mode)


def use_chaos_meteor(preparation_mode):
    spells.use('chaos_meteor', preparation_mode)


def use_multicast_1(preparation_mode):
    pixel_colors = screen_scan.get_pixel_colors()[18:20]

    if (pixel_colors[0] == (78, 88, 101) or pixel_colors[1] == (78, 88, 101)):
        spells.use('ice_wall', preparation_mode)
    else:
        spells.use('ghost_walk', preparation_mode)
    spheres.prepare('quas')


def use_multicast_2(preparation_mode):
    if (preparation_mode):
        spells.prepare_multicast('tornado', 'sun_strike', 'chaos_meteor')
    else:
        spells.prepare_multicast('tornado', 'sun_strike')
        spells.use('tornado')
        sleep(1.4)
        spells.use('sun_strike')
        spells.use('chaos_meteor')
        sleep(1)
        spells.use('deafening_blast')
        spells.use('cold_snap')
        spells.use_item(3)
        spells.use_item(5)
        spells.prepare_multicast('tornado', 'sun_strike', 'chaos_meteor')


def use_multicast_3(preparation_mode):
    if (preparation_mode):
        spells.prepare_multicast('cold_snap', 'chaos_meteor', 'deafening_blast')
    else:
        spells.prepare_multicast('cold_snap', 'chaos_meteor')
        spells.use('cold_snap')
        spells.use('chaos_meteor')
        spells.use('deafening_blast')
        spells.use_item(3)
        spells.use_item(5)
        spells.prepare_multicast('cold_snap', 'chaos_meteor', 'deafening_blast')


def use_multicast_4(preparation_mode):
    if (preparation_mode):
        spells.prepare_multicast('sun_strike', 'chaos_meteor', 'deafening_blast')
    else:
        spells.prepare_multicast('sun_strike', 'chaos_meteor')
        spells.use_item(3)
        spells.use('sun_strike')
        spells.use('chaos_meteor')
        spells.use('deafening_blast')
        spells.use('cold_snap')
        spells.use_item(5)
        spells.prepare_multicast('sun_strike', 'chaos_meteor', 'deafening_blast')
