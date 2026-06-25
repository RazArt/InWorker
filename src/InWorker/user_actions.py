from time import sleep

import InWorker.hotkeys as hotkeys
import InWorker.spheres as spheres
import InWorker.spells as spells
import InWorker.screen_scan as screen_scan

spells_colors = {
    'cold_snap': ((19, 36, 149), (80, 85, 107)),
    'ghost_walk': ((5, 13, 32), (60, 66, 71)),
    'ice_wall': ((168, 208, 236), (123, 136, 147)),
    'emp': ((43, 3, 48), (96, 82, 105)),
    'tornado': ((2, 44, 75), (68, 78, 88)),
    'alacrity': ((52, 24, 23), (63, 66, 71)),
    'deafening_blast': ((27, 69, 124), (75, 83, 99)),
    'sun_strike': ((242, 213, 109), (147, 140, 117)),
    'forge_spirit': ((35, 49, 64), (63, 69, 74)),
    'chaos_meteor': ((172, 92, 5), (86, 79, 79))
}


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
    print(f'{pixel_colors=}')
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
