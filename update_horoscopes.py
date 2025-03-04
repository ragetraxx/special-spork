import requests
from bs4 import BeautifulSoup
import json

# Horoscope signs and their corresponding page numbers
signs = {
    "aries": 1, "taurus": 2, "gemini": 3, "cancer": 4,
    "leo": 5, "virgo": 6, "libra": 7, "scorpio": 8,
    "sagittarius": 9, "capricorn": 10, "aquarius": 11, "pisces": 12
}

horoscopes = {}

for sign, num in signs.items():
    url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={num}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.find("p").get_text(strip=True)
        horoscopes[sign] = text
    else:
        horoscopes[sign] = "Horoscope not available."

# Save to horoscopes.json
with open("horoscopes.json", "w", encoding="utf-8") as f:
    json.dump(horoscopes, f, indent=4, ensure_ascii=False)