#use Python as the base image
FROM python:3.8

#set the working directory in the container
WORKDIR /app

#copy current directory contents into the container at /app
COPY . /app

RUN pip install flask

#expose port 8080
EXPOSE 8080

#set the entry point and default command to run the application
ENTRYPOINT ["python"]
CMD ["app.py"]
