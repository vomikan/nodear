import vk_api
import configparser
import io
import sys

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
id = config['VK']['owner_id'] # id пользователя / сообщества
access_token = config['VK']['access_token'] 

session=vk_api.VkApi(token=access_token)
vk=session.get_api()

sys.stdin.reconfigure(encoding='utf-8')
text = ""
for line in sys.stdin:
    text += line

url = sys.argv[1]

def post():
    vk.wall.post(
        owner_id = id,  # id пользователя / сообщества
        message = text,
        attachments = url,
        copyright = 'https://t.me/MinisterstvoDizaina'
    )

if __name__=="__main__":
    post()
