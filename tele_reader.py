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
username = config['Telegram']['username']

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
		all_messages.append(msg.text)
	
	with open(filename, 'w', encoding='utf8') as outfile:
		json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)

async def main():
	#date_of_post = tz.localize(datetime.strptime(sys.argv[2], '%Y-%m-%d')) #datetime(2023, 5, 25, 0, 0, 0, tzinfo=utc) #parse('2023-05-28 00:00:00') #datetime.datetime(2023, 5, 28)
	tz = pytz.timezone('Europe/Moscow')
	date_of_post = parse(sys.argv[2]).replace(tzinfo=pytz.timezone('Europe/Moscow'))
	url = sys.argv[1]
	filename = sys.argv[3]
	channel = await client.get_entity(url)
	#await dump_all_participants(channel)
	await get_messages_at_date(channel, date_of_post, filename)

with client:
	client.loop.run_until_complete(main())
