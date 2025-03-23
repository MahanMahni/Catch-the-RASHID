FROM python:3.13

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-alsa \
    libasound2 \
    pulseaudio

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "game.py"]
