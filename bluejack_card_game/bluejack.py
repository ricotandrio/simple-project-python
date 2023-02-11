from cryptography.fernet import Fernet
import os
import random

# storage for registered account
database = []
totalIndex = 0

# make global variable is accessible for all function
currName = ""
currPass = ""
currPoint = 0
oldPoint = 0
foundIndex = 0

def getOption():
    os.system("cls")
    print(" ========================")
    print(" || BlueJack Card Game ||")
    print(" ========================")
    print("\n 1. Login")
    print(" 2. Register")
    print(" 3. Exit")
    try:
        inputData = int(input(" Choose[1-3] >> "))
        if not 1 <= inputData <= 3:
            raise ValueError
    except ValueError:
        print('')
    return inputData

def checkPassword(name, password):
    global database
    global totalIndex
    global foundIndex
    fullLine = name + "#" + password

    for i in range (0, totalIndex):
        namew, passw, pointw = database[i].split("#")
        checkerLine = namew + "#" + passw
        if checkerLine == fullLine:
            foundIndex = i
            return True
    return False

def login():
    os.system("cls")
    validate = False
    while validate == False:
        name = input(" Input username : ")
        password = input(" Input password : ")
        validate = checkPassword(name, password)
        if validate == False:
            print(" [!] Account is not exist or password incorrect")
    
    if validate == True:
        print(" [*] Successfully logged in")
    
    input(" Press ENTER to continue ...")
    global foundIndex
    namew, passw, pointw = database[foundIndex].split("#")
    
    global currName 
    global currPass
    global currPoint 
    global oldPoint
    currName = namew
    currPass = passw
    currPoint = int(pointw)
    oldPoint = int(pointw)
    mainMenuGame()

def checkName(username):
    global database
    global totalIndex
    for i in range (0, totalIndex):
        name, passw, point = database[i].split("#")
        if name == username:
            return True
    return False

def regist():
    os.system("cls")
    username = "p"
    exist = True
    while not 4 <= len(username) <= 10 or exist == True:
        username = input(" Input username : ")
        if not 4 <= len(username) <= 10:
            print(" [!] Username must be between 4 and 10 characters")
        exist = checkName(username)
        if exist == True:
            print(" [!] Username already exist")
    
    password = "p"
    checkNum = False
    while not 8 <= len(password) <= 16 or checkNum == False:
        password = input(" Input password : ")
        if not 8 <= len(password) <= 16:
            print(" [!] Passwod must be between 8 and 16 charaters")
        checkNum = any(char.isdigit() for char in password)
        if checkNum == False:
            print(" [!] Password must be alphanumeric")

    print(" [*] Successfully registered an account")
    input(" Press ENTER to continue...")
    fullAccount = username + "#" + password + "#100"
    global database
    global totalIndex
    totalIndex = totalIndex + 1
    database.append(fullAccount)
    writeData()

def exit():
    os.system("cls")
    print("""
    Thank you. The original program should be solved using Java
    """)

# write and read file
# decode is used to convert byte into a string
# encode is used to convert string into a byte
def writeData():
    global database
    global totalIndex
    try:
        with open("bluejack_card_game/SuperS3cr3tFile.dat", "w") as file:
            for i in range(0, totalIndex):
                encM = fernet.encrypt(database[i].encode())
                file.write(encM.decode() + "\n")
    except FileNotFoundError:
        with open("bluejack_card_game/SuperS3cr3tFile.dat", "w") as file:
            pass

def readFile():
    global database
    global totalIndex
    try:
        with open("bluejack_card_game/SuperS3cr3tFile.dat", "r") as file:
            for i in file:
                totalIndex = totalIndex + 1
                i = fernet.decrypt(i.encode()).decode()
                database.append(i.strip())
    except FileNotFoundError:
        with open("bluejack_card_game/SuperS3cr3tFile.dat", "w") as file:
            pass

def mainMenuGame():
    global currPoint
    global currName
    global currPass
    inputData = -1
    while inputData != 3:
        os.system("cls")
        print(" Welcome,", currName)
        print(" point :", currPoint)
        print(" 1. Play")
        print(" 2. Highscore")
        print(" 3. Save & Logout")
        try:
            inputData = int(input(" Choose[1-3] >> "))
            if not 1 <= inputData <= 3:
                raise ValueError
        except ValueError:
            print('')
        if inputData == 1:
            play()
        elif inputData == 2:
            highscore()
        else:
            save()

def getCardValue(card):
    if card > 10:
        if 11 <= card <= 13:
            return 10
        elif card == 14:
            return 1
    else:
        return card

