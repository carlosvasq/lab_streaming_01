# Use the Confluent Kafka Connect base image
FROM confluentinc/cp-kafka-connect:7.4.0

# Switch to root to install necessary files and change permissions
USER root

# Create directories for the connectors and download the JAR files
RUN mkdir -p /usr/share/java/kafka-connect-jdbc /usr/share/java/kafka-connect-s3 && \
    curl -o /usr/share/java/kafka-connect-jdbc/kafka-connect-jdbc.jar \
    https://packages.confluent.io/maven/io/confluent/kafka-connect-jdbc/10.7.3/kafka-connect-jdbc-10.7.3.jar && \
    curl -o /usr/share/java/kafka-connect-s3/kafka-connect-s3.jar \
    https://packages.confluent.io/maven/io/confluent/kafka-connect-s3/10.2.9/kafka-connect-s3-10.2.9.jar && \
    curl -o /usr/share/java/kafka-connect-s3/kafka-connect-storage-common.jar \
    https://packages.confluent.io/maven/io/confluent/kafka-connect-storage-common/10.2.9/kafka-connect-storage-common-10.2.9.jar && \
    curl -o /usr/share/java/kafka-connect-s3/common-config.jar \
    https://packages.confluent.io/maven/io/confluent/common-config/7.4.0/common-config-7.4.0.jar && \
    curl -o /usr/share/java/kafka-connect-s3/common-utils.jar \
    https://packages.confluent.io/maven/io/confluent/common-utils/7.4.0/common-utils-7.4.0.jar

COPY mysql-connector-java.jar /usr/share/java/kafka-connect-jdbc/

# Verify all JAR files were downloaded correctly
RUN ls -l /usr/share/java/kafka-connect-s3 /usr/share/java/kafka-connect-jdbc

# Copy the setup script into the container
COPY setup-connect.sh /setup-connect.sh

# Change permissions of the script
RUN chown appuser:appuser /setup-connect.sh && chmod +x /setup-connect.sh

# Use the non-root user for security
USER appuser

# Set the CLASSPATH and plugin path environment variables to include the new connectors
ENV CLASSPATH="/usr/share/java/kafka-connect-s3/*:/usr/share/java/kafka-connect-jdbc/*"
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/java/kafka-connect-jdbc,/usr/share/java/kafka-connect-s3"

# Run the setup script to start Kafka Connect
CMD ["bash", "/setup-connect.sh"]
