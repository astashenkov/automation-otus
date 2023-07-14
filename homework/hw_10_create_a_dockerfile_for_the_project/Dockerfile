FROM python:3.10-alpine

WORKDIR tests

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY conftest.py .
COPY test_py_server.py .

ENTRYPOINT ["pytest"]