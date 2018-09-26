FROM rbekker87/alpine-python:3.6

ADD . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD ["/bin/sh", "/app/boot.sh"]
