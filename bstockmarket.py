import random
import time

#global variable
data = []
indexP = 0

def insert():
    # insert stock name, generate stock code, validate stock type, and insert stock price
    clear()
    random.seed(time.time())
    length = 1
    while length < 6:
        name = input("    input the stock name[>= 6 characters]: ")
        length = len(name)

    price = 1
    while price < 700:
        try:
            price = int(input("    input the stock price[>= 700]: "))
        except  ValueError:
            print(end = '')

    print("    success added new stock named {} with stock code ".format(name), end = '')
    stockCode = ""
    for i in range (0, 6):
        rnd = random.randint(0, length - 1)
        char = name[rnd]
        if(char >= 'a' and char <= 'z'):
            char = char.upper()
        stockCode = stockCode + char
        print(char, end = '')
    x = random.randint(100, 300)
    print(x)
    stockCode = stockCode + str(x)
    print("    press enter to continue...")
    input("    >> ")    

    index = price * ((int(random.random() * 1000) % 100) + 1)
    while(index > 8562):
        index = (price / ((((int)(random.random() * 1000) % 37) + 1) * 2)) * (((int)(random.random() * 1000) % 100) + 1)
    
    global indexP
    global data
    if 5708 <= index <= 8562:
        data.append([name, stockCode, "blue chip", price])
    elif 2854 <= index <= 5707:
        data.append([name, stockCode, "middle chip", price])
    else:
        data.append([name, stockCode, "small cap", price])        
    indexP = indexP + 1

def viewall():
    # display all stocks that have been added
    clear()
    global indexP
    global data
    if indexP == 0:
        print("    there are no stocks, consider to add one")
    else:
        idxComposite = 0
        print("    no | stock name | stock code | stock label | price")
        for i in range (0, indexP):
            idxComposite = idxComposite + int(data[i][3])
            print("    {}  | {:<10} | {:<10} | {:<10} | {:<10}".format(i+1, data[i][0], data[i][1], data[i][2], data[i][3]))
        print("")
        print(idxComposite)
        print(idxComposite/3)
        idxComposite = ((idxComposite/indexP) * 3) / 2
        print("    idx composite :", idxComposite)

    input("    press enter to continue...")

def delete():
    # delete or remove specific stock that has been added
    clear()
    global indexP
    global data
    if indexP == 0:
        print("    there are no stocks, consider to add one")
    else:
        codeToDelete = "-1"
        while codeToDelete != "back":
            clear()
            if indexP == 0:
                print("    there are no stocks, consider to add one")
                break
            print("    no | stock name | stock code | stock label | price")
            for i in range (0, indexP):
                print("    {}  | {:<10} | {:<10} | {:<10} | {:<10}".format(i+1, data[i][0], data[i][1], data[i][2], float(data[i][3])))
            codeToDelete = str(input("    input the stock code [<= 9 characters][case insensitive][type 'back' to abort the deletion]: "))
            if codeToDelete == "back":
                print("    deletion progess is aborted!")
                break
            else:
                found = 0
                for j in range (0, indexP):
                    if data[j][1] == codeToDelete or data[j][1] == codeToDelete.upper():
                        del data[j]
                        print("    success delete", codeToDelete)
                        indexP = indexP - 1
                        found = 1
                        break
                if found == 0:
                    print("    there are no stock with code", codeToDelete, ",deletion progress is aborted!")
                    input("    press enter to continue...")
            clear()
    input("    press enter to continue...")

def clear():
    # insert a gap between each iteration of a loop
    for i in range (10):
        print("")

def mainMenu():
    # main menu
    clear()
    global indexP
    print("")
    print("    BStockMarket    ", indexP)
    print("""
    1. insert stock
    2. view all stock
    3. delete stock
    4. exit program
    """, end = '')
    x = 1
    while True:
        try: 
            x = int(input(">> "))
            if 1 <= x <= 4:
                return x
            else:
                print("    [!] Input is between 1 - 4")
        except ValueError:
            print("    [!] Invalid input is not integer")

def exit():
    # credit
    clear()
    print("""
    Thanks for using the app
    """)
    
def main():
    while True:
        clear()
        check = mainMenu()
        if(check == 1):
            insert()
        elif(check == 2):
            viewall()
        elif(check == 3):
            delete()
        else:
            exit()
        if(check == 4):
            break

main()