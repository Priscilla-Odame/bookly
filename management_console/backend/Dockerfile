FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SECRET='7o2-(ohb!fi!&bw21k3s9^lzm@ttrj4_4-tbtspus_+(9xif8j'
ENV DBHOST='management_db'
ENV DBNAME='management'
ENV DBUSER='postgres'
ENV DBPASS='managementpass'
ENV EMAIL_HOST="smtp.office365.com"
ENV EMAIL_HOST_USER="pushinsights@scalework.com"
ENV EMAIL_HOST_PASSWORD="Every1canaccess"
WORKDIR /managementConsole
ADD requirements.txt /managementConsole/
RUN pip install -r requirements.txt
COPY . /managementConsole/
EXPOSE 8001


