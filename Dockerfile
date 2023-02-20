FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-opencv
RUN apt-get update --fix-missing && apt-get install -y gcc tesseract-ocr wget libmagic-dev ffmpeg libsm6 libxext6 && rm -rf /var/cache/apt
RUN rm /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata
RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata --directory-prefix=/usr/share/tesseract-ocr/4.00/tessdata
RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/ita.traineddata --directory-prefix=/usr/share/tesseract-ocr/4.00/tessdata
RUN apt install ghostscript python3-tk -y
EXPOSE 8080
ADD ./requirements.txt /
RUN pip install -r /requirements.txt
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
# CMD uvicorn services:app --port 8080 --host  0.0.0.0
CMD python services.py
