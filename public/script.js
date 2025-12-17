// Weather Dictionary Data
const weatherDictionary = {
  "temperature": "The degree of hotness or coldness of the air, measured on a definite scale.",
  "humidity": "The amount of water vapor present in the air, usually expressed as a percentage.",
  "pressure": "The force exerted by the weight of the atmosphere, measured in millibars or inches of mercury.",
  "wind": "Air in natural motion, characterized by direction and speed.",
  "precipitation": "Any form of water - liquid or solid - falling from clouds, including rain, snow, sleet, and hail.",
  "cloud": "A visible mass of water droplets or ice crystals suspended in the atmosphere.",
  "fog": "A thick cloud of tiny water droplets suspended in the atmosphere near the earth's surface, reducing visibility.",
  "drizzle": "Light rain consisting of very small water droplets.",
  "thunderstorm": "A storm with thunder and lightning, typically accompanied by heavy rain or hail.",
  "tornado": "A violently rotating column of air extending from a thunderstorm to the ground.",
  "hurricane": "A severe tropical cyclone with sustained winds exceeding 74 mph.",
  "frost": "A deposit of small white ice crystals formed when water vapor condenses at temperatures below freezing.",
  "dew": "Water droplets that form on cool surfaces at night when atmospheric vapor condenses.",
  "clear": "Sky condition with no clouds or very few clouds.",
  "overcast": "Sky condition when clouds cover most or all of the sky.",
  "visibility": "The greatest distance at which objects can be seen and identified.",
  "UV index": "A measure of the strength of ultraviolet radiation from the sun.",
  "barometer": "An instrument that measures atmospheric pressure.",
  "celsius": "A temperature scale where water freezes at 0° and boils at 100°.",
  "fahrenheit": "A temperature scale where water freezes at 32° and boils at 212°."
};

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

function searchTerm() {
  const searchInput = document.getElementById('termSearch').value.trim().toLowerCase();
  const resultDiv = document.getElementById('dictionaryResult');
  
  if (!searchInput) {
    resultDiv.innerHTML = '<p class="info-message">Please enter a weather term to search.</p>';
    return;
  }
  
  // Search for exact match or partial match
  let found = false;
  let resultHTML = '';
  
  for (const [term, definition] of Object.entries(weatherDictionary)) {
    if (term.toLowerCase() === searchInput) {
      // Exact match
      resultHTML = `
        <div class="term-card">
          <h3 class="term-name">${term.charAt(0).toUpperCase() + term.slice(1)}</h3>
          <p class="term-definition">${definition}</p>
        </div>
      `;
      found = true;
      break;
    } else if (term.toLowerCase().includes(searchInput)) {
      // Partial match - add to results
      resultHTML += `
        <div class="term-card">
          <h3 class="term-name">${term.charAt(0).toUpperCase() + term.slice(1)}</h3>
          <p class="term-definition">${definition}</p>
        </div>
      `;
      found = true;
    }
  }
  
  if (found) {
    resultDiv.innerHTML = resultHTML;
  } else {
    resultDiv.innerHTML = `<p class="error-message">❌ No weather term found matching "${searchInput}"</p>`;
  }
}

// Allow Enter key to search
document.addEventListener('DOMContentLoaded', function() {
  const termInput = document.getElementById('termSearch');
  if (termInput) {
    termInput.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        searchTerm();
      }
    });
  }
  
  const cityInput = document.getElementById('cityInput');
  if (cityInput) {
    cityInput.addEventListener('keypress', function(event) {
      if (event.key === 'Enter') {
        getWeather();
      }
    });
  }
});
