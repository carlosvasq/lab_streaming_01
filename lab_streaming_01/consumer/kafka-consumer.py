import logging
from kafka import KafkaConsumer
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get environment variables
bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS', 'kafka:9092')
topic_name = os.getenv('TOPIC_NAME', 'mysql-operaciones')
group_id = os.getenv('GROUP_ID', 'id1')

# Create a consumer for the topic
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[bootstrap_servers],
    auto_offset_reset='earliest',  # Start reading from the beginning
    enable_auto_commit=True,
    group_id=group_id,  # Set a group ID for managing offsets
    value_deserializer=lambda x: x.decode('utf-8')
)

# Read messages from the topic
for message in consumer:
    logging.info(f"Received message: {message.value}")
