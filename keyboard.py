from telebot import types


def player_moves():
    player_moves_kb = types.ReplyKeyboardMarkup(row_width=4)
    player_moves_kb_button_up = types.KeyboardButton('↑')
    player_moves_kb_button_down = types.KeyboardButton('↓')
    player_moves_kb_button_right = types.KeyboardButton('→')
    player_moves_kb_button_left = types.KeyboardButton('←')
    player_moves_kb.add(
        player_moves_kb_button_up, player_moves_kb_button_down,
        player_moves_kb_button_right, player_moves_kb_button_left
                        )
    return player_moves_kb