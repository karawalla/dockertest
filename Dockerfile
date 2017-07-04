FROM python:latest
RUN pip install redis
ADD src/ /src/
WORKDIR /src/

ENTRYPOINT python3 -m unittest

