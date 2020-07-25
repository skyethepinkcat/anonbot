FROM python:3
RUN pip3 install discord
ADD . /tripled
WORKDIR /tripled
CMD [ "python3", "./run.py"]
