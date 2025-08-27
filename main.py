import random

def diceSelection():
    arr = [4,6,8,10,12,20,100]
    print(f'faces option {arr}')
    UserSelection = int(input("Enter the number of faces on the dice: "))
    if UserSelection not in arr:
        diceSelection()
    return UserSelection

def rolling(faces):
    draw = random.randint(1,faces+1)
    return draw

def main():
    while True:
        print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Enter the number of faces.
2. Roll the dice
3. Exit""")
        option = int(input())
        print("---------------------------------------------------------------------------")
        if option == 1:
            faces = diceSelection()
        elif option == 2:
            result = rolling(faces)
            print(result)  
        elif option == 3:
            break


if __name__ == "__main__":
    main()