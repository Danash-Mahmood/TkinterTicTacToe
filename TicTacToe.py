from tkinter import *
import random

def next_turn(row, column):
    global player  # this means we are using player as a global variable and not just in the local scope
    if buttons[row][column]['text'] == "" and check_winner() is False:  # So if the square hasn't been chosen and there is no winner yet, activate this code block
        # the third ['text'] parameter accesses the text at an index
        if player == "x":
            buttons[row][column]['text'] = "x"
            if check_winner() is False:
                player = "o"
                label.config(text=(player + " turn"))  # if there is no winner when the previous player chooses a square, then switch the players
            elif check_winner() is True:
                label.config(text=(player + " wins"))  # if there is a winner display the winner
            elif check_winner() == "Tie":
                label.config(text=("Tie"))  # displays a tie if it's a draw
        else:  # if player == "o"
            if player == "o":
                buttons[row][column]['text'] = "o"
                if check_winner() is False:
                    player = "x"
                    label.config(text=(player + " turn"))  # if there is no winner when the previous player chooses a square, then switch the players
                elif check_winner() is True:
                    label.config(text=(player + " wins"))  # if there is a winner display the winner
                elif check_winner() == "Tie":
                    label.config(text=("Tie"))  # displays a tie if it's a draw

def check_winner():
    # We need to check all the horizontal win conditions for each row using a for loop
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True  # if all the elements along a row are the same and non-empty someone won

    # We need to check all the vertical win conditions for each column using a for loop
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True  # if all the elements along a row are the same and non-empty someone won

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True  # checking the negative diagonal
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True  # checking the positive diagonal
    elif empty_spaces() is False:
        return "Tie"  # if there are no more empty spaces and the win conditions aren't met then it's a tie
    else:
        return False  # no one has won and it's not a tie yet

def empty_spaces():
    spaces = 9  # we want to loop through each square and see if out of the 9 squares, how many are filled
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False  # no empty spaces left
    else:
        return True

def new_game():
    # this function will just reset everything back
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")  # sets all of the buttons back to blank

window = Tk()  # makes a Tk object
window.title("Noughts and Crosses")  # use the title method to rename the pop-up window

players = ["x", "o"]
player = random.choice(players)  # Chooses a random player from the players array

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]  # initialize 2D list with values of 0 for now

label = Label(text=player + " turn", font=("consolas", 40))  # creates a label object?
label.pack(side="top")

reset_button = Button(text="reset", font=('consolas', 40), command=new_game)  # does this create a button object or function
reset_button.pack(side="top")

frame = Frame(window)  # create a Frame object and pass the window Tk object in it
frame.pack()

# Now we loop through the buttons array to add a button at each point in the matrix which gets added to the Frame which is added to the window
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))  # This is use of a lambda function where we use kwargs of row and column and then call the next_turn function with these as the parameters
        buttons[row][column].grid(row=row, column=column)  # use the grid method with kwargs of row and column

window.mainloop()
