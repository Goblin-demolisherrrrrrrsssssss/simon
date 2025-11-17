import tkinter as tk
userSequence=[]
def button_clicked(buttonColour):
    userSequence.append(buttonColour)

root = tk.Tk()

# Creating a button with specified options
rbutton = tk.Button(root, 
                   text="", 
                   command=button_clicked("R"),
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
                   command=button_clicked("G"),
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
                   command=button_clicked("B"),
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
                   command=button_clicked("Y"),
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

rbutton.grid(row = 0, column = 0,  pady = 2)
bbutton.grid(row = 1, column = 0,  pady = 2)
gbutton.grid(row = 0, column = 1,  pady = 2)
ybutton.grid(row = 1, column = 1,  pady = 2)


#rbutton.place(rely=1.0, relx=1.0,  anchor="se")
#gbutton.place(rely=1.0, relx=0.0,  anchor="ne")
#bbutton.place(rely=0.0, relx=1.0,  anchor="sw")
#ybutton.place(rely=0.0, relx=0.0,  anchor="ne")

#rbutton.pack(padx=20, pady=20)
#gbutton.pack(padx=20, pady=20)
#bbutton.pack(padx=20, pady=20)
#ybutton.pack(padx=20, pady=20)

root.mainloop()
