FROM python:3

RUN git clone https://github.com/manolo2829/examen-phrase-1.git

WORKDIR /examen-phrase-1

CMD ["python3", "-m", "unittest"]