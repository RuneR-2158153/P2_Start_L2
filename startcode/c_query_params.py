# Maak een programma dat:
# - De naam van de gebruiker vraagt.
# - De naam van de gebruiker doorstuurt naar de API.
# - Een tekstje print met de naam en de voorspelde leeftijd.

import requests
naam = input("Geef jouw naam: ")
response = requests.get(
    url="https://api.agify.io/",
    params={"name": naam}
)
if response.status_code == 200:
    data = response.json()
    print(data["age"])
else:
    print(f"Error code{response.status_code}")