import tkinter as tk
import time
userSequence=[]
wrong = False
import random 
sequence = []
root = tk.Tk()
colours = ["GREEN","BLUE","RED","YELLOW"]
points = 0
name = ""
def newRound():
    userSequence.clear()
    sequence.append(random.choice(colours))
    print(sequence)

def buttonClick(colour):
    global points
    userSequence.append(colour)
    print(f"pressed: {colour}")
    for x in range(len(userSequence)):
        if userSequence[x] != sequence[x]:
            print("Oops! Wrong colour. Game over.")
            print(f"Game Over! You scored {points} points!")
            pointAdder = open("points.txt", "a")
            pointAdder.write(f"{name}: {points}\n")
            pointAdder.close()
    if userSequence == sequence:
        print("Correct!")
        points += 1
        root.after(600,newRound)
