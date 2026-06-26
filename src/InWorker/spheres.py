import InWorker.screen_scan as screen_scan
import InWorker.hotkeys as hotkeys
import InWorker.config as config

_selected = {'names': {0: '', 1: '', 2: ''}, 'count': {'quas': 0, 'wex': 0, 'exort': 0}}
_availability = {'quas': False, 'wex': False, 'exort': False}
_preparation = False
_structures = {
    'cold_snap': {
        'quas': 3,
        'wex': 0,
        'exort': 0
    },
    'ghost_walk': {
        'quas': 2,
        'wex': 1,
        'exort': 0
    },
    'ice_wall': {
        'quas': 2,
        'wex': 0,
        'exort': 1
    },
    'emp': {
        'quas': 0,
        'wex': 3,
        'exort': 0
    },
    'tornado': {
        'quas': 1,
        'wex': 2,
        'exort': 0
    },
    'alacrity': {
        'quas': 0,
        'wex': 2,
        'exort': 1
    },
    'deafening_blast': {
        'quas': 1,
        'wex': 1,
        'exort': 1
    },
    'sun_strike': {
        'quas': 0,
        'wex': 0,
        'exort': 3
    },
    'forge_spirit': {
        'quas': 1,
        'wex': 0,
        'exort': 2
    },
    'chaos_meteor': {
        'quas': 0,
        'wex': 1,
        'exort': 2
    }
}


def init():
    global _selected, _availability, _preparation
    _selected = {'names': {0: '', 1: '', 2: ''}, 'count': {'quas': 0, 'wex': 0, 'exort': 0}}
    _availability = {'quas': False, 'wex': False, 'exort': False}
    _preparation = False

    _update()


def is_use_availability():
    if (hotkeys.get_key_state(config.key_binds['actions_lock_1']) or
            hotkeys.get_key_state(config.key_binds['actions_lock_2'])):
        return False

    return True


def _update():
    global _selected, _availability
    position = 0
    pixel_colors = screen_scan.get_pixel_colors()[:15]
    print(f'{pixel_colors[:4]=}')
    for color in pixel_colors[:12]:
        if (color == (40, 122, 175)):
            _selected['names'][position] = 'quas'
            position += 1
        elif (color == (119, 56, 126)):
            _selected['names'][position] = 'wex'
            position += 1
        elif (color == (146, 87, 28)):
            _selected['names'][position] = 'exort'
            position += 1

    _selected['count'] = {'quas': 0, 'wex': 0, 'exort': 0}
    for _, name in _selected['names'].items():
        if (name != ''):
            _selected['count'][name] += 1

    if not (_availability['quas']):
        _availability['quas'] = True if (pixel_colors[12] == (34, 40, 39)) else False
    if not (_availability['wex']):
        _availability['wex'] = True if (pixel_colors[13] == (34, 40, 39)) else False
    if not (_availability['exort']):
        _availability['exort'] = True if (pixel_colors[14] == (34, 40, 39)) else False


def get_prepared_spellname():
    _update()
    print(f'{_selected=}')
    for spellname in _structures:
        if ((_selected['count']['quas'] == _structures[spellname]['quas']) and
            (_selected['count']['wex'] == _structures[spellname]['wex']) and
            (_selected['count']['exort'] == _structures[spellname]['exort'])):
            return spellname

    return None


def prepare(spellname):
    global _preparation
    spellname = "cold_snap" if (spellname == "quas") else spellname
    spellname = "emp" if (spellname == "wex") else spellname
    spellname = "sun_strike" if (spellname == "exort") else spellname
    print(get_prepared_spellname())
    if (get_prepared_spellname() == spellname):
        return True

    if (_preparation):
        return False

    for sphere_name in _structures[spellname]:
        if (_structures[spellname][sphere_name] > 0):
            if (_availability[sphere_name] == False):
                _preparation = False
                return False

    _preparation = True

    spheres = {}
    spheres['names'] = _selected['names'].copy()

    for index in range(3):
        del spheres['names'][index]
        spheres['counts'] = {'quas': 0, 'wex': 0, 'exort': 0}
        spheres['difference'] = {'quas': 0, 'wex': 0, 'exort': 0}

        for _, name in spheres['names'].items():
            if (name != ''):
                spheres['counts'][name] += 1

        for sphere_name in spheres['difference']:
            count = _structures[spellname][sphere_name] - spheres['counts'][sphere_name]
            spheres['difference'][sphere_name] = count if (count > 0) else 0

        if (index == (sum(spheres['difference'].values()) - 1)):
            for sphere_name, count in spheres['difference'].items():
                for _ in range(count):
                    hotkeys.key_send(config.key_binds[sphere_name])
            _preparation = False
            return True

    _preparation = False
    return True
