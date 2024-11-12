FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask requests

EXPOSE 80

CMD ["python", "Linaapp.py"]
