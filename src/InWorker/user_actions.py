from time import sleep

import InWorker.spheres as spheres
import InWorker.spells as spells
import InWorker.screen_scan as screen_scan


def use_quas():
    spheres.prepare('quas')


def use_wex():
    spheres.prepare('wex')


def use_exort():
    spheres.prepare('exort')


def use_cold_snap():
    spells.use('cold_snap')


def use_ghost_walk():
    spells.use('ghost_walk')


def use_ice_wall():
    spells.use('ice_wall')


def use_emp():
    spells.use('emp')


def use_tornado():
    spells.use('tornado')


def use_alacrity():
    spells.use('alacrity')


def use_deafening_blast():
    spells.use('deafening_blast')


def use_sun_strike():
    spells.use('sun_strike')


def use_forge_spirit():
    spells.use('forge_spirit')


def use_chaos_meteor():
    spells.use('chaos_meteor')


def use_multicast_1():
    pixel_colors = screen_scan.get_pixel_colors()[18:20]

    if (pixel_colors[0] == (78, 88, 101) or pixel_colors[1] == (78, 88, 101)):
        spells.use('ice_wall')
    else:
        spells.use('ghost_walk')
    spheres.prepare('quas')


def use_multicast_2():
    if (spells.is_preparation()):
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


def use_multicast_3():
    if (spells.is_preparation()):
        spells.prepare_multicast('cold_snap', 'chaos_meteor', 'deafening_blast')
    else:
        spells.prepare_multicast('cold_snap', 'chaos_meteor')
        spells.use('cold_snap')
        spells.use('chaos_meteor')
        spells.use('deafening_blast')
        spells.use_item(3)
        spells.use_item(5)
        spells.prepare_multicast('cold_snap', 'chaos_meteor', 'deafening_blast')


def use_multicast_4():
    if (spells.is_preparation()):
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
