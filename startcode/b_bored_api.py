# Gebruik de bored api om een JSON-bestand in te lezen: https://www.boredapi.com/api/activity
# De response als json interpreteren kan zo: data = response.json()
import requests

response = requests.get("http://bored.api.lewagon.com/api/activity?type=recreational")
if response.status_code == 200:
    data = response.json()
    print(data["activity"])
else:
    print("error")