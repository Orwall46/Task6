FROM python:latest

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "Rishat/manage.py", "runserver", "0.0.0.0:8000"]