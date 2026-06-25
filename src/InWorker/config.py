import InWorker.user_actions as user_actions

key_binds = {
    'quas': 16,
    'wex': 17,
    'exort': 18,
    'invoke': 19,
    'spell_1': 33,
    'spell_2': 32,
    'item_1': 34,
    'item_2': 35,
    'item_3': 36,
    'item_4': 47,
    'item_5': 48,
    'item_6': 49,
    'preparation_cast_mode': 57,
    'actions_lock_1': 42,
    'actions_lock_2': 29
}

hotkeys = {
    16: (user_actions.use_cold_snap, True),
    17: (user_actions.use_sun_strike, True),
    18: (user_actions.use_multicast_3, True),
    19: (user_actions.use_multicast_2, True),
    20: (user_actions.use_multicast_4, True),
    50: (user_actions.use_multicast_1, True),
    44: (user_actions.use_multicast_2, True),
    45: (user_actions.use_multicast_3, True),
    46: (user_actions.use_multicast_4, True),
    2: (user_actions.use_ice_wall, True),
    3: (user_actions.use_tornado, True),
    4: (user_actions.use_alacrity, True),
    5: (user_actions.use_forge_spirit, True)
}
