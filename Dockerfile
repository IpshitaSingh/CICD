#use Python as the base image
FROM python:3.8

#set the working directory in the container
WORKDIR /app

#copy current directory contents into the container at /app
COPY . /app

#install the app using setuptools
RUN python -m pip install --upgrade pip \
    && python setup.py install

#expose port 8080
EXPOSE 8080

#set the entry point and default command to run the application
CMD ["app"]





