#HighCard.py
import random as arbituary
suits=['clubs', 'diamonds', 'spades', 'hearts']
faces=['two', 'four', 'six', 'eight', 'nine', 'seven', 'five', 'three', 'ten','jack', 'ace', 'king', 'queen']
keep_going = True
while keep_going:
    my_face = arbituary.choice(faces)
    my_suit = arbituary.choice(suits)
    your_face = arbituary.choice(faces)
    your_suit = arbituary.choice(suits)
    print("I have the", my_face, "of", my_suit)
    print("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("Congrations! You finally won at something!")
    elif faces.index(my_face) < faces.index(your_face):
        print("Congratulations!!!..... you are a loser, Officer Diarrhea!")
    else:
        print("So you are both technically losers!!!")
    answer = input("Hit [Enter] to keep going, any other key to be a quitter: ")
    keep_going = (answer == "")


