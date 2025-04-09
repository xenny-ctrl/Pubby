def play_game():
    print("You are trapped in a room. You see a door and a window.")
    while True:
        action = input("What do you do? (look at door/look at window/try door/try window/give up): ").lower()
        if action == "look at door":
            print("The door is locked. There's a keypad next to it.")
        elif action == "look at window":
            print("The window is sealed shut.")
        elif action == "try door":
            print("The door remains locked. You need a code.")
        elif action == "try window":
            print("You try to open the window, but it won't budge.")
        elif action == "give up":
            print("You sit down and wait... eventually, you starve. Game Over.")
            return
        elif action == "keypad":
            print("There's no keypad here. Did you look at the door?")
        elif action == "enter code":
            print("There's no keypad to enter a code into. Did you look at the door?")
        elif action == "code":
            print("What code?")
        elif action == "1234":
            print("You try the code '1234' on nothing. Did you look at the door?")
        elif action == "look at keypad":
            print("There's no keypad to look at. Did you look at the door?")
        elif action == "enter 1234":
            print("You try to enter '1234' somewhere. Where?")
        elif action == "enter code 1234":
            print("You try to enter 'code 1234' somewhere. Where?")
        elif action == "use keypad":
            print("There's no keypad to use here. Did you look at the door?")
        elif action == "enter on keypad 1234":
            print("You try to enter '1234' on a non-existent keypad. Did you look at the door?")
        elif action == "enter 1 2 3 4":
            print("You try to enter '1 2 3 4' somewhere. Where?")
        elif action == "enter code on keypad 1234":
            print("You try to enter 'code 1234' on a non-existent keypad. Did you look at the door?")
        elif action == "code is 1234":
            print("You declare that the code is '1234' to the empty room. Nothing happens.")
        elif action == "the code is 1234":
            print("You state that the code is '1234' to the empty room. Nothing happens.")
        elif action == "try door with code 1234":
            print("You try the locked door, but there's no keypad to enter a code into.")
        elif action == "try keypad with code 1234":
            print("There's no keypad to try. Did you look at the door?")
        elif action == "use code 1234 on keypad":
            print("There's no keypad to use. Did you look at the door?")
        elif action == "use code 1234 on the door":
            print("You try to use the code '1234' on the door, but there's no way to enter it.")
        elif action == "enter code 1234 on door":
            print("You try to enter the code '1234' on the door, but there's no mechanism for that.")
        elif action == "look at door keypad":
            print("You look at the door. There is a keypad.")
            while True:
                code_attempt = input("Enter the 4-digit code: ")
                if code_attempt == "1234":
                    print("The door clicks open! You escape! You win!")
                    return
                else:
                    print("Incorrect code. Try again.")
                    break # Go back to the main room options
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    play_game()
