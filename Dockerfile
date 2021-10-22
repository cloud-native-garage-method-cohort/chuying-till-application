FROM quay.io/bitnami/python
WORKDIR /app
COPY main.py main.py
CMD ["python3", "main.py"]