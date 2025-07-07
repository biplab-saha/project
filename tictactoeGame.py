import tkinter as tk
from tkinter import messagebox

def checkWinner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe",f"Player {buttons[combo[0]]["text"]} wins!")
            root.quit()

def  buttonCheck(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = currentPlayer
        checkWinner()
        togglePlayer()

def togglePlayer():
    global currentPlayer
    currentPlayer = "X" if currentPlayer == "O" else "O"
    label.config(text=f"Player {currentPlayer}'s trun")
    
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root,text="",font=("normal",25),width=6,height=2,command=lambda i=i: buttonCheck(i))for i in range(9)]

for i , button in enumerate(buttons):
    button.grid(row=i //3, column=i %3)
    
    
currentPlayer ="X"
winner = False 
label =tk.Label(root,text=f"Player{currentPlayer}'s turn",font=("normal",16))
label.grid(row=3,column=0,columnspan=3)

root.mainloop()          