# lessons-runner
Приложение для автоматического посещения лекций

### Требования
  Требуются Python2.7 и pip:

  [Установить Python 2.7.9](https://www.python.org/downloads/release/python-279/) (pip идет в комплекте)

  ***Если Вы установите версию Python 2.7, но младше версии 2.7.9, то pip придется устанавливать отдельно***

  Устанавливаем selenium и click (обработка CLI):

  ```
  pip install selenium
  pip install click
  ```

  Если отсутствует дисплей, потребуется установить **виртуальный дисплей**:
  ``` pip install pyvirtualdisplay ```

### Использование
  Формат использования:
  _python main.py [options]_

#### Docker
  Возможно использование приложения в Docker контейнере.
  1. Используя docker-compose

     [Установить docker-compose](https://dker.ru/docs/docker-compose/install-compose/)
     ```
     docker-compose build # Сборка всех контейнеров
     docker-compose up browser # На порте 4444 будет открыт Selenium Server

     docker-compose run --rm app [options] # --rm необходим для удаления docker контейнера сразу после исполнения введенной команды
     ```
  2. Без использования docker-compose
     ```
     docker run -d -p 4444:4444 selenium/standalone-chrome
     docker build -t lessons-runner . # Build a container

     docker run --rm lessons-runner [options]
     ```

  ### Описание опций
   ```
     -t, --type СТРОКА          Тип конференции [webinar, freeconferencecall]
                                 [обязательно]

     -n, --name СТРОКА          Имя человека, заходящего в конференцию
                                 [обязательно]

     -u, --url СТРОКА           URL конференции  [обязательно]
     --wait-time ЧИСЛО        Время подключения к конференции в секундах
                                 (по умолчанию 60 сек)

     --presence-time ЧИСЛО    Время присутствия на лекции
                                 (по умолчанию 1 ч 35 мин)

     -k, --key СТРОКА           Указать пароль для доступа к комнате webinar.bmstu.ru
     --executor СТРОКА          Указать URL адрес сервера Selenium (локальный адрес: http://localhost:4444/wd/hub, на Mac при использовании docker-compose: http://docker.for.mac.localhost:4444/wd/hub)

     -vd, --virtual-display   Подключить виртуальный дисплей (потребуется пакет pyvirtualdisplay)
     --no-headless            Будет использован графический интерфейс (откроется настоящий браузер), если флаг активен
     --no-sandbox             Использовать это для запуска из-под пользователя root (например, при использовании Docker контейнера)

     --help                   Отобразить справку.
  ```
