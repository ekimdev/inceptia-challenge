FROM python:3.11.4-slim-bookworm

ARG PIP_ARGS="--no-cache-dir --disable-pip-version-check"

COPY requirements.txt /tmp

RUN pip install $PIP_ARGS -r /tmp/requirements.txt

WORKDIR /app

COPY geoapi.py ${WORKDIR} 

ENTRYPOINT ["python", "geoapi.py"]
