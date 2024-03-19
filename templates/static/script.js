document.getElementById("weatherForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const city = document.getElementById("city").value;
    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();
    const weatherInfo = document.getElementById("weatherInfo");
    weatherInfo.innerHTML = `
        <p>City: ${data.city}</p>
        <p>Temperature: ${data.weather.main.temp} °C</p>
        <p>Description: ${data.weather.weather[0].description}</p>
    `;
});
