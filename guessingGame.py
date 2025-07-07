import random

easyWord = ["apple","train","tiger","money","india"]
mediumWord = ["pyhton","bottle","magra","howrah","bandel","laptop","monkey","planet"]
hardWord = ["elephant","diamond","umbrella","mountain","computer"]

print("Wlecome to the password guessing game")
print("Choose a difficulty level: Easy(type eg.e ), Medium(type eg.m) or Hard(type eg.h)")

level = input("Enter difficulty: ").lower()
if level == "e":
    secret = random.choice(easyWord)
elif level == "m":
    secret =random.choice(mediumWord)
elif level == "h":
    secret =random.choice(hardWord)
else:
    print("Invalid choice. Defaulting to easy level")
    secret =random.choice(easyWord) 

attempts=0
print("\n Guess thw secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts+=1
    
    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts.')
        break
    
    
    hint=""
    
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
            
    print("Hint: ",hint)

print("Game Over")    