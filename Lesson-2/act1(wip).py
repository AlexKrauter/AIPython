from textblob import TextBlob
import colorama
from colorama import Fore, Style
import sys
import time
user_name = ""
conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_prossessing_animation():
    print(f'{Fore.CYAN}🕵️ Detecting sentiment clues', end='')
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()

def analyze_sentimen(text):
    try:
        global positive_count, negative_count, neutral_count
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        conversation_history.apped(text)

        if sentiment > 0.75:
            positive_count += 1
            return f"\n{Fore.LIGHTGREEN_EX}😃 Very Positive sentiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN}🙂 Positive sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        elif -0.25 <= sentiment <= 0.25:
            neutral_count += 1
            return f"\n{Fore.YELLOW}😐 Neutral sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        elif -0.75 <= sentiment < -0.25:
            negative_count += 1
            return f"\n{Fore.RED}🙁 Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        else:
            negative_count += 1
            return f"\n{Fore.MAGENTA}😠 Very Negative sentiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
    except Exception as e:
        return f"\n{Fore.BLUE}❔ Sentiment undetected, Agent {user_name}. (Error: {str(e)})"

    
        