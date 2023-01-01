import random 
import os
import time

cards= []
pairs = []
shuffled_cards = []
board = []

deck_selected = False

choose_one = str
choose_two = str
choose_one_selected = False
choose_two_selected = False
moves = 25
game_end = False # This must start in false for the game to run




#! TO THE ONE CORRECTING THIS PROYECT: FEEL FREE TO ACTIVATE THIS CHEAT MODE TO SEE BETTER WHATS HAPPENING AND TRY THINGS WITHOUT NEED OF PLAY THE ACTUAL GAME
cheat_mode = False # The cheat mode allow you yo see all time the board with the correct answers (this is for testing and for the professors correcting this project)

# Those are the different decks the player can choose
decks = {
    'animals': {
        'cards': ("🐵", "🐶", "🐔", "🐷", "🦝", "🐱", "🦁", "🐯", "🐴", "🦄"),
        'dificulty': "hard",
        'moves': 25
    },
    'colors': {
        'cards': ("🔴", "🟡", "🟢", "🔵", "🟣", "⚫", "⚪"),
        'dificulty': "medium",
        'moves': 20
    },
    'music': {
        'cards': ("🎷", "🎸", "🥁", "📀", "🎤"),
        'dificulty': "easy",
        'moves': 15
    },
    'cloths': {
        'cards': ("👚", "👠", "👘", "🧥"),
        'dificulty': "very easy",
        'moves': 10
    }
}

# Here whe give the player the options
print("""
Choose a deck to play
1 - Animals (10 pairs / 25 moves)
2 - Colors (7 pairs / 20 moves)
3 - Music (5 pairs / 15 moves)
4 - Cloths (4 pairs / 10 moves)
""")

# This is a switch when the player input his choice, if it is one of the listed the code preceed to the set-up and the game and if it's note ask the player to choose again
while not deck_selected:
    deck = input("Deck selected: ")
    deck_selected = True
    if deck == "1" or deck.casefold() == "animals":
        cards = decks["animals"]["cards"]
        moves = decks["animals"]["moves"]
    elif deck == "2" or deck.casefold() == "colors":
        cards = decks["colors"]["cards"]
        moves = decks["colors"]["moves"]
    elif deck == "3" or deck.casefold() == "music":
        cards = decks["music"]["cards"]
        moves = decks["music"]["moves"]
    elif deck == "4" or deck.casefold() == "cloths" or deck.casefold() == "cloth":
        cards = decks["cloths"]["cards"]
        moves = decks["cloths"]["moves"]
    else:
        print("That's not one of the options")
        deck_selected = False

# This "for" transforms every card in a pair
for a in cards:
    for i in range(2):
        pairs.append(a)

# This "for" use the random method to take shuffle the position of every card on an unsorted list
for i in range(len(pairs)):
    picked = random.choice(pairs)
    pairs.remove(picked)
    shuffled_cards.append(picked)
    board.append("❔")

# "print_board() is the function that clean the console/terminal and show an updated state of the board"
def print_board():
    os.system('cls')

    if cheat_mode: # The cheat mode allow you yo see all time the board with the correct answers (this is for testing and for the professors correcting this project)
        print(shuffled_cards)

    print(board)
    print("Moves left: " + str(moves))

print_board()

while not game_end:

    # Here I make sure that the input of the player follow the conditions needed to not crash the game
    while not choose_one_selected: # I'm using a boolean that will only be true if we get to the end of al confirmations needed
        choose_one = input("Type a number between 1 and " + str(len(board)) + ": ")
        while not choose_one.isdigit(): # First check: the value must be a digit or we couldn't aply the "int()" method
            print("That's not a number!")
            choose_one = input("Type a number between 1 and " + str(len(board)) + ": ")
        choose_one = int(choose_one) - 1 # We substract 1 so the number match the system of positions on a python list
        if choose_one < 0 or choose_one > (len(board) - 1): # Second check: the value must be between the min and max coords of our list of cards
            print("That's out of range!")
        elif board[choose_one] != "❔": # Third check: the selected position cannot be diferent of "❔" (The "unselected" value)
            print("You already discover that emoji")
        else:
            choose_one_selected = True # Only when we pass all three checks we are able to change this boolean and get out of our "while"

    board[choose_one] = shuffled_cards[choose_one] # Here, when we check that the selection is a valid move, we put a selected card into the board so the player can see it...
    print_board() # ... and update the view of the player 

    # Then repeat all previous steps for a second selection
    while not choose_two_selected:
        choose_two = input("Type a number between 1 and " + str(len(board)) + ": ")
        while not choose_two.isdigit():    
            print("That's not a number!")
            choose_two = input("Type a number between 1 and " + str(len(board)) + ": ")
        choose_two = int(choose_two) - 1 
        if choose_two < 0 or choose_two > (len(board) - 1):
            print("That's out of range!")
        elif board[choose_two] != "❔":
            print("You already discover that emoji")
        else:
            choose_two_selected = True 

    board[choose_two] = shuffled_cards[choose_two]
    print_board()

    moves -= 1 # Here I know two cards has been selected so I can call that a move and substract one of the moves counter

    # When we have two selections whe check the results of the play
    if board[choose_one] != board[choose_two]: # In case the cards are different 
        print("Nop, try again") # throw a feedback message 
        board[choose_one] = board[choose_two] = "❔" # reset the values on the board for "unselected"
        choose_one_selected = choose_two_selected = False # reset the booleants so the player can continue selecting new values
    else: # In case the cards are equal 
        print("Its a match!!!") # throw a feedback message 
        choose_one_selected = choose_two_selected = False # reset the booleants so the player can continue selecting new values

    time.sleep(1) # Here I use the time method to make that the board view reset wait for one second for the player to him being able to view what happend
    if moves == 0:
        print_board()
        print("You are out of moves, you lose")
        game_end = True
    elif "❔" in board: # If there's still some undiscover pairs we just restart the board view
        print_board()
    else: # And if ther's not  undiscover pairs we throw a victory message and end the game
        print("VICTORY!!!")
        game_end = True