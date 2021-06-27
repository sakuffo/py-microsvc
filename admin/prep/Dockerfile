FROM python:3.9.5

ENV PYTHONUBNUFFERED 1

WORKDIR /prep

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ../. /prep

CMD python manage.py makemigrations

CMD python manage.py migrate