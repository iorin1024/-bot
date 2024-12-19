FROM python:3.11
WORKDIR /discordbot
COPY requirements.txt /bdiscordbot/
RUN pip install -r requirements.txt
COPY . /discordbot
CMD python main.py