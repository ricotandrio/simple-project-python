import random

def main():
    option = ["rock", "paper", "scissors"]
    while True:
        print("""
        1. rock 
        2. paper
        3. scissors
        """)
        bot = random.choice(option)
        try:
            user = int(input("    Choice [1 - 3]: "))
            if user < 1 or user > 3:
                raise ValueError("    Invalid input. Please enter a number from 1 - 3")
        except ValueError as e:
            print(e)
            input("    press enter to continue...")
            continue
        print("    Computer:", bot)
        print("    User:", option[user-1])
        if bot == "rock":
            if user == 1:
                print("    TIE")
            elif user == 2:
                print("   USER WIN")
            else:
                print("    BOT WIN")
        elif bot == "paper":
            if user == 1:
                print("    BOT WIN")
            elif user == 2:
                print("   TIE")
            else:
                print("    USER WIN")
        else:
            if user == 1:
                print("    USER WIN")
            elif user == 2:
                print("   BOT WIN")
            else:
                print("    TIE")
        input("    press enter to continue...")
main()
