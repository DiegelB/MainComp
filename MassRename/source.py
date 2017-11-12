import os


def main():
    images = []
    imageSize = 0

    os.system("ls -1 /home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net > oldFileNames.txt")

    importFile = open("oldFileNames.txt", "r")
    exportFile = open("newFileNames.txt", "w")
    
    readingFile = importFile.read()

    for i in readingFile.split():
        images.append(i)
        

    for i in images:
        portToOs = ("mv /home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net/" + "'" + str(i) + "'" + 
                   " /home/skelly/Scripting/AutoDownload/www.freedigitalphotos.net/img_" + str(imageSize))
        os.system(portToOs)
        portToExport = "img_" + str(imageSize) + "\n"
        exportFile.write(portToExport)
        imageSize += 1

    importFile.close()
    exportFile.close()


main()