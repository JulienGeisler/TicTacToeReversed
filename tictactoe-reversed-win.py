from tkinter import *
import random as rd


def checklooser():
    for row in range(4):
        for col in range(2):
            if buttons[row][col]["text"] == buttons[row][col + 1]["text"] == buttons[row][col + 2]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row, col + 1), (row, col + 2)]
    for col in range(4):
        for row in range(2):
            if buttons[row][col]["text"] == buttons[row + 1][col]["text"] == buttons[row + 2][col]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col), (row + 2, col)]
    for row in range(2):
        for col in range(2):
            if buttons[row][col]["text"] == buttons[row + 1][col + 1]["text"] == buttons[row + 2][col + 2][
                "text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col + 1), (row + 2, col + 2)]
    for row in range(2):
        for col in range(2, 4):
            if buttons[row][col]["text"] == buttons[row + 1][col - 1]["text"] == buttons[row + 2][col - 2][
                "text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col - 1), (row + 2, col - 2)]

    for row in range(4):
        for col in range(4):
            if buttons[row][col]["text"] == "":
                return None, []

    return "tie", []


def switchplayer(row, column):
    global player
    if buttons[row][column]["text"] == "" and checklooser()[0] is None:
        buttons[row][column]["text"] = player
        result, loosing_coords = checklooser()

        if result == "tie":
            label.config(text="Unentschieden")
            reset_buttons_color()
        elif result:
            label.config(text=f"{result} Hat verloren!")
            highlight_losing_fields(loosing_coords)
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} Ist an der Reihe")


def newgame():
    global player
    player = rd.choice(players)
    label.config(text=f"{player} Ist an der Reihe")
    reset_buttons_color()

    for row in range(4):
        for col in range(4):
            buttons[row][col]["text"] = ""


def reset_buttons_color():
    for row in range(4):
        for col in range(4):
            buttons[row][col].config(bg="SystemButtonFace")


def highlight_losing_fields(loosing_coords):
    for (row, col) in loosing_coords:
        buttons[row][col].config(bg="red")


Window = Tk()
Window.title("Tic-Tac-Toe Rückwärts")
players = ["X", "O"]
player = rd.choice(players)
buttons = [[0, 0, 0, 0] for _ in range(4)]

label = Label(text=f"{player} Ist an der Reihe", font=('', 30))
label.pack(side="top")

reset = Button(text="Von vorne anfangen", font=('', 20), command=newgame)
reset.pack()

frame = Frame(Window)
frame.pack()

for row in range(4):
    for column in range(4):
        buttons[row][column] = Button(frame, text="", font=('', 40), width=5, height=2,
                                      command=lambda row=row, column=column: switchplayer(row, column))
        buttons[row][column].grid(row=row, column=column)

Window.mainloop()
