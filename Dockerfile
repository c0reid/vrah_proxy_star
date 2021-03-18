FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
WORKDIR /code
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8111
EXPOSE 5432
COPY . /code/
