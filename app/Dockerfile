FROM python:3.11-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY baiter /app/baiter
COPY run.py /app/run.py

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]