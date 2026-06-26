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
    'actions_exit': (42, 29)
}

user_hotkeys = {
    16: (user_actions.use_cold_snap, True),  # Q
    17: (user_actions.use_sun_strike, True),  # W
    18: (user_actions.use_multicast_3, True),  # E
    19: (user_actions.use_multicast_2, True),  # R
    20: (user_actions.use_multicast_4, True),  # T
    50: (user_actions.use_multicast_1, True),  # M
    44: (user_actions.use_quas, True),  # Z
    45: (user_actions.use_wex, True),  # X
    46: (user_actions.use_exort, True),  # C
    25: (user_actions.use_multicast_2, True),  # P
    26: (user_actions.use_multicast_3, True),  # {
    27: (user_actions.use_multicast_4, True),  # }
    2: (user_actions.use_ice_wall, True),  # 1
    3: (user_actions.use_tornado, True),  # 2
    4: (user_actions.use_alacrity, True),  # 3
    5: (user_actions.use_forge_spirit, True),  # 4
}
