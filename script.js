
const n = 10; // Number of LEDs

// Get LED strip element
const ledStrip = document.getElementById('led-strip');

// Create LED elements
for (let i = 0; i < n; i++) {
    const led = document.createElement('div');
    led.className = 'led';
    led.id = 'led-' + i;
    ledStrip.appendChild(led);
}

// Function to update LED color and glow
function updateLED(index, color) {
    const led = document.getElementById('led-' + index);
    if (led) {
        led.style.backgroundColor = color;
        const isOff = color === 'rgb(0, 0, 0)'; // Assuming 'off' is black
        led.style.boxShadow = isOff 
            ? '0 0 10px rgba(0, 0, 0, 0)' // No glow when off
            : `0 0 10px ${color}, 0 0 20px ${color}, 0 0 30px ${color}`; // Glow when on
    }
}

// WebSocket connection
const socket = new WebSocket('ws://localhost:8765');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateLED(data.index, `rgb(${data.r}, ${data.g}, ${data.b})`);
};

socket.onopen = function() {
    console.log('WebSocket connection established');
};

socket.onclose = function() {
    console.log('WebSocket connection closed');
};
