import sys

WoD=sys.argv[0]

counter=0
while counter<5:
    Try = input("Try:" )
    while len(Try)>5:
        print("The length of word must be five")
        counter+=1
        Try = input("Try:")
    while len(Try) < 5:
        print("The length of word must be five")
        counter += 1
        Try = input("Try:")
    while len(Try)==5:
        if Try==WoD:
            print("Congratulations! You guess right !")
            break
        else:
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
