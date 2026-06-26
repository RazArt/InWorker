from time import sleep

import InWorker.screen_scan as screen_scan
import InWorker.hotkeys as hotkeys
import InWorker.config as config
import InWorker.spheres as spheres

_selected = {0: '', 1: ''}
_invoke_cooldown = False


def _update():
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
    pixel_colors = screen_scan.get_pixel_colors()[15:17]

    for index in range(2):
        for spellname, colors_array in spells_colors.items():
            if (colors_array[0] == pixel_colors[index] or colors_array[1] == pixel_colors[index]):
                _selected[index] = spellname


def init():
    global _selected, _invoke_cooldown
    _selected = {0: '', 1: ''}
    _invoke_cooldown = False

    _update()


def is_preparation():
    return hotkeys.get_key_state(config.key_binds['preparation_cast_mode'])


def use_invoke():
    if (screen_scan.get_pixel_colors()[17] != (240, 160, 37)):
        return False

    hotkeys.key_send(config.key_binds['invoke'])
    return True


def prepare(spellname):
    if (spheres.prepare(spellname) == False or use_invoke() == False):
        return False

    return True


def prepare_multicast(spellname_1, spellname_2, spellname_3=''):
    _update()

    if ((_selected[0] == spellname_1 and _selected[1] == spellname_2) or
        (_selected[1] == spellname_1 and _selected[0] == spellname_2)):
        pass
    elif (_selected[1] == spellname_1):
        prepare(spellname_1)
        prepare(spellname_2)
    elif (_selected[1] == spellname_2):
        prepare(spellname_2)
        prepare(spellname_1)
    elif (_selected[0] == spellname_1):
        prepare(spellname_2)
    elif (_selected[0] == spellname_2):
        prepare(spellname_1)
    else:
        prepare(spellname_1)
        prepare(spellname_2)

    if (spellname_3):
        spheres.prepare(spellname_3)


def use(spellname, preparation_mode=False):
    _update()

    if (preparation_mode):
        if ((_selected[0] == spellname)):
            return True
        else:
            return prepare(spellname)
    else:
        if (_selected[0] == spellname):
            hotkeys.key_press(56)
            hotkeys.key_send(config.key_binds['spell_1'])
            hotkeys.key_release(56)
            hotkeys.key_send(config.key_binds['spell_1'])
            return True
        elif (_selected[1] == spellname):
            hotkeys.key_press(56)
            hotkeys.key_send(config.key_binds['spell_2'])
            hotkeys.key_release(56)
            hotkeys.key_send(config.key_binds['spell_2'])
            return True
        elif (spheres.get_prepared_spellname() == spellname):
            if (use_invoke() == True):
                hotkeys.key_press(56)
                hotkeys.key_send(config.key_binds['spell_1'])
                hotkeys.key_release(56)
                hotkeys.key_send(config.key_binds['spell_1'])
                return True
            return False
        elif (prepare(spellname)):
            hotkeys.key_press(56)
            hotkeys.key_send(config.key_binds['spell_1'])
            hotkeys.key_release(56)
            hotkeys.key_send(config.key_binds['spell_1'])
            return True

    return False


def use_item(item_num):
    hotkeys.key_send(config.key_binds['item_' + str(item_num)])
    return True
