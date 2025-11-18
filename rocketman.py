import random 
try: 
    test = open("points.txt", "r") 
    test.close() 
except FileNotFoundError: 
    pointFileCreator = open("points.txt", "w") 
    pointFileCreator.close() 
colours = ["GREEN","BLUE","RED","YELLOW"] 
sequence = [] 
repeat = True
points = 0
name = ""
while repeat:
    displayColour = random.choice(colours)
    sequence.append(displayColour)
    print(*sequence,sep = ",")
    for x in range(len(sequence)):
        colourInput = input("Colour input:")
        if colourInput.upper() != sequence:
            print("Oops! Wrong colour!")
            break
        else:
            points += 1
print(f"Game Over! You scored {points} points!")
pointAdder = open("points.txt", "a")
pointAdder.write(f"{name}: {points}\n")
pointAdder.close()
