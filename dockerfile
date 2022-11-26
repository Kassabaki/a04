FROM python:3.8-slim-buster
WORKDIR /python-docker
COPY main.py ./
CMD ["python3", "main.py"]
