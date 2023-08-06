FROM python:3.10-alpine

WORKDIR /API_tests

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["pytest"]