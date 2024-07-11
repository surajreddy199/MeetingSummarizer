# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the local code to the container
COPY . .

# Expose the port number the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
