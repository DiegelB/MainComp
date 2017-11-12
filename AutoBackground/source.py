import random
import time
import os

def main():
    images = []
    imageSize = 0

    os.system("ls -1 /home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net > fileNamesOutput.txt")

    fileOpen = open("fileNamesOutput.txt", "r")
    readingFile = fileOpen.read()

    for i in readingFile.split():
        images.append(i)
        imageSize += 1

    timerFunc(images)
    
def timerFunc(images):
    previousPicture = ""

    while(True):
        currentPicture = random.choice(images)
        if (currentPicture == previousPicture):
            currentPicture = random.choice(images)
            previousPicture = currentPicture
            portToOs = "gsettings set org.gnome.desktop.background picture-uri file:/home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net/" + currentPicture
            os.system(portToOs)
        else:
            previousPicture = currentPicture
            portToOs = "gsettings set org.gnome.desktop.background picture-uri file:/home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net/" + currentPicture
            os.system(portToOs)
        time.sleep(86400) # every day


main() 
