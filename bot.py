import telebot
from TOKEN import TOKEN
from app import initial_new_user, new_player
from app import app
from keyboard import player_moves
from datetime import datetime
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['join', 'start'])
def handle_join(message):
    try:
        with app.app_context():
            initial_new_user(name=message.from_user.first_name, game_last=0, score=0)
            bot.send_message(message.chat.id, f'Ты добавлен в список лидеров\n'
                             f'Cписок лидеров:\nhttp://127.0.0.1:5000/leader_board')
            new_player(name=message.from_user.first_name, position_x=0, position_y=0, joined_time=datetime.now(),
                       coins_collected=0)
            bot.send_message(message.chat.id, f'Ты добавлен в базу данных игроков')
        bot.send_message(message.chat.id, f'Для управления используй кнопки', reply_markup=player_moves())
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка\n'
                                          f'{e}')

@bot.message_handler(content_types=['text'])
def handle_moves(message):
    if message.text == '↑':
        pass
    elif message.text == '↓':
        pass
    elif message.text == '→':
        pass
    elif message.text == '←':
        pass
    else:
        bot.send_message(message.chat.id, f'Твой ход не засчитан\n'
                                          f'Используй кнопки')
bot.polling(none_stop=True)