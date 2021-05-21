import vk_api, vk
from vk_api.utils import get_random_id
import datetime, random, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def say_message(text, attachment=None):
    vk.messages.send(
        key=key,
        server=server,
        ts=ts,
        random_id=get_random_id(),
        message=text,
        attachment=attachment,
        chat_id=event.chat_id
    )

"""
def answer_message(chat_id, id_message, peer_id, text):
    query_json = json.dumps({"peer_id": peer_id, "conversation_message_ids": [id_message], "is_reply": True})
    vk_session.method('messages.send', {
        'chat_id': chat_id,
        'forward': [query_json],
        'message': text,
        'random_id': get_random_id()}
        ) 17
"""


def joke():
    num = random.randint(0, 19)
    f = open(f"jokes/joke{num}.txt", "r")
    message = "Дорогой друг, сейчас я расскажу тебе, что я сегодня прочитал в интересной книге\n\n"
    lines = f.readlines()
    for line in lines:
        message += line
    message += "\n\nС уважением, Чжун ли."
    f.close()
    return message

with open("loginstuff.json", "r") as read_file:
    data = json.load(read_file)

token = data[0]["token"]
longpoll = data[0]["longpoll"]
key = data[0]["key"]
server = data[0]["server"]
ts = data[0]["ts"]

vk_session = vk_api.VkApi(token=token)
random.seed()

longpoll = VkBotLongPoll(vk_session, longpoll)
vk = vk_session.get_api()

print("Бот успешно запущен")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        if 'Моракс' in str(event) or 'моракс' in str(event):
            if event.from_chat:
                say_message("Моракс умер", 'photo-175821022_457239620')

        elif 'Привет!' in str(event) or 'привет!' in str(event):
            if event.from_chat:
                if random.randint(0, 19) == 0:
                    say_message('Я родился!\nПоздравляю, сегодня тебе повезёт в гаче(нет)\n\nС уважением, Чжун Ли.')
                else:
                    greetnum = None
                    nowtime = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).hour
                    if 0 < nowtime < 4:
                        greetnum = 4  # Ночь
                    elif 4 < nowtime < 10:
                        greetnum = 1  # Утро
                    elif 10 < nowtime < 18:
                        greetnum = 2  # День
                    elif 18 < nowtime <= 23:
                        greetnum = 3  # Вечер

                    with open("greeting.txt", 'r') as greetingf:
                        for i in range(greetnum):
                            greetmessage =greetingf.readline()
                    greetingf.close()
                    say_message(f'{greetmessage}\n\nС уважением, Чжун Ли.')

        elif 'Пока!' in str(event) or 'пока!' in str(event):
            if event.from_chat:
                if random.randint(0, 19) == 0:
                    say_message('Вернись, мне мору надо!\n\nС уважением, Чжун Ли.')
                else:
                    say_message('До встречи!\n\nС уважением, Чжун Ли.')

        elif 'Как дела?' in str(event) or 'как дела?' in str(event):
            if event.from_chat:
                if (random.randint(0, 19) == 0):
                    say_message('Дай мору\n\nС уважением, Чжун Ли.')
                else:
                    say_message('Сегодня выдался продуктивный день\n\nС уважением, Чжун Ли.',
                                'photo-175821022_457239616')

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
                say_message("⠀⠀⠀⠀⠀⠀「" + message + "」\n⠀Дорогой путешественник, сегодня доступно:", pic)

        elif '.gettime' in str(event):
            if event.from_chat:
                say_message(datetime.datetime.utcnow())

        elif 'Чжун Ли инфа' in str(event) or 'чжун ли инфа' in str(event) or 'Чжун инфа' in str(
                event) or 'чжун инфа' in str(event):
            if event.from_chat:
                say_message(f'Вероятность примерно {str(random.randint(0, 100))}%\n\nС уважением, Чжун Ли.')

        elif 'Чжун помощь' in str(event) or 'чжун помощь' in str(event):
            if event.from_chat:
                say_message(
                    'Список команд:\n「Общение」\n⠀• Привет!\n⠀• Как дела?\n⠀'
                    '• Пока!\n⠀• Бот\n「Информация」\n⠀• Чжун сегодня\n⠀• Чжун инфа\n\nС уважением, Чжун Ли.')

        elif 'Помогите!' in str(event):
            if event.from_chat:
                    say_message('Тебе уже ничего не поможет.\n\nС уважением, Чжун Ли.')
        elif 'Чжун анекдот' in str(event) or 'чжун анекдот' in str(event):
            if event.from_chat:
                say_message(joke())