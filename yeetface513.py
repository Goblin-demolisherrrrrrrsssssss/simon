import hashlib

def userAdder():
    fileAdder = open("test.txt", "a")
    newName = str(input("enter your new username: "))
    hashedNewName = hashlib.sha256(newName.encode(encoding="utf-8")).hexdigest()
    newPass = str(input("enter your new password: "))
    hashedNewPass = hashlib.sha256(newPass.encode(encoding="utf-8")).hexdigest()
    fileAdder.write(hashedNewName+"\n"+hashedNewPass+"\n")
    fileAdder.close()
newUser = input("do you want to register a new user? (y/n): ")
if newUser == "y":
    userAdder()
email = input("please enter your email here: ")
name = input("please enter your name here: ")
hash1 = hashlib.sha256((name.encode(encoding="utf-8"))).hexdigest()
password = input("please enter your password here: ")
hash2 = hashlib.sha256(password.encode(encoding="utf-8")).hexdigest()
file = open("test.txt", "r")
fileContents = file.read()
file.close()
splitFileContents = fileContents.splitlines()
x = int(0)
userVerified = False
passVerified = False
while x<int(len(splitFileContents)):
    if hash1 == splitFileContents[x]:
        userVerified = True
    elif hash2 == splitFileContents[x]:
        passVerified = True
    x = x + 1
if userVerified == True and passVerified == True:
    print("user has logged in")
else:
    print("user has entered something wrong...")
    sys.exit()
