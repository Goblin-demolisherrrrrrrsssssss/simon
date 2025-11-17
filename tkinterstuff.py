import tkinter as tk
userSequence=[]
def button_clicked(buttonColour):
    userSequence.append(buttonColour)

root = tk.Tk()

# Creating a button with specified options
redButton = tk.Button(root, 
                   text="", 
                   command=button_clicked("R"),
                   activebackground="white", 
                   activeforeground="black",
                   anchor="center",
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
greenButton = tk.Button(root, 
                   text="", 
                   command=button_clicked("G"),
                   activebackground="white", 
                   activeforeground="black",
                   anchor="center",
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
blueButton = tk.Button(root, 
                   text="", 
                   command=button_clicked("B"),
                   activebackground="white", 
                   activeforeground="black",
                   anchor="center",
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
yellowButton = tk.Button(root, 
                   text="", 
                   command=button_clicked("Y"),
                   activebackground="white", 
                   activeforeground="black",
                   anchor="center",
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

redButton.pack(padx=20, pady=20)
greenButton.pack(padx=20, pady=20)
blueButton.pack(padx=20, pady=20)
yellowButton.pack(padx=20, pady=20)

root.mainloop()