def play():
    global currPoint
    global currName
    global currPass
    try:
        bet = int(input(" Input your bet [max 100]: "))
        if not 1 <= bet <= 100:
            raise ValueError(" [!] Input must be between 1 and 100")
    except ValueError as e:
        print(e)
    
    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(card)
    currIndex = 0
    dealer = 0
    dealerCard = []
    player = 0
    playerCard = []
    match = 0
    while dealer <= 21 and player <= 21 and match < 4:
        os.system("cls")
        print(" Dealer Card : \n ")
        temp = 0
        for i in dealerCard:
            if temp == 0:
                if i == "11":
                    print("J", end = ' | ??')
                elif i == "12":
                    print("Q", end = ' | ??')
                elif i == "13":
                    print("K", end = ' | ??')
                elif i == "14":
                    print("A", end = ' | ??')
                else:
                    print(i, end = ' | ??')
            else:
                break
            temp = temp + 1
        print("\n\n Player Card : \n ")
        for i in playerCard:
            if i == "11":
                print("J", end = ' | ')
            elif i == "12":
                print("Q", end = ' | ')
            elif i == "13":
                print("K", end = ' | ')
            elif i == "14":
                print("A", end = ' | ')
            else:
                print(i, end = ' | ')
        valueCard = getCardValue(card[currIndex])
        dealer += valueCard
        dealerCard.append(str(card[currIndex]))
        valueCard = getCardValue(card[currIndex + 1])
        player += valueCard
        playerCard.append(str(card[currIndex + 1]))
        currIndex += 2
        print("\n\n Choose your move:")
        print(" 1. Hit")
        print(" 2. Stand")
        try:
            choose = int(input(" Choose[1 - 2] >> "))
            if not 1 <= choose <= 2:
                raise ValueError
        except ValueError:
            print(end = '')
        if choose == 2:
            break
        match = match + 1

    print("\n")
    os.system("cls")
    print(" Dealer Card : \n ")
    for i in dealerCard:
        if i == "11":
            print("J", end = ' | ')
        elif i == "12":
            print("Q", end = ' | ')
        elif i == "13":
            print("K", end = ' | ')
        elif i == "14":
            print("A", end = ' | ')
        else:
            print(i, end = ' | ')
    print("\n\n Player Card : \n ")
    for i in playerCard:
        if i == "11":
            print("J", end = ' | ')
        elif i == "12":
            print("Q", end = ' | ')
        elif i == "13":
            print("K", end = ' | ')
        elif i == "14":
            print("A", end = ' | ')
        else:
            print(i, end = ' | ')
    print("\n")
    if (dealer > 21 and player > 21) or (player == dealer):
        print(" [!] It's tie, you got nothing")
    elif (dealer > 21) or (player > dealer):
        print(" [!] The dealer busted, you won", bet, "point(s)")
        currPoint = currPoint + bet
    elif (player > 21) or (player < dealer):
        print(" [!]", currName, "Busted, You lost", bet, "point(s)")
        currPoint = currPoint - bet
        
    input(" Press ENTER to continue...")

def highscore():
    os.system("cls")
    print(" ===============")
    print(" || Highscore ||")
    print(" ===============")
    global database
    global totalIndex
    newList = []
    # split data that stored inside list
    for i in range (0, totalIndex):
        n, ps, sc = database[i].split("#")
        newList.append([n, ps, int(sc)])
    
    # sort list by point
    newList_sortbyPoint = sorted(newList, key = lambda a: a[2], reverse=True)
    print("\n Name       | Score")
    for nme, ps, scr in newList_sortbyPoint:
        print(" {:<10} | {:<10}".format(nme, scr))

    input("\n Press ENTER to continue...")

def save():
    find = currName + "#" + currPass + "#" + str(oldPoint)
    removeIndex = database.index(find)
    database.pop(removeIndex)
    find = currName + "#" + currPass + "#" + str(currPoint)
    database.append(find)
    writeData()
    os.system("cls")
    print(" [!] Saved successfully")
    input(" Press ENTER to continue...")
    
def main():
    readFile()
    while True:
        check = getOption()
        if check == 1:
            login()
        elif check == 2:
            regist()
        else:
            exit()
        if check == 3:
            break

# encrypt and decrypt
# create one key that used to encrypt all registered account
# key will stored in token.dat
try:
    with open("bluejack_card_game/token.dat", "r") as file:
        key = file.readline()
        if not key:
            raise FileNotFoundError
except FileNotFoundError:
    with open("bluejack_card_game/token.dat", "wb") as file:
        key = Fernet.generate_key()
        file.write(key)
        file.close()
file.close()

fernet = Fernet(key)
main()
