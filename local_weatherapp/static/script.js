document.addEventListener('DOMContentLoaded', function() {
    console.log('Page is loaded!')
    // Define all constants at the beginning
    const Spinner = document.querySelector('#spinner');
    const CloseAnswer = document.querySelector('#close-answer');
    const Answer = document.querySelector('#answer');
    const Form = document.querySelector('form');
    const Temperature = document.querySelector('#Temperature');
    const Weather = document.querySelector('#Weather');
    const Suggestion = document.querySelector('#Suggestion');
    const Location = document.querySelector('#Location');
    const ZipInput = document.querySelector('#name');

    // Function to toggle spinner visibility
    function spinner(flag) {
        Spinner.style.display = flag ? 'block' : 'none';
    }

    // Close answer button event listener
    CloseAnswer.addEventListener('click', function() {
        Answer.style.display = 'none';
    });
    
    // Form submission event listener
    Form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Display a message
        const zip = ZipInput.value;
        getWeather(zip);

        // Reset the form after submission
        event.target.reset();
    });

    // Function to get weather information
    async function getWeather(zip) {
        spinner(true);
        const response = await fetch(`/get_weather?zip=${zip}`);
        const data = await response.json();
        Answer.style.display = 'block';
        Location.textContent = `Location: ${data.City}, ${data.State}`;
        Temperature.textContent = `Temperature: ${data.TempF}°F`;
        Weather.textContent = `Weather: ${data.Weather}`;
        Suggestion.textContent = `Wear suggestion: ${data.suggestion}`;
        spinner(false);
    }
});
