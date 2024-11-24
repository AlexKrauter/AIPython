import re, random, time

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = {
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
}

class TravelBot():
    def __init__():
        print("Hello! I'm TravelBot, your virtual travel assistant.")
        name = input("May I please know your name? ")
        print(f"Nice to meet you, {name}! How can I assist you today?")
    def help():
        print("\nI can assist you with the following:")
        print("- Provide travel recommendations")
        print("- Check flight status")
        print("- Offer packing tips")
        print("- Tell travel jokes")
        print("Just ask me a question or type exit to leave.\n")
    def process(input):
        return re.sub(r'[^\w\s]','',input).lower()
    def recommend():
        print("Sure! Are you interested in beaches, mountains, or cities?")
        preference = input().lower()
        if preference in destinations:
            suggestion = random.choice(destinations[suggestion])
            print(f"How about visiting suggestion?")
        else:
            print("Sorry, I don't have recommendations for that preference. Prehaps check your spelling.")
    def flight():
        print("Please enter your flight number.")
        flight_number = input().upper()
        for i in range(10):
            time.sleep(0.6)
            
        