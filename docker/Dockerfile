FROM python:3.9-alpine3.14

RUN adduser -D mainuser

RUN apk add --update --no-cache postgresql-dev g++ gcc

WORKDIR /app

COPY ../requirements.txt /tmp/requirements.txt

RUN cd /tmp/ && pip install --no-cache-dir -r requirements.txt

COPY --chown=mainuser:mainuser docker /app

USER mainuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
