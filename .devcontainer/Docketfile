FROM python:3.10

# Install Neo4j
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add - && \
    echo 'deb https://debian.neo4j.com stable 4.4' | tee /etc/apt/sources.list.d/neo4j.list && \
    apt-get update && \
    apt-get install -y neo4j && \
    apt-get clean

# Set environment variables
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes

# Expose Neo4j browser and bolt port
EXPOSE 7474 7687

# Start Neo4j in background and run bash
CMD service neo4j start && tail -f /dev/null
