FROM python:3

ADD . /

CMD [ "python", "data-classes.py" ]