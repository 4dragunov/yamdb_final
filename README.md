#
![Build Status](https://github.com/4dragunov/yamdb_final/workflows/yambd-workflow/badge.svg)

# Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Приложение написано на основе `fullREST` архитектуры на фреймворке `django-rest-framework`. База данных `postgresssql`.
<br><br>Проект доступен по адресу: http://84.252.128.33 <br>
Документация: http://84.252.128.33/redoc/

В корне проекта файл `entrypoint.sh
` собирает статику и выполняет миграции. 

## Установка на локальном компьютере
Приведенная ниже последовательность позволит развернуть проект на локальной машине для тестирования
### Установка Docker
Для запуска проекта необходима установка программ `docker` и `docker-compose`. https://docs.docker.com/engine/install/
### Запуск проекта (Lunux)  
1. Создайте на локальном ПК папку проекта yamdb_final командой `mkdir
 yamdb_final`
 
2. Склонируйте репозиторий в текущую папку командой 
`git clone https://github.com/4dragunov/yamdb_final/ .` и перейдите в нее командой `cd yamdb_final`

3. Создайте файл `.env` командой `touch .env
` с переменными окружениями для работы с базой данных на основе шаблона
 для работы с базой данных:
 ```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
    
4.Запустите `docker-compose` командой sudo `docker-compose up -d`

Следующие шаги выполняет скрипт `entrypoint.sh
`, в случае ручного выполнения необходимо выполнить следующие команды

- Создайте миграции `sudo docker-compose exec web python manage.py migrate`

- Соберите статику проекта командой `sudo docker-compose exec web python
 manage.py collectstatic --no-input`

5.Создайте суперпользователя Django `sudo docker-compose exec web python
 manage.py createsuperuser`

6.Загрузите фикстуры (тестовые данные) в базу данных командой `sudo docker
-compose exec web python manage.py loaddata fixtures.json`

7.Запуск тестов (при желании)<br>
В терминале или командной строке перейдите в директорию проекта (она содержит этот readme файл) командой `cd [путь]` <br>
Установите пакет pytest командой `pip install -U pytest` подробнее https://docs.pytest.org/en/stable/getting-started.html
<br>Запустите тесторование командой `pytest`


После описанных выше действий проект будет доступен по адресу `http://127.0.0.1`
<br>Документация для работы с API будет доступна по адресу `http://127.0.0.1/redoc`
## Установка (деплой) на удаленном сервере
## Деплой с использованием git actions
Необходимо создать переменные окружения в вашем репозитории github
 в разделе `secrets`
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь сервера
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта (для оправки уведомления об успешном деплое)
TELEGRAM_TOKEN # Токен бота (для оправки уведомления об успешном деплое)
```
При каждом деплое будет происходить:
- проверка кода соответствие страндарту `pep8`
- выполнение тестов `pytest`
- сборка и обновление образа на сервисе `docker-hub`
- автоматический деплой на сервер, указанный в `secrets`
- отправка уведомления в телеграм
При необходимости изменения или добавления действий редактируйте файл `.github/workflows/main.yml`. <br>
Файл `yamdb_workflow.yaml
` является копией и создан для проведения тестов `pytest`

### Использованные технологии
Django Rest Framework https://www.django-rest-framework.org/ <br>
Django https://www.djangoproject.com/ <br>
PostgreSQL https://www.postgresql.org/ <br>
Docker https://www.docker.com/ <br>

### Авторы проекта
Алексей Драгунов - Python Developer <br>
Евгения Самсонова - Python Developer <br>
Алексей Сухачевский - Python Developer

### Лицензии
Этот проект, включая все файлы и их содержимое, лицензирован в соответствии с условиями лицензии MIT.
Смотрите LICENSE.txt для деталей.


