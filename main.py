import vk_api, vk
from vk_api.utils import get_random_id
import datetime, random, json

vk_session = vk_api.VkApi(token='f29dd2332c43bcc37bf87b807df1496d06627b1103654209109a1c541fbac967a255be4152baf8a928e94')
random.seed()
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

longpoll = VkBotLongPoll(vk_session, 203658568)
vk = vk_session.get_api()

def saymessage(message, chatid):
    vk.messages.send(
        key='265b9078df036d8b0bc08fa119f73547cb9e6fd9',
        server='https://lp.vk.com/wh203658568',
        ts='1',
        random_id=get_random_id(),
        message=message,
        chat_id=chatid
    )

def answer_message(chat_id, id_message, peer_id, text):
  query_json = json.dumps({"peer_id": peer_id,"conversation_message_ids":[id_message],"is_reply":True})
  vk_session.method('messages.send', {
    'chat_id': chat_id,
    'forward': [query_json],
    'message': text,
    'random_id': get_random_id()})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Моракс' in str(event) or 'моракс' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key='265b9078df036d8b0bc08fa119f73547cb9e6fd9',
                    server='https://lp.vk.com/wh203658568',
                    ts='1',
                    random_id=get_random_id(),
                    message="Моракс умер",
                    attachment='photo-175821022_457239620',
                    chat_id=event.chat_id
                )
        elif 'Привет!' in str(event) or 'привет!' in str(event):
            if event.from_chat:
                if random.randint(0, 19) == 0:
                    saymessage('Я родился!\nПоздравляю, сегодня тебе повезёт в гаче(нет)\n\nС уважением, Чжун Ли.', event.chat_id)
                else:
                    saymessage('Привет!\n\nС уважением, Чжун Ли.', event.chat_id)
        elif 'Пока!' in str(event) or 'пока!' in str(event):
            if event.from_chat:
                saymessage('Пока!\n\nС уважением, Чжун Ли.', event.chat_id)
        elif 'Как дела?' in str(event) or 'как дела?' in str(event):
            if event.from_chat:
                if (random.randint(0, 1) == 0):
                    saymessage('Дай мору\n\nС уважением, Чжун Ли.', event.chat_id)
                else:
                    vk.messages.send(
                        key='265b9078df036d8b0bc08fa119f73547cb9e6fd9',
                        server='https://lp.vk.com/wh203658568',
                        ts='1',
                        random_id=get_random_id(),
                        message='Сегодня выдался продуктивный день\n\nС уважением, Чжун Ли.',
                        attachment='photo-175821022_457239616',
                        chat_id=event.chat_id
                    )
        elif 'Чжун сегодня' in str(event) or 'чжун сегодня' in str(event):
            if event.from_chat:
                nowtime = (datetime.datetime.utcnow() + datetime.timedelta(hours=-2)).isoweekday()

                if nowtime == 1:
                    message = "Понедельник"
                    pic = "photo-175821022_457239608"
                elif nowtime == 2:
                    message = "Вторник"
                    pic = "photo-175821022_457239609"
                elif nowtime == 3:
                    message = "Среда"
                    pic = "photo-175821022_457239610"
                elif nowtime == 4:
                    message = "Четверг"
                    pic = "photo-175821022_457239611"
                elif nowtime == 5:
                    message = "Пятница"
                    pic = "photo-175821022_457239612"
                elif nowtime == 6:
                    message = "Суббота"
                    pic = "photo-175821022_457239613"
                else:
                    message = "Воскресенье"
                    pic = "photo480012858_457278730"

                vk.messages.send(
                    key='265b9078df036d8b0bc08fa119f73547cb9e6fd9',
                    server='https://lp.vk.com/wh203658568',
                    ts='1',
                    random_id=get_random_id(),
                    message="⠀⠀⠀⠀⠀⠀「" + message + "」\n⠀Дорогой путешественник, сегодня доступно:",
                    attachment=pic,
                    chat_id=event.chat_id
                )

        elif '.gettime' in str(event):
            if event.from_chat:

                vk.messages.send(
                    key='265b9078df036d8b0bc08fa119f73547cb9e6fd9',
                    server='https://lp.vk.com/wh203658568',
                    ts='1',
                    random_id=get_random_id(),
                    message=datetime.datetime.utcnow(),
                    chat_id=event.chat_id
                )
        elif 'Чжун Ли инфа' in str(event) or 'чжун ли инфа' in str(event) or 'Чжун инфа' in str(event) or 'чжун инфа' in str(event):
            if event.from_chat:
                if event.obj.from_id == 191548563:
                    saymessage('Вероятность примерно 100%\n\nС уважением, Чжун Ли.', event.chat_id)
                else:
                    saymessage('Вероятность примерно ' + str(random.randint(0, 100)) + '%\n\nС уважением, Чжун Ли.', event.chat_id)
        elif 'Чжун помощь' in str(event) or 'чжун помощь' in str(event):
            if event.from_chat:
                saymessage('Список команд:\n「Общение」\n⠀• Привет!\n⠀• Как дела?\n⠀• Пока!\n⠀• Бот\n「Информация」\n⠀• Чжун сегодня\n⠀• Чжун инфа\n\nС уважением, Чжун Ли.', event.chat_id)
        elif 'Помогите!' in str(event):
            if event.from_chat:
                saymessage('Тебе уже ничего не поможет.\n\nС уважением, Чжун Ли.', 1)
