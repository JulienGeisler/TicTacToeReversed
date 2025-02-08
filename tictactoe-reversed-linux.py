from tkinter import *
import random as rd     # Zufällige Auswahl des Spielers, damit keiner einen Vorteil hat

Window = Tk()
Window.title("Tic-Tac-Toe Rückwärts")
players = ["X", "O"]  # Liste der Spieler
player = rd.choice(players)  # Zufälliger Spieler
buttons = [[0, 0, 0, 0] for _ in range(4)] 

def checklooser():
    # Horizontale Überprüfung (Reihen)
    for row in range(4):
        for col in range(2):  # Prüft 3 aufeinanderfolgende Felder
            if buttons[row][col]["text"] == buttons[row][col + 1]["text"] == buttons[row][col + 2]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row, col + 1), (row, col + 2)] 
    
    # Vertikale Überprüfung (Spalten)
    for col in range(4):
        for row in range(2):  # Prüft 3 aufeinanderfolgende Felder in der Spalte
            if buttons[row][col]["text"] == buttons[row + 1][col]["text"] == buttons[row + 2][col]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col), (row + 2, col)]
    
    # Diagonal-Überprüfung (Hauptdiagonale)
    for row in range(2):
        for col in range(2):
            if buttons[row][col]["text"] == buttons[row + 1][col + 1]["text"] == buttons[row + 2][col + 2]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col + 1), (row + 2, col + 2)]
    
    # Diagonal-Überprüfung (Neben-Diagonale)
    for row in range(2):
        for col in range(2, 4):
            if buttons[row][col]["text"] == buttons[row + 1][col - 1]["text"] == buttons[row + 2][col - 2]["text"] != "":
                return buttons[row][col]["text"], [(row, col), (row + 1, col - 1), (row + 2, col - 2)]

    # Programm nicht stoppen wenn es wenn es noch leere felder gibt 
    for row in range(4):
        for col in range(4):
            if buttons[row][col]["text"] == "":
                return None, []
            



def switchplayer(row, column):
    global player
    result, loosing_coords = checklooser()  # Prüfen, ob es einen Gewinner oder Verlierer gibt
    if buttons[row][column]["text"] == "" and result is None:
        buttons[row][column]["text"] = player
        result, loosing_coords = checklooser()  # Überprüfen, ob nach dem Zug jemand verloren hat
        if result:
            label.config(text=f"{result} Hat verloren!")
            highlight_losing_fields(loosing_coords)
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} Ist an der Reihe")


def newgame():
    global player
    player = rd.choice(players)
    label.config(text=f"{player} Ist an der Reihe")
    resetbuttonscolor()

    for row in range(4):
        for col in range(4):
            buttons[row][col]["text"] = ""


def resetbuttonscolor():
    for row in range(4):
        for col in range(4):
            buttons[row][col].config(bg="lightgray")


def highlight_losing_fields(loosing_coords):
    for (row, col) in loosing_coords:
        buttons[row][col].config(bg="red")          




label = Label(text=f"{player} Ist an der Reihe", font=('', 30))
label.pack(side="top")

reset = Button(text="Von vorne anfangen", font=('', 20), command=newgame)
reset.pack()

frame = Frame(Window)
frame.pack()

for row in range(4):
    for column in range(4):
        buttons[row][column] = Button(frame, text="", font=('', 40), width=5, height=2,
                                      command=lambda row=row, column=column: switchplayer(row, column)) # Lambda wird benutzt um die funktionen auf zu rufen wenn der Knopf gedrückt wird
        buttons[row][column].grid(row=row, column=column)

Window.mainloop()
