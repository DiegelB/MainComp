import os
import time

def main():

    while(True):
        time.sleep(3) #scans every 30 mins (in seconds) 
        if(os.listdir("/home/skelly/googledrive/AutoBackup") == []): # if googlesrive folder is empty nothing happens
            print("I scanned at " + time.strftime("%I:%M:%S") + " nothing was found.")
        else: # if it has files in it then it moves them locally to ~/BackupLoca
            print("Found 1 or more files...Moving now.")
            os.system("mv /home/skelly/googledrive/AutoBackup/* /home/skelly/")

main()
