import configparser
import sys

from telethon.sync import TelegramClient
from telethon import connection

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

#proxy = (proxy_server, proxy_port, proxy_key)

client = TelegramClient(username, api_id, api_hash)

client.start()

async def main():
	url = sys.argv[1]
	text = sys.argv[2]
	channel = await client.get_entity(url)
	#print(date_of_post)
	await client.send_message(channel, text)

with client:
	client.loop.run_until_complete(main())
