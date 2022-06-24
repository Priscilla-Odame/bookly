# pulling an official python base image
FROM python:3.8.5-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip to latest version
RUN pip install --upgrade pip

# install dependencies (mainly for cryptography and postgres-db)
RUN apk update && apk add libpq gcc musl-dev libffi-dev openssl-dev python3-dev postgresql-dev

# copying and installing requirements from requirements.txt file
COPY ./backend/requirements.txt .
RUN pip install --no-cache -r requirements.txt

# adding google dns resolver to container
RUN echo 'nameserver 8.8.8.8' >> /etc/resolv.conf

# copying project files from local machine to docker container instance 
COPY ./backend /rest_api
COPY ./docker/backend/scripts /scripts

# making all scripts sxecutable
RUN chmod +x /scripts/*

# setting work directory for docker
WORKDIR /rest_api

# # setting up linter
# RUN pip install flake8
# RUN flake8 --ignore=E501,F401 .

RUN mkdir -p /vol/web/static
RUN mkdir -p /vol/web/media

# including security requirements
RUN adduser -D pushinsights
RUN chown -R pushinsights:pushinsights /vol
RUN chmod -R 755 /vol/web 

# switching to different user to enforce security requirements
USER pushinsights

ENTRYPOINT ["sh", "/scripts/entrypoint.sh"]