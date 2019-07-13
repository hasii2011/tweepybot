FROM python:3.7-alpine

WORKDIR /
ENV PYTHONPATH "./"

COPY org/hasii/tweepybots/config.py          org/hasii/tweepybots/
COPY org/hasii/tweepybots/followfollowers.py org/hasii/tweepybots/
COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "org/hasii/tweepybots/followfollowers.py"]
