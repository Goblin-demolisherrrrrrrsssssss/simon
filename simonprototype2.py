import tkinter as tk
import time
import winsound
import sys
userSequence=[]
wrong = False
import random 
sequence = []
root = tk.Tk()
colours = ["GREEN","BLUE","RED","YELLOW"]
points = 0
name = ""
sound_map = {
    "RED": 440,     # A4
    "GREEN": 523,   # C5
    "BLUE": 349,    # F4
    "YELLOW": 392   # G4
}
def newRound():
    userSequence.clear()
    sequence.append(random.choice(colours))
    #print(sequence)
    for i in range(len(sequence)):
        colour = sequence[i]
        if colour == "RED":
            btn = rbutton
            orig = "red"
            new="orangered"
        elif colour == "BLUE":
            btn = bbutton
            orig = "blue"
            new="cyan"
        elif colour == "GREEN":
            btn = gbutton
            orig = "green"
            new="springgreen1"
        else:
            btn = ybutton
            orig = "yellow"
            new="gold1"

        btn.config(bg=new)
        root.update()
        root.after(500)

        btn.config(bg=orig)
        root.update()
        winsound.Beep(sound_map[colour], 400)
        root.after(300)


def buttonClick(colour):
    global points
    userSequence.append(colour)
    print(f"Pressed: {colour}\n")
    for x in range(len(userSequence)):
        if userSequence[x] != sequence[x]:
            rbutton.config(bg="black", state=tk.DISABLED)
            gbutton.config(bg="black", state=tk.DISABLED)
            bbutton.config(bg="black", state=tk.DISABLED)
            ybutton.config(bg="black", state=tk.DISABLED)
            label.config(text="GAME OVER")
            print("Oops! Wrong colour. Game over.")
            print(f"Game Over! You scored {points} points!")
            pointAdder = open("points.txt", "a")
            pointAdder.write(f"{name}: {points}\n")
            pointAdder.close()
            sys.exit(0)
            
    if userSequence == sequence:
        print("Correct!\n")
        points += 1
        label.config(text="Correct, on "+str(points)+" points")
        root.after(600,newRound)
        
label = tk.Label(root, text="hello", font=("Arial", 14))

rbutton = tk.Button(root,
                    text="",
                    command=lambda:buttonClick("RED"),
                    activebackground="white",
                    activeforeground="black",
                    anchor="n",
                    bd=3,
                    bg="red",
                    cursor="hand2",
                    disabledforeground="black",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)


gbutton = tk.Button(root,
                    text="",
                    command=lambda:buttonClick("GREEN"),
                    activebackground="white",
                    activeforeground="black",
                    anchor="e",
                    bd=3,
                    bg="green",
                    cursor="hand2",
                    disabledforeground="black",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

bbutton = tk.Button(root,
                    text="",
                    command=lambda:buttonClick("BLUE"),
                    activebackground="white",
                    activeforeground="black",
                    anchor="s",
                    bd=3,
                    bg="blue",
                    cursor="hand2",
                    disabledforeground="black",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

ybutton = tk.Button(root,
                    text="",
                    command=lambda:buttonClick("YELLOW"),
                    activebackground="white",
                    activeforeground="black",
                    anchor="w",
                    bd=3,
                    bg="yellow",
                    cursor="hand2",
                    disabledforeground="black",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

rbutton.grid(row = 0, column = 0,  pady = 10, padx= 10)
bbutton.grid(row = 1, column = 0,  pady = 10, padx= 10)
gbutton.grid(row = 0, column = 1,  pady = 10, padx= 10)
ybutton.grid(row = 1, column = 1,  pady = 10, padx= 10)
label.grid(row= 1, column=2, pady = 10, padx= 10)



    #rbutton.place(rely=1.0, relx=1.0,  anchor="se")
    #gbutton.place(rely=1.0, relx=0.0,  anchor="ne")
    #bbutton.place(rely=0.0, relx=1.0,  anchor="sw")
    #ybutton.place(rely=0.0, relx=0.0,  anchor="ne")

    #rbutton.pack(padx=20, pady=20)
    #gbutton.pack(padx=20, pady=20)
    #bbutton.pack(padx=20, pady=20)
    #ybutton.pack(padx=20, pady=20)


newRound()
root.mainloop()
