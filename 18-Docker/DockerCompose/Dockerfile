FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_RUN_HOST=0.0.0.0
# COPY INTO /CODE FOLDER
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]