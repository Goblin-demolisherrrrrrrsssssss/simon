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
    print("New round!\n")
    time.sleep(2)
    for y in range(len(sequence)):
        if sequence[y] == "RED":
            flash_button("RED",print(""))
        elif sequence[y] == "GREEN":
            flash_button("GREEN",print(""))
        elif sequence[y] == "BLUE":
            flash_button("BLUE",print(""))
        elif sequence[y] == "YELLOW":
            flash_button("YELLOW",print(""))

def flash_button(colour, callback):
    button_map = {
        "RED": rbutton,
        "GREEN": gbutton,
        "BLUE": bbutton,
        "YELLOW": ybutton
    }

    normal = {
        "RED": "red",
        "GREEN": "green",
        "BLUE": "blue",
        "YELLOW": "yellow"
    }

    flash = {
        "RED": "orangered",
        "GREEN": "springgreen2",
        "BLUE": "deepskyblue",
        "YELLOW": "orange2"
    }

    btn = button_map[colour]

    # Step 1: flash bright colour
    btn.config(bg=flash[colour])
    root.after(300, lambda: (
        btn.config(bg=normal[colour]),
        root.after(200, callback)
    ))

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

    # Creating a button with specified options
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
