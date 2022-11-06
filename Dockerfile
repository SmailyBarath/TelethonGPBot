FROM python:3.10.0

WORKDIR /root/GPBot

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip install -U -r requirements.txt

CMD ["python3","-m","GPBot"]
