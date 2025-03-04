function fetchHoroscope() {
    let sign = document.getElementById("zodiac-sign").value;
    if (!sign) {
        alert("Please select a zodiac sign!");
        return;
    }

    fetch("horoscopes.json")
        .then(response => response.json())
        .then(data => {
            document.getElementById("horoscope-text").innerText = data[sign] || "Horoscope not found.";
            document.getElementById("horoscope-sound").play(); // Play sound when opening horoscope
        })
        .catch(error => {
            document.getElementById("horoscope-text").innerText = "Error loading horoscopes.";
            console.error("Error:", error);
        });
}