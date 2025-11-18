import tkinter as tk
import time
userSequence=[]
def button_clicked(buttonColour):
    userSequence.append(buttonColour)

root = tk.Tk()

# Creating a button with specified options
rbutton = tk.Button(root, 
                   text="", 
                   command=lambda:button_clicked("RED"),
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
                   command=lambda:button_clicked("GREEN"),
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
                   command=lambda:button_clicked("BLUE"),
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
                   command=lambda:button_clicked("YELLOW"),
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

root.mainloop()
print(userSequence)
