FROM ubuntu:22.04

LABEL Name=data-engineering Version=0.0.1

# Update and install basic utilities
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    software-properties-common \
    python3 \
    python3-pip
#    openjdk-11-jdk

# Set Java environment variables
# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
# ENV PATH=$PATH:$JAVA_HOME/bin

# Install Spark
#ENV SPARK_VERSION=3.5.1
#ENV SPARK_HOME=/opt/spark

#RUN wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
#    && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
#    && mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark \
#    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Add Spark to PATH
# ENV PATH=$PATH:$SPARK_HOME/bin

# Set working directory
WORKDIR /app

# Command to keep container running
CMD ["bash"]
