print("Hello! I am AI Bot. What is your name?")
name = input()
print(f"Nice to meet you, {name}!")

print("How are you feeling today? (Good/Bad)")
while True:
    
    mood = input().lower()
    
    if mood == "good":
        print(f"I'm glad to hear that, {name}!")
        break
    elif mood == "bad":
        print(f"i'm sorry to hear that, {name}. I hope things get better soon.")
        break
    else:
        print("I dont understand what you are saying. Please say good or bad.")

print(f"It was nice having a conversation with you, {name}. Goodbye!")