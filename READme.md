# FastAPI Weather App

Welcome to the FastAPI Weather App! This project is a web application built with FastAPI that allows users to retrieve current weather information for a specific location using the OpenWeatherMap API.

## Features

- **Weather Data Retrieval:** Users can input a city name and retrieve current weather information for that city.
- **Not Responsive Design:** The web interface is designed to just grab the API result.
- **Asynchronous Processing:** The backend utilizes asynchronous programming with FastAPI to handle concurrent requests efficiently.
- **Static Files:** CSS and JavaScript files are served statically to enhance the user interface and functionality of the weather app.

## Technologies Used

- **FastAPI:** FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **OpenWeatherMap API:** The OpenWeatherMap API is used to retrieve weather data for the specified city.
- **HTML/CSS/JavaScript:** The frontend of the weather app is built using HTML for structure, CSS for styling, and JavaScript for interactivity.
- **HTTPx:** HTTPx is used as the HTTP client for making requests to the OpenWeatherMap API asynchronously.

## Installation

1. Cone the repository
```bash
git clone https://github.com/your-username/fastapi-weather-app.git
```

2. Navigate to the project directory: 
```bash
cd fastapi-weather-app
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/) and replace "OPENWEATHERMAP_API_KEY" in main.py with your actual API key.

## Usage

1. Run the FastAPI application:
```bash
uvicorn main:app --reload
```

2. Open your web browser and navigate to http://localhost:8000 to access the weather app.
3. Enter a city name in the input field and click "Get Weather" to retrieve the current weather information for that city.

## Deployment

Make sure to configure environment variables for sensitive information such as API keys, and follow the deployment guides provided by the chosen platform.

## Contributing

Contributions to the FastAPI Weather App are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request on GitHub.
