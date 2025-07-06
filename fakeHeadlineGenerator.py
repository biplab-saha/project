# import the random module
import random
# create subject
subjects=[
    "Shahrukh khan",
    "Virat Kohli",
    "A Hoogly Dog",
    "A Group Of Monkeys",
    "Prime Minister Modi",
    "Magic Driver From Inchura Magra Road"
    ]

actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "orders",
    "celebrates",
]
placesOrThings=[
    "at Red Fort",
    "WestBengal Local Train",
    "a plate of singara",
    "inside parliament",
    "at Ganga Ghat",
    "druring IPL Match",
    "at India Gate"
]

# start the headline generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    placeOrThing=random.choice(placesOrThings)
    
    headline = f" BREAKING NEWS: {subject} {action} {placeOrThing} "
    print("\n"+ headline)
    
    userInput=input("\n Do you want another headline? (Yes/No) ").strip().lower()
    if userInput =="no":
        break
    
print("\n Thanks for using the Fake News Headline Generator.Have a fun day")    