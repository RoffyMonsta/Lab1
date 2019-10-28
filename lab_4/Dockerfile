FROM python:3.7-slim

LABEL author="Anton"
LABEL version=1.0

# оновлюємо систему
RUN apt-get update && apt-get upgrade -y

# Встановлюємо потрібні пакети
RUN apt-get install git -y && pip install pipenv

# Створюємо робочу папку
WORKDIR /lab

# Завантажуємо файли з Git
RUN git clone https://github.com/RoffyMonsta/Lomovatskyi.git

# Створюємо остаточну робочу папку з Веб-сайтом та копіюємо туди файли
WORKDIR /app
<<<<<<< HEAD
RUN cp -r lab/Lomovatskyi/lab_3/* .
=======
RUN cp -r /lab/devops_course/lab3/* .
>>>>>>> ec177715f28f47518b303a599a84682650497824

# Інсталюємо всі залежності
RUN pipenv install

# Відкриваємо порт 8000 на зовні
EXPOSE 8000

# Це команда яка виконається при створенні контейнера
ENTRYPOINT ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
