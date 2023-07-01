# nodear

## Telegram

### Подготовка к работе
Понадобился фикс для повторного запуска скрипта open_tele.py
https://github.com/thedemons/opentele/pull/74/files

Сперва надо открыть telegram сессию в десктопном приложении.
Затем, запускаем ```python3 open_tele.py```
Этот скрипт из каталога %USERPROFILE%\AppData\Roaming\Telegram Desktop\tdata сделает файл telethon.session
Файл можно использовать продолжительное время, т.е. его не требуется формировать кажный раз.

Создаём файл config.ini с содержимым из https://my.telegram.org/apps 

```
[Telegram]
api_id = 12345678
api_hash = 999e888777ab66bf555cb44aa33a220f
```

to install or upgrade the library to the latest version:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade telethon
pip3 install python-dateutil
pip3 install pytz
```
Из-за вот этого кейса, пришлось делать downgrade telethon до версии 1.27
https://github.com/lonamiwebs/telethon/issues/4092?ysclid=lic6ma6j9e43921132

В итоге надо апгейдить Python до 3.9
Для этого сначала надо установить  sudo yum install libsqlite3-dev
и с ./configure --enable-loadable-sqlite-extensions собрать Пайтон.

### Чтение сообщений
Запускаем срипт ```python3 tele_reader.py https://t.me/SolovievLive 2023-05-30T15:45:13+00:00 telethon SolovievLive.json```

где параметры:

1) url канала;
2) дата, после которой, считывать сообщения;
3) название файла сессии (telethon.session);
4) Имя файла в который сохранится результат.

В результате получаем массив JSON сообщений (только текст) начиная с обозначенной даты и времени.

### Отправка сообщения из файла
Формируем html или md файл с текстом сообщения с названием, например, test.html.
Запускаем срипт ```cat test.html|python3 tele_sender.py https://t.me/edotechestv_chat html theleton```
где параметры:
1) название канала
2) тип файла сообщения html или md
3) название файла сессии (telethon.session)

### Отправка html файла
Запускаем срипт ```python3 tele_file_sender.py https://t.me/edotechestv_chat```
В результате из папки "files" будет считан рандомный html файл и его содержимое отправится в качестве сообщения

## VK
### Подготовка к работе
```pip3 install vk_api
pip3 install urllib3==1.26.6
``` 

Конфигурация VK и токен описаны, например, тут: https://badtry.net/vk-api-osnovy-poluchieniie-tokiena/#vkcom

Добавляем в  файл config.ini
```
[VK]
access_token = vk1.a.3M..........-W5w
owner_id = 1234567
```

Тестовый вызов из Windows:
```type test.txt|python vk_post.py https://t.me/nod_news ```
где test.txt файл с содержимым поста.
