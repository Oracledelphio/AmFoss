document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "1b80fb913eb0ecf9f28e11b0902b41eb"; 
    const weatherInfo = document.getElementById("weatherInfo");
    const searchButton = document.getElementById("searchButton");

    searchButton.addEventListener("click", () => {
        const locationInput = document.getElementById("locationInput").value;

        if (locationInput) {
            fetchWeatherData(locationInput, apiKey);
        } else {
            alert("Please enter a location.");
        }
    });

    function fetchWeatherData(location, apiKey) {
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=metric`;

        fetch(apiUrl)
            .then((response) => response.json())
            .then((data) => {
                if (data.cod === 200) {
                    const temperature = data.main.temp;
                    const description = data.weather[0].description;

                    const weatherHTML = `
                        <p>Location: ${location}</p>
                        <p>Temperature: ${temperature}°C</p>
                        <p>Description: ${description}</p>
                    `;

                    weatherInfo.innerHTML = weatherHTML;
                } else {
                    weatherInfo.innerHTML = `<p>Location not found. Please try again.</p>`;
                }
            })
            .catch((error) => {
                console.error("Error fetching weather data:", error);
                weatherInfo.innerHTML = `<p>An error occurred. Please try again later.</p>`;
            });
    }
});
