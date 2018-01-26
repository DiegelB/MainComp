import random
import subprocess
import pickle
import datetime


#All of the global values that are used to store conversation data
global knownThings

#Lists of bot-known items, as well as current conversation status
knownThings = []
#The last thing the bot said (used so the bot wont say the same thing twice)
globalCurrent = ['']
#The last user response
globalUser = []
#the name of the user
userName = []

startUpDisclaimer = "Xeria ChatBot Ver_pDEV.02\n" \
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
def startProgram(startUpDisclaimer):
    global knownThings
    file = open("chatbot.txt", 'rb')
    knownThings = pickle.load(file)
    file.close()
    print(startUpDisclaimer)
    print("Xeria: Hello User, my name is Xeria. How are you?")
    mainLoop()

#This main loop of the program that jumps back and forth to save the data
def mainLoop():
    userInput = raw_input("User: ")
    keyWordChecker(userInput)

#checks for key words in user input
def keyWordChecker(userInput):
    if userInput == "help me Xeria":
        keyWordHelp()
    elif userInput == "goodbye Xeria":
        goodByeUser()
    elif "your name"in userInput:
        myNameScript(userName)
    elif "my purpose?" in userInput or "What is my purpose?" in userInput:
        myPurpose()
    elif "open a program Xeria" in userInput:
        openProgram()
    elif "what" in userInput and "the time" in userInput:
        timeScript()
    else:
        botSpeak(globalCurrent)
        saveInput(userInput)

#SCRIPTS-------------------------------------------------------------------------------------SCRIPTS
#list of key words to use Xeria
def keyWordHelp():
    print("\n"+"           --Keywords--\n"
          "'help me Xeria' -- Opens this menu\n"
          "'goodbye Xeria' -- Closes program\n"
          "'open a program Xeria' -- Starts a program\n"
          "    **capitalization matters**\n")
    raw_input("Press enter to return to Xeria\n")
    mainLoop()

#When Xerias name is asked
def myNameScript(userName):
    nameLibrary = ['My name is Xeria. What is yours?', 'Xeria, whats yours?', 'Hello, I am '
                                                                              'Xeria, whats your name?',
                   'Xeria, whos askin?']
    print('Xeria: '+secure_random.choice(nameLibrary))
    userName.append(raw_input("User: "))
    print("Xeria: Hello " + str(userName[0]))
    mainLoop()

#Opens various programs from users files
def openProgram():
    userResponse = raw_input("Xeria: What program would you like to open? Reply with"
                             "'Chrome', 'Steam', or 'PyCharm'!\nUser: ")
    if "Chrome" in userResponse or "chrome" in userResponse:
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
        botSpeak(globalCurrent)
        mainLoop()
    elif "Steam" in userResponse or "steam" in userResponse:
        subprocess.Popen([r"C:\Program Files (x86)\Steam\Steam.exe"])
        botSpeak(globalCurrent)
        mainLoop()
    elif "PyCharm" in userResponse or "pycharm" in userResponse:
        subprocess.Popen([r"C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.3\bin\pycharm64.exe"])
        botSpeak(globalCurrent)
        mainLoop()
    else:
        print("Xeria: I'm sorry, you did not input a valid resonse. Please press enter to return"
              "talking to me!\n")
        raw_input()
        mainLoop()

#The bot tells the user the current time. IN 24 HOUR TIME, NEED TO MAKE IT 12 HOUR TIME
def timeScript():
    time = datetime.datetime.now()
    print("Xeria: The current time is - " + str(time.hour) + ":" + str(time.minute))
    mainLoop()

#This randomizes a script to choose from so Xeria can engage the user
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def randomScript():
    randomScriptNum = random.randint(1,1)
    if randomScriptNum == 1:
        howWasDay()

def howWasDay():
    botResponse = ['How was your day', 'How has your day been?', 'What have you been up to today?']
    print("Xeria: " + secure_random.choice(botResponse))
    userResponse = raw_input("User: ")
    print("Xeria: That's wonderful!")
    saveInput(userResponse)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#rick and morty easter egg
def myPurpose():
    print("Xeria: You pass the butter.")
    mainLoop()

#Function to exit Xeria
def goodByeUser():
    print("Xeria: Goodbye User...")
    raw_input("Press enter to exit Xeria\n")
    exit()
#SCRIPTS-------------------------------------------------------------------------------------SCRIPTS

#Used to save user input and at it to the known things for the bot
def saveInput(userInput):
    global knownThings
    knownThings.append(userInput)
    saveBot()
    mainLoop()

#The logical operators of the bot so it doesnt seem as dumb
def botSpeak(globalCurrent):
    global knownThings
    current = secure_random.choice(knownThings)
    #This adds a more engaging reponses for the bot. it has a 10% chance to run a random pre-defined
    #script-tree.
    chanceForScript = random.randint(1,10)
    if chanceForScript == 1:
        randomScript()
    else:
        # this if statment stops Xeria from repeating the same thing twice in a row
        if current == globalCurrent[0]:
            botSpeak(globalCurrent)
        else:
            print("Xeria: " + current)
            globalCurrent[0] = current

#Saves the bots data
def saveBot():
    global file
    global knownThings
    file = open("chatbot.txt", 'wb')
    pickle.dump(knownThings, file)
    file.close()

#Starts the program when the application is opened.
startProgram(startUpDisclaimer)