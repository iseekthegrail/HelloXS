FROM python:3.8
#ADD HelloXS.py /

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "./HelloXS.py"]
