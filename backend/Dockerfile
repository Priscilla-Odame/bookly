FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /pushInsights_dev
ADD requirements.txt /pushInsights_dev/

# adding google dns resolver to container (uncomment the line below if you container has issues downloading packages)
# RUN echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
RUN pip install pip --upgrade
RUN pip install cython
# RUN python setup.py install
#RUN pip install pandas==0.25.3
# RUN pip install pandas-profiling==3.0.0
RUN pip install -r requirements.txt
COPY . /pushInsights_dev/
EXPOSE 8000

# 0.25.3
