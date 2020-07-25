FROM python:3
RUN pip3 install discord
ADD . /bot
WORKDIR /bot
CMD [ "python3", "./run.py"]
