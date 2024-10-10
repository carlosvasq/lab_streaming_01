# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir kafka-python

# Set environment variables
ENV BOOTSTRAP_SERVERS="kafka:9092"
ENV TOPIC_NAME="mysql-operaciones"
ENV GROUP_ID="id1"

# Add the Python Kafka Consumer script to the container
COPY kafka-consumer.py /app/kafka-consumer.py

# Run the Python consumer script
CMD ["python", "/app/kafka-consumer.py"]
