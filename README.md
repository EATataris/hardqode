# Тестовое задание от HardQode

## Как запустить сервис

#### Создайте пустой каталог с именем, например "hardqode_server"
#### Перейдите в данный каталог в терминале или в командной строке
#### python -m venv vevn - создайте виртуальное окружение
#### .\venv\Scripts\activate - активируйте вирутльное окружение(или source source env/bin/activate)
#### git clone https://github.com/EATataris/hardqode
#### cd .\hardqode\
#### python -m pip install -r requirements.txt (или python3 -m pip install -r requirements.txt
#### python manage.py makemigrations  - создаем миграции
#### python manage.py migrate  - применяем миграции
#### python manage.py createsuperuser - создаем админа, чтоб потом чрез адми-панель было удобно наполнять нашу БД
#### python manage.py runserver - запускаем наш сервер