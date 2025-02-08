import requests
def joke():
    url = 'https://official-joke-api.appspot.com/jokes/random'

    response = requests.get(url)

    if response.status_code != 200: return f'Failed to retrieve joke: {response.status_code}'

    print(f'Full JSON Response: {response.json()}')

    result = response.json()

    return f'{result['setup']} - {result['punchline']}'

def main():
    print('Welcome to the random joke generator!')

    while True:
        answer = input('Press Enter to get a new joke, or type q / exit to quit: ').strip().lower()

        if answer in ('q', 'exit'):

            print('Alright, see you soon!')

            break
    
        print(joke())

if __name__ == '__main__':

    main()

