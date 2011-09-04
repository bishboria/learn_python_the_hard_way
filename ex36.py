from sys import exit

def user_input():
    return raw_input("> ")

def display_to_user(*args):
    for i in args:
        print i

def not_greedy(gold_taken):
    return gold_taken < 50

def gold_room():
    display_to_user("This room is full of gold. How much do you take?")

    next = user_input()

    if int(next):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if not_greedy(how_much):
        display_to_user("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    display_to_user(
        "There is a bear here.",
        "The bear has a bunch of honey.",
        "The fat bear is in front of another door.",
        "How are you going to move the bear?"
    )
    bear_moved = False

    while True:
        next = user_input()

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            display_to_user("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            display_to_user("I got no idea what that means.")

def cthulu_room():
    display_to_user(
        "Here you see the great evil Cthulu.",
        "He, it, whatever stares at you and you go insane.",
        "Do you flee for your life or eat your head?"
    )

    next = user_input()

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    display_to_user("%s Good job!" % why)
    exit(0)

def start():
    display_to_user(
        "You are in a dark room.",
        "There is door to your right and left.",
        "Which one do you take?"
    )

    next = user_input()

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
