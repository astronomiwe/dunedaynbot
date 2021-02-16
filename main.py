import telebot
from config import TOKEN

from keyboa import keyboa_maker
from keyboards import main_menu, member_menu, events_menu, action_menu

# import psycopg2
from config import DB_LOGIN_DATA

bot = telebot.TeleBot(TOKEN)
last_id = None
last_username = None

# коннект с БД
# conn = psycopg2.connect(dbname=DB_LOGIN_DATA[0], user=DB_LOGIN_DATA[1], password=DB_LOGIN_DATA[2],
#                         host=DB_LOGIN_DATA[3])
# cursor = conn.cursor()
# conn.autocommit = True

# создаём клавиатуры
kb_main_menu = keyboa_maker(items=main_menu, copy_text_to_callback=True)
kb_member_menu = keyboa_maker(items=member_menu, copy_text_to_callback=True)
# kb_events_menu = keyboa_maker(items=events_menu, copy_text_to_callback=True)
kb_action_menu = keyboa_maker(items=action_menu, copy_text_to_callback=True)


# универсальная функция ответа на нажатие кнопки пользователем.
# text - ответное сообщение, next_menu - следующее вызываемое меню (None если никакое)


def reply(text='Здесь пока ничего нет', next_menu=None):
    global last_id
    bot.send_message(
        chat_id=last_id,
        text=str(last_id) + ' ' + text + str(last_username),
        reply_markup=next_menu)


@bot.message_handler(content_types=['text'])
def mainMenu(message):
    global last_id
    last_id = message.from_user.id
    global last_username
    last_username = message.from_user.username
    reply('Привет! Что тебя интересует?', kb_main_menu)


# TODO написать реакцию на callback
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # блок main menu
    if call.data == main_menu[0]:
        reply()
    elif call.data == main_menu[1]:
        reply()
    elif call.data == main_menu[2]:
        reply()
    elif call.data == main_menu[3][0]:
        reply()
    elif call.data == main_menu[3][1]:
        reply()
    elif call.data == main_menu[4]:
        reply('Меню игрока:', kb_member_menu)
    # блок меню игрока
    elif call.data == member_menu[0]:
        reply()
    elif call.data == member_menu[1][0]:
        reply()
    elif call.data == member_menu[1][1]:
        reply()
    elif call.data == member_menu[2]:
        reply('Что тебя интересует?', kb_main_menu)

    # TODO блок вывода мероприятий для записи - генерировать клавиатуру
    # блок меню записи на конкретное меропр.

    # todo SQL запрос, форматированный вывод
    elif call.data == action_menu[0]:
        reply()
    elif call.data == action_menu[1]:
        reply()
    elif call.data == action_menu[2]:
        reply()


# RUN
bot.polling(none_stop=True, timeout=25)
