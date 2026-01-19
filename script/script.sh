#!/bin/bash 

# Sending requests to FastAPI application to generate metrics

for i in {1..1000}; do
    # Send GET request to the root endpoint
    curl -s http://localhost:8000/cars > /dev/null

    # Send GET request with id 
    curl -s http://localhost:8000/cars/$i > /dev/null

    # Send POST request to crete
    curl -X POST http://localhost:8000/cars > /dev/null

    # Small delay between requests
    sleep 0.1

    # Send PUT request to update
    curl -X PUT http://localhost:8000/cars/$i > /dev/null

    # Send DELETE request to delete
    curl -X DELETE http://localhost:8000/cars/$i > /dev/null
done