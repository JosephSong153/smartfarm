from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Farm Running"}

@app.get("/revenue")
def revenue():
    yield_kg = random.uniform(180, 220)
    price = 15000
    heating_cost = random.uniform(200000, 300000)
    power_cost = random.uniform(100000, 150000)

    total_sales = yield_kg * price
    net_profit = total_sales - (heating_cost + power_cost)

    return {
        "yield_kg": round(yield_kg, 2),
        "total_sales": round(total_sales, 2),
        "net_profit": round(net_profit, 2)
    }
