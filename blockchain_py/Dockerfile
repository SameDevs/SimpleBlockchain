FROM python:alpine3.6

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./src /code
WORKDIR /code

# Define exposed variables
ARG PORT=5000
ENV PORT $PORT

ENV DEBUG $DEBUG

EXPOSE ${PORT}

CMD ["python", "main.py"]
