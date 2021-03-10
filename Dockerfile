
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /code/
