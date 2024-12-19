FROM python:3.13.0
WORKDIR /discordbot
COPY requirements.txt /discordbot/
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . /discordbot
CMD python main.py
