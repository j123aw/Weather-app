async function getWeather() {
  const city = document.getElementById('cityInput').value.trim();
  const apiKey = 'ddaa48de39ce058e0739f630a12df479'; // 🔁 Replace with your actual API key
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    const weatherText = `
      🌍 Location: ${data.name}<br>
      🌡️ Temperature: ${data.main.temp}°C<br>
      🌥️ Condition: ${data.weather[0].description}
    `;
    document.getElementById("weatherResult").innerHTML = weatherText;
  } catch (error) {
    document.getElementById("weatherResult").innerHTML = `❌ Error: ${error.message}`;
  }
}
