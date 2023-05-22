# nodear

Понадобился фикс для повторного запуса
https://github.com/thedemons/opentele/pull/74/files

Создаём файл с содержимым из https://my.telegram.org/apps где username не имеет значения

```
[Telegram]
api_id = 12345678
api_hash = 999e888777ab66bf555cb44aa33a220f
username = telethon
```
Сперва надо открыть telegram сессию в десктопном приложении. 
Запускаем ```python open_tele.py``` 
Этот скрипт из файла %USERPROFILE%\AppData\Roaming\Telegram Desktop\tdata сделает файл telethon.session

Запускаем ```python tele_reader.py```

Если всё хорошо, то появится запрос:

```Введите ссылку на канал или чат:```

