FROM node:12

ENV PORT 3000

# Create app directory
RUN mkdir -p /pushInsights_Front_prod
WORKDIR /pushInsights_Front_prod

# Installing dependencies
COPY package*.json /pushInsights_Front_prod/
RUN yarn install

# Copying source files
COPY . /pushInsights_Front_prod/

# Building app
RUN yarn run build

# Expose the listening port
EXPOSE 3000
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf

# Running the app
CMD "yarn" "next" "start"