FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN adduser -D user
USER user

#CMD ["python","app.py"]