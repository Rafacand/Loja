# base image  
FROM python:3.10.12  doc
RUN mkdir /code
WORKDIR /code
COPY requeriments.txt /code/
RUN pip install -r requeriments.txt
EXPOSE 8000
COPY . /code/