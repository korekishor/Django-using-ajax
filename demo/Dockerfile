FROM python:3.9
WORKDIR /app
COPY ./app/requirements.txt req.txt
RUN pip install -r req.txt
COPY . .
EXPOSE 9000
CMD python manage.py runserver 0.0.0.0:9000
