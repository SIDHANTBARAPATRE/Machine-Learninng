# base image
FROM python:3.7

 # copy everything present int the current working directory into the app folder oresent in the base image.
COPY . /app     
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py