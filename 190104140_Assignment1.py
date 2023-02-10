# Python code for finding brother/sister/uncle/aunt of a person in a given KB of kinship domain
 
import os
ParentKB =  [('parent', 'Hasib', 'Rakib'),
        ('parent', 'Rakib', 'Sohel'),
        ('parent', 'Rakib', 'Rebeka'),
        ('parent', 'Rashid', 'Hasib'),
        ('parent', 'Rakib', 'Asif'),
        ('parent', 'Rakib', 'Saber'),
        ('parent', 'Rabeya', 'Asif'),
        ('parent', 'Rabeya', 'Sohel'),
        ('parent', 'Hasib', 'Rakhi'),
        ('parent', 'Samir', 'Rabeya'),
        ('parent', 'Samir', 'Akib'),
        ('parent', 'Samir', 'Tanny')]

MaleKB = ['Hasib', 'Rakib', 'Sohel', 'Rashid', 'Ashiq', 'Asif', 'Samir', 'Akib', 'Saber']
FemaleKB = ['Rebeka', 'Rabeya', 'Rakhi', 'Tanny']

        
def findSibling(relation, name):
    parents = []
    siblings = []

    for i in range(len(ParentKB)):
        if (ParentKB[i][2] == name):
            parents.append(ParentKB[i][1])

    for i in range(len(parents)):
        for j in range(len(ParentKB)):
            if(parents[i] == ParentKB[j][1] and ParentKB[j][2] != name ):
                if(relation == "Brother" and ParentKB[j][2] in MaleKB and ParentKB[j][2] not in siblings ):
                    siblings.append(ParentKB[j][2])
                elif(relation == "Sister" and ParentKB[j][2] in FemaleKB and ParentKB[j][2] not in siblings):
                    siblings.append(ParentKB[j][2])
    if(len(siblings) != 0):
        print(*siblings , end= " ;", sep = ", ")


def findRelative(relation, name):
    parents = []

    for i in range(len(ParentKB)):
        if (ParentKB[i][2] == name):
            parents.append(ParentKB[i][1])

    for i in range(len(parents)):
        if(relation == "Uncle"):
            findSibling("Brother", parents[i])
        elif(relation == "Aunt"):
            findSibling("Sister", parents[i])

while(True):
    os.system('cls')
    print("1.Find Brother \n2.Find Sister \n3.Find Uncle \n4.Find Aunt \n")
    userInput = int(input("Input: "))
    X = input("Name : ")

    if(userInput == 1): 
        print("Brother/s of {0} : ".format(X), end=' ')
        findSibling("Brother", X)
    elif(userInput == 2):
        print("Sister/s of {0} : ".format(X), end=' ') 
        findSibling("Sister", X)
    elif(userInput == 3):
        print("Uncle/s of {0} : ".format(X), end=' ') 
        findRelative("Uncle", X)
    elif(userInput == 4):
        print("Aunt/s of {0} : ".format(X), end=' ') 
        findRelative("Aunt", X) 

    input("\nPress a key to continue..")        
                    