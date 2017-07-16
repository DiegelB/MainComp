import random
import subprocess
import pickle
import datetime

# All of the global values that are used to store conversation data
global knownThings
# Lists of bot-known items, as well as current conversation status
knownThings = []
# The last thing the bot said (used so the bot wont say the same thing twice)
globalCurrent = ['']
# The last user response
globalUser = []
# the name of the user
userName = []
# About Xeria
startUpDisclaimer = "Xeria ChatBot Ver_pDEV.03\n" \
                    "Author *|^|MLGSkelly|^|*\n\n" \
                    "      ---About Xeria---\n" \
                    "This bot learns from user input.\n" \
                    "Currently Xeria responds at random.\n" \
                    "In time she will be able to hold \n" \
                    "everyday, normal conversations.\n" \
                    "If you need help with commands,\n" \
                    "please type 'help me Xeria'.\n"
# Used to grab an item from a list at random
secure_random = random.SystemRandom()

# SCRIPTS---------------------------------------------------------------------------------------------------------SCRIPTS
# list of key words to use Xeria
def keyWordHelp():
    print("\n" + "           --Keywords--\n"
                 "'help me Xeria' -- Opens this menu\n"
                 "'goodbye Xeria' -- Closes program\n"
                 "'open a program Xeria' -- Starts a program\n"
                 "    **capitalization matters**\n")
    input("Press enter to return to Xeria\n")
    mainLoop()

# When Xeria's name is asked
def myNameScript(UN):
    nameLibrary = ['My name is Xeria. What is yours?', 'Xeria, whats yours?', 'Hello, I am '
                                                                              'Xeria, whats your name?',
                   'Xeria, whos askin?']
    print('Xeria: ' + secure_random.choice(nameLibrary))
    UN.insert(0, input("User: "))
    print("Xeria: Hello " + str(UN[0]))
    mainLoop()

# rick and morty easter egg
def myPurpose():
    print("Xeria: You pass the butter.")
    mainLoop()

