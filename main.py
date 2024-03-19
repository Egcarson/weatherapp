from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates/static"), name="static")

OPENWHEATHERMAP_API_KEY = "d08981263c09df4ad1541dcf5953a221"

async def get_weather_data(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWHEATHERMAP_API_KEY,
        "units": "metric"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Weather data not found")
        
        return response.json()

@app.get("/", response_class=HTMLResponse)
async def get_weather_page():
    return FileResponse("templates/index.html")

@app.get("/weather")
async def get_weather(city: str):
    weather_data = await get_weather_data(city)
    return {
        "city": city,
        "weather": weather_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)