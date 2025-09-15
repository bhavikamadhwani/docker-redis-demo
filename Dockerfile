version: '3.8'

# Define a custom network named "app-network"
networks:
  app-network:
    driver: bridge

services:
  web:
    build: .
    ports:
      - "5000:5000"  # Railway will provide its own public port, but internal mapping is needed
    depends_on:
      - redis
    # Connect the web service to the custom network
    networks:
      - app-network
    # Add an environment variable for the Redis URL (optional but good practice)
    environment:
      - REDIS_HOST=redis  # This tells the app to use the hostname 'redis'

  redis:
    image: "redis:alpine"
    # Connect the redis service to the same custom network
    networks:
      - app-network
    # Optional: Add a volume to persist Redis data between deploys
    volumes:
      - redis_data:/data

# Define a volume to persist Redis data
volumes:
  redis_data:
