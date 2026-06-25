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
    'preparation_cast_mode': 43,
    'actions_lock_1': 42,
    'actions_lock_2': 29
}

hotkeys = {
    16: (user_actions.press_q, True),
    17: (user_actions.press_w, True),
    18: (user_actions.press_e, True),
    19: (user_actions.press_r, True),
    20: (user_actions.press_t, True),
    50: (user_actions.press_m, True),
    2: (user_actions.press_1, True),
    3: (user_actions.press_2, True),
    4: (user_actions.press_3, True),
    5: (user_actions.press_4, True)
}
