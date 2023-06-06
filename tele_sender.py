import configparser
import sys
import io

from telethon.sync import TelegramClient
from telethon import connection

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

sys.stdin.reconfigure(encoding='utf-8')

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")
username = sys.argv[3]

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username

#proxy = (proxy_server, proxy_port, proxy_key)

client = TelegramClient(username, api_id, api_hash, system_version="4.16.30-vxNODEAR")

client.start()

async def main():
	url = sys.argv[1]
	parse_mode = sys.argv[2]

	text = ""
	for line in sys.stdin:
		text += line

	channel = await client.get_entity(url)
	#print(date_of_post)
	client.parse_mode = parse_mode
	await client.send_message(channel, text)

with client:
	client.loop.run_until_complete(main())
