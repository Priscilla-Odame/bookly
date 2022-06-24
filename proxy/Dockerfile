FROM nginx:1.19.0-alpine

# removing previous default configurations
RUN rm /etc/nginx/conf.d/default.conf 

# copying new configurations and uwsgi params to docker container
COPY ./default.conf /etc/nginx/conf.d/default.conf

# # creating volume for persistent data
# RUN mkdir -p /pushInsights/staticfiles
# RUN mkdir -p /pushInsights/mediafiles

# RUN chmod 755 /pushInsights/staticfiles
# RUN chmod 755 /pushInsights/mediafiles

