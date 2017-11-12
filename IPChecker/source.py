import os 
import os.path as osp
import time

def main():
    userInput = int(input("# of files created>>"))

    # this loop counts to 3 the creates a file. It loops for as long o
    for counter in range(userInput):
        timer()
        touch()


# this function runs a timer. It counts to 3 at .5 seconds each
def timer():
    timer = 0
    while timer < 3:
        timer = timer + 1
        print(timer)
        time.sleep(.5) 

# this function creates a file for the input at the top
def touch():
    touch.counter += 1
    enterToOsSystem = "touch file" + str(touch.counter) +".txt"
    os.system(enterToOsSystem)   
    os.system("ls")
touch.counter = 0

main()


