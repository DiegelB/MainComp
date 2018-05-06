import os
import random

def main():
    mainMenu()

def mainMenu():
    print("(1). Play Game")
    print("(2). See History")
    print("(3). Login")
    print("(4). Exit\n")

    while(True):
        userInput = input(">>")

        if(userInput == "1"):
            mainLoop()
        elif(userInput == "2"):
            historyPage()
        elif(userInput == "3"):
            loginPage()
        elif(userInput == "4"):
            exit()
        else:
            print("Please choose only (1-4).")
            continue






def mainLoop():
    

    os.system("clear")
    print("\tWelcome to MADLIBS!\n")
    print("MADLIBS is a fun story generating program.", 
          "\nIt will ask you to enter nouns, simple and proper, verbs, and adjectives.\n")

    pressEnter()

    flag = True
    while(flag):
        pNouns = []
        adjs = []
        verbs = []
        nouns = []
        allWords = []

        for i in range(0,1): #0,2
            banner()
            printHistory(allWords)

            temp = input("\n--Please input proper noun " + str(i+1) + "--\n>>")
            pNouns.append(temp)
            allWords.append(temp)

        for i in range(0,1): #0,9
            banner()
            printHistory(allWords)

            temp = input("\n--Please input adjective " + str(i+1) + "--\n>>")
            adjs.append(temp)
            allWords.append(temp)

        for i in range(0,1): #0,7
            banner()
            printHistory(allWords)

            temp = input("\n--Please input verb " + str(i+1) + "--\n>>")
            verbs.append(temp)
            allWords.append(temp)

        for i in range(0,1): #0,9
            banner()
            printHistory(allWords)

            temp = input("\n--Please input simple noun " + str(i+1) + "--\n>>")
            nouns.append(temp)
            allWords.append(temp)

        flag = checkHistory(allWords)
        
    p1 = generateparagraph(pNouns,adjs,verbs,nouns)
    p2 = generatePlotPara(pNouns,adjs,verbs,nouns)
    p3 = generateConflictPara(pNouns,adjs,verbs,nouns)
    p4 = generateResoPara(pNouns,adjs,verbs,nouns)

    createdStory = str(p1) + "\n\n" + str(p2) + "\n\n" + str(p3) + "\n\n" + str(p4) + "\n\n"

    print(createdStory)


def generateparagraph(pNouns,adjs,verbs,nouns):
    # needs 3 adjs, 1 verb, and 2 nouns
    paragraph = []

    randomNumber = random.randint(1,1) # 1,4
    fileName = "/home/skelly/Scripting/MadLibs/MLStories/Intro/" + str(randomNumber) + ".txt"
    readFile = open(fileName, 'r')
    splitFile = readFile.read()
    
    for currentWord in splitFile.split():
        paragraph.append(currentWord)

    for i in range(len(paragraph)):
        if paragraph[i] == "AAA":
            paragraph[i] = random.choice(adjs)
        elif paragraph[i] == "NNN":
            paragraph[i] = random.choice(nouns)
        elif paragraph[i] == "ING":
            paragraph[i] = random.choice(verbs) + "ing"
        elif paragraph[i] == "PPP":
            paragraph[i] = pNouns[0]
    
    finalPara = " ".join(paragraph)

    return finalPara

def generatePlotPara(pNouns,adjs,verbs,nouns):
    # needs 3 adjs, 1 verb, and 2 nouns
    paragraph = []

    randomNumber = random.randint(1,1) # 1,4
    fileName = "/home/skelly/Scripting/MadLibs/MLStories/Plot/" + str(randomNumber) + ".txt"
    readFile = open(fileName, 'r')
    splitFile = readFile.read()
    
    for currentWord in splitFile.split():
        paragraph.append(currentWord)

    for i in range(len(paragraph)):
        if paragraph[i] == "AAA":
            paragraph[i] = random.choice(adjs)
        elif paragraph[i] == "NNN":
            paragraph[i] = random.choice(nouns)
        elif paragraph[i] == "ING":
            paragraph[i] = random.choice(verbs) + "ing"
        elif paragraph[i] == "PPP":
            paragraph[i] = pNouns[0]
    
    finalPara = " ".join(paragraph)

    return finalPara

def generateConflictPara(pNouns,adjs,verbs,nouns):
    # needs 3 adjs, 1 verb, and 2 nouns
    paragraph = []

    randomNumber = random.randint(1,1) # 1,4
    fileName = "/home/skelly/Scripting/MadLibs/MLStories/Conf/" + str(randomNumber) + ".txt"
    readFile = open(fileName, 'r')
    splitFile = readFile.read()
    
    for currentWord in splitFile.split():
        paragraph.append(currentWord)

    for i in range(len(paragraph)):
        if paragraph[i] == "AAA":
            paragraph[i] = random.choice(adjs)
        elif paragraph[i] == "NNN":
            paragraph[i] = random.choice(nouns)
        elif paragraph[i] == "ING":
            paragraph[i] = random.choice(verbs) + "ing"
        elif paragraph[i] == "PPP":
            paragraph[i] = pNouns[0]
    
    finalPara = " ".join(paragraph)

    return finalPara

def generateResoPara(pNouns,adjs,verbs,nouns):
    # needs 3 adjs, 1 verb, and 2 nouns
    paragraph = []

    randomNumber = random.randint(1,1) # 1,4
    fileName = "/home/skelly/Scripting/MadLibs/MLStories/Reso/" + str(randomNumber) + ".txt"
    readFile = open(fileName, 'r')
    splitFile = readFile.read()
    
    for currentWord in splitFile.split():
        paragraph.append(currentWord)

    for i in range(len(paragraph)):
        if paragraph[i] == "AAA":
            paragraph[i] = random.choice(adjs)
        elif paragraph[i] == "NNN":
            paragraph[i] = random.choice(nouns)
        elif paragraph[i] == "ING":
            paragraph[i] = random.choice(verbs) + "ing"
        elif paragraph[i] == "PPP":
            paragraph[i] = pNouns[0]
    
    finalPara = " ".join(paragraph)

    return finalPara

def checkHistory(allWords):
    banner()
    print("--History--")
    for r in allWords:
        print(r)

    while(True):
        userInput = input("Do you like your words (Y/N)?\n>>")
        if(userInput.lower() == "y"):
            return False
        elif(userInput.lower() == "n"):
            return True
        else:
            print("Please only enter (Y/N)")
            continue  
    
def banner():
    os.system("clear")
    print("~-~-~-~-~-~-~MADLIBS~-~-~-~-~-~-~\n")

def pressEnter():
    print("--Please press enter to continue---\n")
    input(">>")
    print()

def printHistory(allWords):
    print("--History--")
    for r in allWords:
        print(r)



main()