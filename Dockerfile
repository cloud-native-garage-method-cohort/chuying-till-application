FROM quay.io/bitnami/python
WORKDIR /app
COPY main.py main.py
RUN python main.py