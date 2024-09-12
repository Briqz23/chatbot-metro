# Use the Redis Stack server base image
FROM redis/redis-stack-server:latest

# Expose port 6379 to the host machine
EXPOSE 6379

# Run the Redis Stack server
CMD ["redis-stack-server"]

#docker build -t my-redis-stack-server .
#docker run -d --name redis-stack-server -p 6379:6379 my-redis-stack-server
