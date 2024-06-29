FROM python:3.11.3-alpine

WORKDIR /app/

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . /app/

CMD [ "flask", "--app", "source/webapp/app.py", "run", "--host", "0.0.0.0"]
