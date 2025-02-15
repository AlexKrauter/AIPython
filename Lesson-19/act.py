import requests, random, html, time, os
CATEGORY = 9
URL = f'https://opentdb.com/api.php?amount=10&category={CATEGORY}&type=multiple'
def getquestions():

    response = requests.get(URL)

    if response.status_code != 200: return f'Failed to retrieve questions: Error {response.status_code}'

    #print(f'Full JSON Response: {response.json()}')

    data = response.json()

    return data['results']

def main():
    
    questions = getquestions()

    score = 0

    order = ''
    
    print('Welcome to the education quiz!\n')
    time.sleep(1)
    print('Please select a category')
    
    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]
        options = incorrects + [correct]
        random.shuffle(options)

        print(f'Question {i}: {question}')

        for i, option in enumerate(options,1):
            print(f'{i}. {option}')



        while True:
            try:
                answer = int(input('What is your choice (1-4): '))
                if 1 <= answer <= 4:
                    break
            except ValueError:
                pass
            print('Invalid input! Please enter 1-4')

        if options[answer-1] == correct:
            print(f'✅ Correct! You guessed: {correct}')
            order += '✅ '
            score += 1
        else:
            print(f'❌ Incorrect! Correct answer: {correct}')
            order += '❌ '

    print(f'Final Score: {score}/{len(questions)}')
    print(f'Percentage: {score/len(questions)*100}%')
    print(f'Question order: {order[:-1]}')


if __name__ == '__main__':

    main()

