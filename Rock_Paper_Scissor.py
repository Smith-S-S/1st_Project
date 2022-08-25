import random
com_sc=0
player_sc=0

while True:
    player = input("select: ")
    print(player)
    com = ["r", "p", "s"]

    x= random.choice(com)

    if player==x:
        print ("draw")

    if player=="r" and x=="p":
        print("com win")
        com_sc += 1

    if player=="r" and x=="s":
        print("player win")
        player_sc += 1

    if player == "p" and x == "s":
        print("com win")
        com_sc += 1

    if player == "p" and x == "r":
        print("player win")
        player_sc += 1

    if player == "s" and x == "r":
        print("com win")
        com_sc += 1

    if player == "s" and x == "p":
        print("player win")
        player_sc += 1

    print("yes or no")
    ch=input("type: ")

    if ch=="no":
        break


    print ("computer choose: ",x)
print ("score: ",com_sc)
print("score: ", player_sc)

"""for i in range(0,11):
    print (i,"=3=",i%3)
    print (i,"=4=",i%4)"""