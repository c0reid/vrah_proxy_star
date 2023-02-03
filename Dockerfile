FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/
WORKDIR /code
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev
RUN pip install -r requirements.txt
EXPOSE 8112
EXPOSE 5432
COPY . /code/
