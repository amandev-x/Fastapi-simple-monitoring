from fastapi import FastAPI
from prometheus_client import Counter, start_http_server
import uvicorn

# Counting the number of http requests
REQUESTS = Counter("http_requests_total", "Total number of HTTP requests", ["method", "endpoint"])

# Create FastAPI app
app = FastAPI()

@app.get("/cars")
async def get_cars():
    REQUESTS.labels("get", "/cars").inc() # Increment the request counter by 1.
    return ["Toyota", "Honda", "Ford", "Mercedes", "Audi", "BMW", "Koenigsegg"]

@app.get("/cars/{car_id}")
async def get_car_by_id(car_id: int):
    REQUESTS.labels("get", "/cars/car_id").inc()
    return "Single Card"

@app.post("/cars")
async def create_car():
    REQUESTS.labels("post", "/cars").inc()
    return "Car created"

@app.put("/cars/{car_id}")
async def update_car(car_id: int):
    REQUESTS.labels("put", "/cars/{car_id}").inc()
    return "Car updated"

@app.delete("/cars/{car_id}")
async def delete_car(car_id: int):
    REQUESTS.labels("delete", "/car/{car_id}").inc()
    return "Car deleted"


if __name__ == "__main__":
    # Start Prometheus metrics server on port 8001
    start_http_server(8001)

    # Start FastAPI app on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
