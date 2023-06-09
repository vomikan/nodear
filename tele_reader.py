import configparser
import json
import sys
from datetime import timedelta, date
from dateutil.parser import parse
from pytz import timezone, utc
import pytz

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

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
username = sys.argv[3]

#proxy = (proxy_server, proxy_port, proxy_key)

client = TelegramClient(username, api_id, api_hash)

client.start()

async def get_messages_at_date(channel, date, filename):
	class DateTimeEncoder(json.JSONEncoder):
		'''Класс для сериализации записи дат в JSON'''
		def default(self, o):
			if isinstance(o, datetime):
				return o.isoformat()
			if isinstance(o, bytes):
				return list(o)
			return json.JSONEncoder.default(self, o)
	all_messages = []
	async for msg in client.iter_messages(channel, reverse = True, offset_date=date):
		if msg.text:
			fwd_from = -1
			if hasattr(msg.fwd_from, 'from_id'):
				if (msg.fwd_from.from_id, 'channel_id'):
					fwd_from = msg.fwd_from.from_id.channel_id
			if hasattr(msg.from_id, 'user_id'):
				all_messages.append({'id':msg.id, 'user_id':msg.from_id.user_id, 'date':msg.date, 'text':msg.text, 'fwd_from':fwd_from})
			else:
				all_messages.append({'id':msg.id, 'date':msg.date, 'text':msg.text, 'fwd_from':fwd_from})

	with open(filename, 'w', encoding='utf8') as outfile:
		json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)

async def main():
	date_of_post = parse(sys.argv[2]) + timedelta(0,1) 
	url = sys.argv[1]
	filename = sys.argv[4]
	channel = await client.get_entity(url)
	#print(date_of_post)
	await get_messages_at_date(channel, date_of_post, filename)

with client:
	client.loop.run_until_complete(main())
