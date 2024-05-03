
const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const statusText = document.getElementById('status');
let recognition; // Declare recognition variable outside event listeners

recordButton.addEventListener('click', () => {
    recordButton.disabled = true;
    stopButton.disabled = false; // Enable stop button when recording starts
    statusText.textContent = 'Recording...';

    recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        statusText.textContent = 'Sending...';
        sendTranscript(transcript);
    };

    recognition.onerror = function(event) {
        console.error('Speech recognition error:', event.error);
        statusText.textContent = 'Speech recognition error.';
        enableButtons();
    };
});

stopButton.addEventListener('click', () => {
    recognition.stop(); // Stop the recognition
    enableButtons();
    statusText.textContent = 'Recording stopped.';
});

// Function to send transcript data
function sendTranscript(transcript) {
    // Get CSRF token
    const csrftoken = getCookie('csrftoken');

    // Send POST request with CSRF token in headers
    fetch('/upload_audio/', {
        method: 'POST',
        body: JSON.stringify({ transcript: transcript }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.text())
    .then(data => {
        statusText.textContent = data;
        enableButtons();
    })
    .catch(error => {
        console.error('Error:', error);
        statusText.textContent = 'Error occurred.';
        enableButtons();
    });
}

// Function to enable buttons after recording stops or errors occur
function enableButtons() {
    recordButton.disabled = false;
    stopButton.disabled = true;
}

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Search for the CSRF cookie name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
