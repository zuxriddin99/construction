import telegram
from mainapp.models import Korxona

BOT_TOKEN = '1652636238:AAEaM3xVl2WdZnb7oWMT9YmEg618MiZf4JU'
BOT_URL = 'https://api.telegram.org/bot%s' % BOT_TOKEN
BOT_CHAT_ID = '630613565'

telegram_id = str(Korxona.objects.get(id=1).telegram)


def send_message_via_bot(request, msg):
    bot = telegram.Bot(token=BOT_TOKEN)
    try:
        bot.sendMessage(telegram_id, text=msg, parse_mode='html')
    except:
        pass

