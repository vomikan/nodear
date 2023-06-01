import configparser
import sys
import os, random
import webbrowser
import codecs

from os import listdir
from os.path import isfile, join

from telethon.sync import TelegramClient
from telethon import connection

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Директория c html файлами для отправки
basedir = "files"

#Читаем случайный файл
filename = join(basedir, random.choice([x for x in os.listdir(basedir)
	if os.path.isfile(os.path.join(basedir, x))]))
#print("Playing file {}...".format(filename))

#Содержимое файла в переменную
try:
	filehandle = codecs.open(filename, "r", "utf-8") #open(filename, "r")
except:
	print("Could not open file " + filename)
	quit() 

text = filehandle.read()
filehandle.close()
#print (text)

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
	channel = await client.get_entity(url)
	#print(date_of_post)
	client.parse_mode = "html"
	await client.send_message(channel, text)

with client:
	client.loop.run_until_complete(main())
