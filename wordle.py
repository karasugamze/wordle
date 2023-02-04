import sys

print("""WELCOME TO THE WORDLE GAME
GUESS THE WORDS OF THE DAY!!
YOU HAVE THE RIGHT TO GUESS FİVE WORDS..""")

WoD = sys.argv[1]         #word of the day
counter=0

while counter<6:
    Try = input("Try:" )       #guess
    #the length of the guessed word is checked
    while len(Try)>5:
        print("The length of word must be five")
        counter+=1
        Try = input("Try:")
    while len(Try) < 5:
        print("The length of word must be five")
        counter += 1
        Try = input("Try")
    while len(Try)==5:
        #The letters of the guessed word are compared with the letters of the word of the day.
        if Try!=WoD:
            for i in range(0,4):
                if Try[i] == WoD[i]:
                    print(i + 1, ". letter exist and located in right position.")
                elif Try[i] != WoD[i] and Try[i] == WoD[1] or Try[i] == WoD[2] or Try[i] == WoD[3]:
                    print(i + 1, ". letter exist but located in wrong position.")
                elif Try[i] != WoD[i] and Try[i] == WoD[4]:
                    print(i + 1, ".letter exist but located in wrong position.")
                else:
                    print(i + 1, ". letter does not exist.")
            counter+=1
            break
        else:
            print("Congratulations! You guess right !")
        break
    break
