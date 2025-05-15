MAXWIDTH = 100
MAXSIZE = 1000

undo = [""] * MAXWIDTH
redo = [""] * MAXWIDTH
curr = ""
undotop = -1
redotop = -1

def pushundo(str_val):
    global undotop
    if undotop < MAXWIDTH - 1:
        undotop += 1
        undo[undotop] = str_val[:MAXSIZE-1]  

def pushredo(str_val):
    global redotop
    if redotop < MAXWIDTH - 1:
        redotop += 1
        redo[redotop] = str_val[:MAXSIZE-1]  

def clearredo():
    global redotop
    redotop = -1

def main():
    global curr, undotop, redotop
    curr = ""
    pushundo(curr)

    while True:
        print("\n--- Menu ---")
        print("1. Append text")
        print("2. Undo")
        print("3. Redo")
        print("4. Quit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            text = input("Enter text to append: ")
            curr = (curr + text)[:MAXSIZE-1]  
            pushundo(curr)
            clearredo()
            print("Current string:", curr)
        
        elif choice == 2:
            if undotop > 0:
                pushredo(curr)
                undotop -= 1
                curr = undo[undotop]
                print("Undo successful. Current string:", curr)
            else:
                print("Nothing to undo.")
        
        elif choice == 3:
            if redotop >= 0:
                pushundo(curr)
                curr = redo[redotop]
                redotop -= 1
                print("Redo successful. Current string:", curr)
            else:
                print("Nothing to redo.")
        
        elif choice == 4:
            print("Byee byee!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()