# Opens various programs from users files
def openProgramScript():
    userResponse = input("Xeria: What program would you like to open? Reply with "
                         "'Chrome', 'Steam', or 'PyCharm'!\nUser: ")
    if "Chrome" in userResponse or "chrome" in userResponse:
        subprocess.Popen([r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
        print("Xeria: Chrome has been opened.")
        mainLoop()
    elif "Steam" in userResponse or "steam" in userResponse:
        subprocess.Popen([r"C:\Program Files (x86)\Steam\Steam.exe"])
        print("Xeria: Steam has been opened.")
        mainLoop()
    elif "PyCharm" in userResponse or "pycharm" in userResponse:
        subprocess.Popen([r"C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.3\bin\pycharm64.exe"])
        print("Xeria: PyCharm has been opened.")
        mainLoop()
    else:
        print("Xeria: I'm sorry, you did not input a valid response. Please press enter to return"
              "talking to me!\n")
        input()
        mainLoop()

# The bot tells the user the current time. IN 24 HOUR TIME, NEED TO MAKE IT 12 HOUR TIME
def timeScript():
    time = datetime.datetime.now()
    print("Xeria: The current time is - " + str(time.hour) + ":" + str(time.minute))
    mainLoop()

# When Xeria is thanked
def thankYouScript(UN):
    botResponse = ['You are very welcome ', 'No problem ', 'Dont mention it ', 'Anytime ', 'As always ']
    # This algorithm checks if there is a name within userName. if there is not it calls the user User
    if not UN:
        print("Xeria: " + secure_random.choice(botResponse) + "User" + '!')
    else:
        print("Xeria: " + secure_random.choice(botResponse) + str(UN[0]) + '!')
    mainLoop()

# Picks a random one-liner joke to say to the user
def jokeScript():
    knownJokes = ['I have the heart of a lion and a lifetime ban from the Toronto zoo.',
                  'A man walked into his house and was delighted when he discovered '
                  'that someone had stolen all of his lamps.',
                  'Its hard to explain puns to kleptomaniacs because they always take '
                  'things literally.',
                  'I discovered a substance that had no mass, and I was like "0mg!"',
                  'Parallel lines have so much in common but it’s a shame they’ll never meet.',
                  'Bug? Thats not a bug, thats a feature', 'Computer programmers do it byte by byte.',
                  'Computers are not intelligent. They only think they are.',
                  'FORMATTING DRIVE C:/ PLEASE WAIT...', 'Dont hit the keys so hard, it hurts.']
    print("Xeria: " + secure_random.choice(knownJokes))
    mainLoop()

# It grabs the name of the user if a key word it seen
def grabNameScript(UN):
    print("Xeria: What is your name?")
    userResponse = input("User: ")
    UN.insert(0, userResponse)
    print("Xeria: Hello " + UN[0] + "!")
    mainLoop()

def notNiceScript(UN):
    if not UN:
        print("Xeria: You are not being nice right now User.")
    else:
        print("Xeria: You are not being nice right now " + UN[0] + ".")
    mainLoop()

# This randomizes a script to choose from so Xeria can engage the user
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def randomScript():
    randomScriptNum = random.randint(1, 2)
    if randomScriptNum == 1:
        howWasDay(userName)
    elif randomScriptNum == 2:
        jokeScript()

# Bot asks how the users day has been
def howWasDay(UN):
    botResponse = ['How was your day', 'How has your day been?', 'What have you been up to today?']
    print("Xeria: " + secure_random.choice(botResponse))
    userResponse = input("User: ")
    userResponse = userResponse.lower()
    saveInput(userResponse)
    if "not" in userResponse:
        print("Xeria: Oh no, how can I help? Would you like to hear a joke?")
        userResponse = input("User: ")
        userResponse = userResponse.lower()
        if "yes" in userResponse or "yeah" in userResponse or "sure" in userResponse or "that" in userResponse \
                or "ok" in userResponse or "okay" in userResponse:
            jokeScript()
        else:
            print("Xeria: Well I hope your day will be better while talking to me!")
            mainLoop()
    else:
        botResponse = ['Good to hear ', 'That is a-okay ', 'Wonderful stuff I see ', 'Good to know ',
                       'Thaaaaats greeeeaaat ']
        if not UN:
            print("Xeria: " + secure_random.choice(botResponse) + "User.")
        else:
            print("Xeria: " + secure_random.choice(botResponse) + UN[0] + ".")
        mainLoop()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Function to exit Xeria
def goodByeUser(UN):
    if not UN:
        print("Xeria: Goodbye User...")
        input("Press enter to exit Xeria\n")
        exit()
    else:
        print("Xeria: Goodbye " + UN[0])
        input("Press enter to exit Xeria\n")
        exit()

# SCRIPTS---------------------------------------------------------------------------------------------------------SCRIPTS
# Saves the bots data
def saveBot():
    global file
    global knownThings
    file = open("chatbot.txt", 'wb')
    pickle.dump(knownThings, file)
    file.close()

# Used to save user input and at it to the known things for the bot
def saveInput(userInput):
    global knownThings
    knownThings.append(userInput)
    saveBot()

# The logical operators of the bot so it doesnt seem as dumb
def botSpeak(GC):
    global knownThings
    current = secure_random.choice(knownThings)
    # This adds a more engaging responses for the bot. it has a 10% chance to run a random pre-defined
    # script-tree.
    chanceForScript = random.randint(1, 20)
    if chanceForScript == 1:
        randomScript()
    else:
        # this if statement stops Xeria from repeating the same thing twice in a row
        if current == GC[0]:
            botSpeak(GC)
        else:
            print("Xeria: " + current)
            GC[0] = current

# checks for key words in user input
def keyWordChecker(UI):
    if UI == "help me Xeria":
        keyWordHelp()
    elif UI == "goodbye Xeria":
        goodByeUser(userName)
    elif "your name" in UI:
        myNameScript(userName)
    elif "my purpose?" in UI or "What is my purpose?" in UI:
        myPurpose()
    elif "open a program Xeria" in UI:
        openProgramScript()
    elif "what" in UI and "time" in UI and "is" in UI:
        timeScript()
    elif "thank" in UI and "you" in UI or "Thank" in UI and "you" in UI \
            or "thanks" in UI:
        thankYouScript(userName)
    elif "tell" in UI and "joke" in UI or "know" in UI and "joke" in UI or "what's" in UI \
            and "joke" or "what is" in UI and "joke" or "whats" in UI \
            and "joke" in UI or "got" in UI and "joke" in UI:
        jokeScript()
    elif "my name" in UI or "call me" in UI or "My name" in UI or "Call me" in UI:
        grabNameScript(userName)
    elif "I hate you" in UI or "i hate you" in UI or "you" in UI and "stupid" in UI \
            or "you" in UI and 'dumb' in UI or "your" in UI and "stupid" in UI:
        notNiceScript(userName)
    else:
        botSpeak(globalCurrent)
        saveInput(UI)
        mainLoop()

# This main loop of the program that jumps back and forth to save the data
def mainLoop():
    userInput = input("User: ")
    keyWordChecker(userInput)

# This is when the application is opened. It loads the previous file and prompts the user to talk.
def startProgram(SUD):
    global knownThings
    file = open("chatbot.txt", 'rb')
    knownThings = pickle.load(file)
    file.close()
    print(SUD)
    print("Xeria: Hello User, my name is Xeria. How are you?")
    mainLoop()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Starts the program when the application is opened.
startProgram(startUpDisclaimer)
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Testing changes