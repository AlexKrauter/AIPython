import requests

url = 'https://uselessfacts.jsph.pl/random.json?language=en'

for i in range(100):

    response = requests.get(url)

    if response.status_code != 200: break

    data = response.json()

    print(data['text'])