FROM python:3.10-slim
CMD echo "ciao ce"
RUN apt-get update && apt-get install -y python3-opencv
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
