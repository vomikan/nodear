import requests
import configparser
import io
import sys

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
bot_token = config['Telegram']['bot_token']
bot_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

bot_name = "бот"
#bot = telebot.TeleBot(bot_token)

#Входящий поток в переменную
sys.stdin.reconfigure(encoding='utf-8')
message = ""
for line in sys.stdin:
    message += line

chat_id = sys.argv[1]

def post():
    try:
        #response = requests.post(bot_api_url, json={'chat_id': chat_id, 'text': message, 'disable_content_type_detection': None})
        response = requests.post(bot_api_url, json={'chat_id': chat_id, 'text': message, 'parse_mode': 'html'})
        print(response.text)
    except Exception as e:
        print(e)

if __name__=="__main__":
    post()
