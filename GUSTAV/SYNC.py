import shutil
import os
import pwd
from time import sleep





class SyncInputData(object):

    def __init__(self):
        self.target = "/appdata/abinitio/data/EDW/Testdata/TestDataContainer/" #"/appdata/abinitio/data/EDW/TestData/Testdaten_Container"
        self.source = "/appdata/abinitio/data/EDW/Testdata/ENTWICKLUNG/" #"/appdata/abinitio/data/EDW/TestData/ENTWICKLUNG"
        self.source_host = "192.168.0.171"
        self.user = None

    def printProgressBar (self,iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
        """
        Call in a loop to create terminal progress bar
        @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
        # Print New Line on Complete
        if iteration == total: 
            print()

    def get_username(self):
        self.user = pwd.getpwuid(os.getuid())[0]
        return pwd.getpwuid(os.getuid())[0]
        #return "oliver"

    def sync(self):
        dry_run = input("wollen sie einen Dry-run durchfuehren?(j/n)" )
        if dry_run == "j":
            dryrun = "n"
        elif dry_run == "n":
            dryrun = ""
        else:
            print("Falsche Eingabe!")

        command = "rsync -akPzbch{dryrun} --stats --delete {user}@{source_host}:{source} {target}".format(dryrun=dryrun,user="bab0255",source_host=self.source_host,source = self.source,target=self.target)
        if  self.get_username() == "bab0255":
            os.system(command)
        else:
            print("Nur als bab0255 ausfuehrbar!")
            print("Warte auf beenden!")
            waits=11
            for i in range(waits+1):
                self.printProgressBar(i,waits)
                sleep(0.5)
            quit()
