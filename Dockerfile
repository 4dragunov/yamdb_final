# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM python:3.8.5

WORKDIR /code

COPY . .

RUN pip install -r ./requirements.txt

#CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

#CMD python manage.py makemigrations && python manage.py makemigrations api
#&& python manage.py migrate
#&& gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

