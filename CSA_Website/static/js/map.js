const balloon_icon = L.icon({
	iconUrl: {% static 'images/mapicon.png' %}
});

const map = L.map('map', {icon: balloon_icon}).setView([48.5704, -81.3694], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
   attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const marker = L.marker([48.5704, -81.3694]);
marker.addTo(map);
