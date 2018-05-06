import random
import subprocess
import pickle
import sys

#All of the global values that are used to store conversation data
global knownThings
global responseThings
global userInput
global globalCurrent
global globalUser
global startUpDisclaimer

#Lists of bot-known items, as well as current conversation status
knownThings = []
responseThings = []
globalCurrent = ""
globalUser = ""
startUpDisclaimer = "Xeria ChatBot Ver_pDEV.01\n" \
                    "Author *|^|MLGSkelly|^|*\n\n" \
                    "      ---About Xeria---\n" \
                    "This bot learns from user input.\n" \
                    "Currently Xeria responds at random.\n" \
                    "In time she will be able to hold \n" \
                    "everyday, normal conversations.\n" \
                    "If you need help with commands,\n" \
                    "please type 'help me Xeria'.\n"

#Used to grab an item from a list at random
secure_random = random.SystemRandom()

#This is when the application is opened. It loads the previous file and prompts the user to talk.
def startProgram():
    global userInput
    global globalUser
    global knownThings
    file = open("chatbot.txt", 'rb')
    knownThings = pickle.load(file)
    file.close()
    print(startUpDisclaimer)
    print("Xeria: Hello, my name is Xeria. How are you?")
    userInput = raw_input("User: ")
    globalUser = userInput
    if "goodbye Xeria" in globalUser:
        print("Xeria: Goodbye user")
        raw_input("Press any key to close application")
        exit()
    elif "help me Xeria" in globalUser:
        keyWordHelp()
    else:
        saveInput()

#This main loop of the program that jumps back and forth to save the data
def mainLoop():
    global userInput
    global globalUser
    botSpeak()
    print ("Xeria: " + globalCurrent)
    userInput = raw_input("User: ")
    globalUser = userInput
    if "goodbye Xeria" in globalUser:
        print("Xeria: Goodbye user")
        raw_input("Press any key to close application\n")
        exit()
    elif "help me Xeria" in globalUser:
        keyWordHelp()
    else:
        saveInput()

#Used to save user input and at it to the known things for the bot
def saveInput():
    knownThings.append(userInput)
    saveBot()
    mainLoop()

#The logical operators of the bot so it doesnt seem as dumb
def botSpeak():
    global globalCurrent
    global globalUser
    current = secure_random.choice(knownThings)
    if current == globalCurrent:
        botSpeak()
    else:
        globalCurrent = current



def nameScript():
    global globalCurrent
    global globalUser
    nameScript = ['My name is Xeria, what is yours?', 'Xeria, how are you?', 'They programmed me to say Xeria. What did '
                                                                             'they program you to say?',
                  'Hello I am Xeria, its nice to meet you!']
    if "?" in globalUser:
        print("Poop")
        #globalCurrent = secure_random.choice(nameScript)
    else:
        current = secure_random.choice(knownThings)
        if current == globalCurrent:
            botSpeak()
        else:
            globalCurrent = current

#list of key words to use Xeria
def keyWordHelp():
    print("           --Keywords--\n"
          "'help me Xeria' -- Opens this menu\n"
          "'goodbye Xeria' -- Closes program\n"
          "    **capitalization matters**\n")
    raw_input("Press any key to return to Xeria\n")
    mainLoop()

#Saves the bots data
def saveBot():
    global file
    global knownThings
    global test
    file = open("chatbot.txt", 'wb')
    pickle.dump(knownThings, file)
    file.close()

#Starts the program when the application is opened.
startProgram()