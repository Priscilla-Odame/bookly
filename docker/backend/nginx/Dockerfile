FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/nginx.conf

RUN mkdir -p /vol/static/
RUN chmod 755 /vol/static/