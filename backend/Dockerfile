FROM python:3.9-alpine


RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY .. /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

#ENV CONTAINER_HOME=/var/www
#ADD . $CONTAINER_HOME
#WORKDIR $CONTAINER_HOME

#RUN pip install -r $CONTAINER_HOME/requirements.txt


EXPOSE 8000


