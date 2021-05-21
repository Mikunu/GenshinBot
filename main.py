import vk_api, vk
from vk_api.utils import get_random_id
import datetime, random, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

byezhong = "\n\nС уважением, Чжун Ли."

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
    f = open(f"txts/jokes/joke{num}.txt", "r")
    message = "Дорогой друг, сейчас я расскажу тебе, что я сегодня прочитал в интересной книге\n\n"
    lines = f.readlines()
    for line in lines:
        message += line
    message += byezhong
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
                    say_message(f'Я родился!\nПоздравляю, сегодня тебе повезёт в гаче(нет){byezhong}')
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

                    with open("txts/greeting.txt", 'r') as greetingf:
                        for i in range(greetnum):
                            greetmessage =greetingf.readline()
                    greetingf.close()
                    say_message(f'{greetmessage}{byezhong}')

        elif 'Пока!' in str(event) or 'пока!' in str(event):
            if event.from_chat:
                randnum = random.randint(0, 19)

                if randnum == 0:
                    goodbyenum = 0
                elif 1 < randnum < 6:
                    goodbyenum = 1
                elif 6 < randnum < 10:
                    goodbyenum = 2
                elif 10 < randnum <= 15:
                    goodbyenum = 3
                elif 15 < randnum <= 20:
                    goodbyenum = 4

                with open("txts/goodbyes.txt", 'r') as goodbyef:
                    for i in range(goodbyenum):
                        greetmessage = goodbyef.readline()
                goodbyef.close()
                say_message(f'{greetmessage}{byezhong}')

        elif 'Как дела?' in str(event) or 'как дела?' in str(event):
            if event.from_chat:
                if (random.randint(0, 19) == 0):
                    say_message('Дай мору\n\nС уважением, Чжун Ли.')
                else:
                    say_message(f'Сегодня выдался продуктивный день{byezhong}',
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
                say_message(f'Вероятность примерно {str(random.randint(0, 100))}%{byezhong}')

        elif 'Чжун помощь' in str(event) or 'чжун помощь' in str(event):
            if event.from_chat:
                say_message(
                    'Список команд:\n「Общение」\n⠀• Привет!\n⠀• Как дела?\n⠀'
                    f'• Пока!\n⠀• Бот\n「Информация」\n⠀• Чжун сегодня\n⠀• Чжун инфа{byezhong}')

        elif 'Помогите!' in str(event):
            if event.from_chat:
                    say_message(f'Тебе уже ничего не поможет.{byezhong}')

        elif 'Чжун анекдот' in str(event) or 'чжун анекдот' in str(event):
            if event.from_chat:
                say_message(joke())

        elif 'Чжун альбомы' in str(event):
            if event.from_chat:
                f = open(f"txts/info/albums.txt", "r")
                albmessage = ""
                lines = f.readlines()
                for line in lines:
                    albmessage += line
                albmessage += byezhong
                f.close()
                say_message(albmessage)

        elif 'Чжун ссылки' in str(event):
            if event.from_chat:
                f = open(f"txts/info/urls.txt", "r")
                urlmessage = ""
                lines = f.readlines()
                for line in lines:
                    urlmessage += line
                urlmessage += byezhong
                f.close()
                say_message(urlmessage)