
def teamJoin(message):
    bot.send_message(
        chat_id=message.from_user_id,
        text='Чтобы вступить к нам, необходимо (TODO)')  # TODO текст вступления в команду


def eventCalendar(message):
    bot.send_message(
        chat_id=message.from_user_id,
        text='С календарем мероприятий можно '
             'ознакомиться по ссылке: ..., ближайшее мероприятие')  # TODO ссылка на календарь, ближайшее меропр. из БД


def teamRules(message):
    bot.send_message(
        chat_id=message.from_user_id,
        text='Ознакомиться с нашими внутренними правилами можно '
             'по ссылке: ... '  # TODO ссылка на устав и подводящий текст
             'Мы писали правила сами, и придерживаемся их.')


def teamKitList(message):
    bot.send_message(
        chat_id=message.from_user_id,
        text='Посмотреть кит-лист можно по ссылке: ') # TODO ссылка на устав и подводящий текст
