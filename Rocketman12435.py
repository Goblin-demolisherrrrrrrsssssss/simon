import random
colours = ["GREEN","BLUE","RED","YELLOW"]
sequence = []
repeat = True
while repeat:
    displaycolour = random.choice(colours)
    sequence.append(displaycolour)
    print(*sequence,sep = ",")
    for x in range(len(sequence)):
        colourinput = input("Colour input:")
        if colourinput.upper() != sequence:
            print("Oops! Wrong colour!")
            repeat = False
