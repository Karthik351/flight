# Use an official Python runtime as a base image
FROM python:3.9

# Create the /app directory
RUN mkdir -p /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the project code into the container
COPY . /app/

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on (optional, depending on your needs)
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]