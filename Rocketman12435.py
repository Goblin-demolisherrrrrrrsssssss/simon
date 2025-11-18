import random # absolute shawarma I fixed your code
try: # absolute shawarma I fixed your code
    test = open("points.txt", "r") # absolute shawarma I fixed your code
    test.close() # absolute shawarma I fixed your code
except FileNotFoundError: # absolute shawarma I fixed your code
    pointFileCreator = open("points.txt", "w") # absolute shawarma I fixed your code
    pointFileCreator.close() # absolute shawarma I fixed your code
colours = ["GREEN","BLUE","RED","YELLOW"] # absolute shawarma I fixed your code
sequence = [] # absolute shawarma I fixed your code
repeat = True # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
points = 0 # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
name = "" # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
while repeat: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    displayColour = random.choice(colours) # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    sequence.append(displayColour) # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    print(*sequence,sep = ",") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    for x in range(len(sequence)): # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        colourInput = input("Colour input:") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        if colourInput.upper() != sequence: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            print("Oops! Wrong colour!") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            break # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        else: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            points += 1 # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
print(f"Game Over! You scored {points} points!") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder = open("points.txt", "a") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder.write(f"{name}: {points}\n") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder.close() # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
