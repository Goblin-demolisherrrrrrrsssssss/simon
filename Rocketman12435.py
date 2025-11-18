import random
try:
    test = open("points.txt", "r")
    test.close()
except FileNotFoundError:
    pointFileCreator = open("points.txt", "w")
    pointFileCreator.close()
colours = ["GREEN","BLUE","RED","YELLOW"]
sequence = []
repeat = True # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
points = 0 # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
name = "" # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
while repeat: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    displaycolour = random.choice(colours) # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    sequence.append(displaycolour) # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    print(*sequence,sep = ",") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
    for x in range(len(sequence)): # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        colourinput = input("Colour input:") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        if colourinput.upper() != sequence: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            print("Oops! Wrong colour!") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            break # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
        else: # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
            points += 1 # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
print(f"Game Over! You scored {points} points!") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder = open("points.txt", "a") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder.write(f"{name}: {points}\n") # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
pointAdder.close() # imagine if ninja got a LOWWWWW taperrrr fadeeeeee
