#FROM tensorflow/tensorflow:1.14.0-py3
FROM python:3.6

# Copy our application code
WORKDIR /var/app

# . Here means current directory.
COPY . .

RUN pip install -r requirements.txt
RUN python -m spacy download en

# Expose port
EXPOSE 80

# Start the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80","--workers","1"]