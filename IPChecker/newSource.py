import os
import time

def main():
    nmapType = startUpScreen()
    ipAddr = runIpAddr(nmapType)
    nmap(ipAddr)
    grabNmapIp()

# the only thing the program asks 
def startUpScreen():
    inputVal = False
    while(inputVal == False):
        userInput = input("Are you scanning a wire(d) network or a wireles(s) network?\n>>")
        userInput = userInput.lower()
        if(userInput == 'd'):
            nmapType = 'wired'
            inputVal = True
        elif(userInput == 's'):
            nmapType = 'wireless'
            inputVal = True
        else:
            print("You did not enter a correct input.\n>>")
    return nmapType

def runIpAddr(netType):
    if(netType == 'wired'):
        os.system("ip addr show enp3s0 > ipAddressInfo.txt")

        openIpFile = open("ipAddressInfo.txt", 'r')

        openingFile = openIpFile.read()

        for currentWord in openingFile.split():
            if(currentWord.count('.') == 3):
                return currentWord
    elif(netType == 'wireless'):
        os.system("ip addr show wlan0 > ipAddressInfo.txt")

        openIpFile = open("ipAddressInfo.txt", 'r')

        openingFile = openIpFile.read()

        for currentWord in openingFile.split():
            if(currentWord.count('.') == 3):
                return currentWord

def nmap(ipAddr):
    sendToOs = "nmap"
    
def grabNmapIp():
    currentIPs = []
    readFile = open("commonIps.txt", "r") # open file to read Nmap output
    writeFile = open("saveIps.txt", "w") # open file to write program output (list of ip addr)

    readingFile = readFile.read() # reads the whole file
    print("Starting file scan...")

    # little loading bar script, not needed but it makes it seem like the program is doing more that it really is lol
    loadingBar(30)
    
    # splits the whole Nmap file into seperate words
    for currentWord in readingFile.split():
        if (currentWord.count(".") == 3): # finds ip addrs (looks for 3 periods)
            writeFile.write(currentWord + "\n") # writes the addr to file (new line each time)
            currentIPs.append(currentWord) # appends it to a seperate list to print them out
    print("\nScan finished, this is what I found: ")
    for i in currentIPs: # prints found ip addrs
        print(i)
    
    readFile.close() # close both files
    writeFile.close()

# loading bar func
def loadingBar(barNum):
    for i in range(barNum): 
        time.sleep(.06)
        print("|", end='', flush=True) #flush is to allow it to be printed in real time
main()
