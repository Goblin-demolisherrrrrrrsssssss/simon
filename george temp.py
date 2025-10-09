def useradder():
    griddygriddy = open("test.txt", "a")
    user = str(input("enter your new username: "))
    hasheduser = hashlib.sha256(user.encode(encoding="utf-8")).hexdigest()
    beanchilling = str(input("enter your new password: "))
    hashedpass = hashlib.sha256(beanchilling.encode(encoding="utf-8")).hexdigest()
    griddygriddy.write(hasheduser+"\n"+hashedpass+"\n")
    griddygriddy.close()
newuser = input("do you want to register a new user? (y/n): ")
if newuser == "y":
    useradder()
othernewuser = input("do you want to register another new user? (y/n): ")
if othernewuser == "y":
    useradder()
email1 = input("player 1 please enter your email here: ")
name1 = input("player 1 please enter your name here: ")
hash1 = hashlib.sha256((name1.encode(encoding="utf-8"))).hexdigest()
password1 = input("player 1 please enter your password here: ")
hash2 = hashlib.sha256(password1.encode(encoding="utf-8")).hexdigest()
email2 = input("player 2 please enter your email here: ")
name2 = input("player 2 please enter your name here: ")
hash3 = hashlib.sha256(name2.encode(encoding="utf-8")).hexdigest()
password2 = input("player 2 please enter your password here: ")
hash4 = hashlib.sha256(password2.encode(encoding="utf-8")).hexdigest()
file = open("test.txt", "r")
stuff = file.read()
file.close()
rehe = stuff.splitlines()
re = int(0)
user1verified = False
pass1verified = False
user2verified = False
pass2verified = False
while re<int(len(rehe)):
    if hash1 == rehe[re]:
        user1verified = True
    elif hash2 == rehe[re]:
        pass1verified = True
    elif hash3 == rehe[re]:
        user2verified = True
    elif hash4 == rehe[re]:
        pass2verified = True
    re = re+1
if user1verified == True and pass1verified == True:
    print("user one has logged in")
else:
    print("user one has entered something wrong...")
    sys.exit()
if user2verified == True and pass2verified == True:
    print("user two has logged in")
else:
    print("user two has entered something wrong...")
    sys.exit()
