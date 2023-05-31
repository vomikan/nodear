# nodear
### Подготовка к работе
Понадобился фикс для повторного запуска скрипта open_tele.py
https://github.com/thedemons/opentele/pull/74/files

Создаём файл config.ini с содержимым из https://my.telegram.org/apps где username не имеет значения

```
[Telegram]
api_id = 12345678
api_hash = 999e888777ab66bf555cb44aa33a220f
username = telethon
```
Сперва надо открыть telegram сессию в десктопном приложении.
Затем, запускаем ```python3 open_tele.py```
Этот скрипт из файла %USERPROFILE%\AppData\Roaming\Telegram Desktop\tdata сделает файл telethon.session
Файл можно использовать продолжительное время, т.е. его не требуется формировать кажный раз.

to install or upgrade the library to the latest version:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade telethon
pip3 install python-dateutil
pip3 install pytz
```

### Чтение сообщений
Запускаем срипт ```python3 tele_reader.py https://t.me/SolovievLive 2023-05-30T15:45:13+00:00 SolovievLive.json```

где параметры:

- url канала;
- дата, после которой, считывать сообщения;
- Имя файла в который сохранится результат.

В результате получаем массив JSON сообщений (только текст) начиная с обозначенной даты и времени.

### Отправка сообщений
Запускаем срипт ```python3 tele_sender.py https://t.me/edotechestv_chat "Родина, Свобода, Путин!"```

