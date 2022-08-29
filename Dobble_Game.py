import random

# basic
def dg():

    n=["a","c","g","h","k"]
    g=["a","x","y","z","q"]
    x= str(input(":"))
    if x in n and g:
        print("lu")
    else:
        print("pooo")

#  Dobblr_game

import string
sympols=[]
# here we for an lis from a-z and A-Z
sympols= list(string.ascii_letters)
print ("from a-z and A-Z", sympols)

# here we use create the 2 cards with the length of 5

card1=[0]*5
card2=[0]*5
print ("card1: ",card1)
print ("card2: ",card2)


# here we create the 2 position
# because in the 2 cards 1 position want to same
pos1=random.randint(0,4)
pos2=random.randint(0,4)

print("pos1:",pos1)
print("pos2:",pos2)


# we create the "same_sympols" to save that same letter

same_sympols= random.choice(sympols)
sympols.remove(same_sympols)
print("same_sympols: ",same_sympols)

# checking if the pos1 is equal to pos2 because in some existence only it may same
if (pos1==pos2):
    card1[pos1]=same_sympols
    card2[pos1]=same_sympols
else:
    card1[pos1] = same_sympols
    card2[pos2] = same_sympols
    print(card1[pos1])
    print(card2[pos2])

    # this is for
    # card1[pos2])
    # (card2[pos1])

# if we not use this means the following "while" condition is comes to neglate,
    # if pos1=1 pos2=0
    # that we say that if i== pos neglate, so  pos1=1 pos2=0  got value
    # But  pos1=0 and pos2=1 n0 get value
    card1[pos2] = random.choice(sympols)
    sympols.remove(card1[pos2])
    card2[pos1] = random.choice(sympols)
    sympols.remove(card2[pos1])
    print(card1[pos2])
    print(card2[pos1])


# ya here in
i=0
while (i<5):
    if (i!= pos1 and i!= pos2):
        al1=random.choice(sympols)
        sympols.remove(al1)
        al2 = random.choice(sympols)
        sympols.remove(al2)
        card1[i]=al1
        card2[i] = al2
        print("i:",i)
    i +=1

print(card1)
print(card2)
n = input("Please Type the common letter: ")
if n in card1 and card2:
    print ("Right da!")
else:
    print("Sorry Thanmbi")






