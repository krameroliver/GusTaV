import shutil
import os
#import pwd

class SyncInputData(object):

    def __init__(self):
        self.target = "/appdata/abinitio/data/EDW/TestData/Testdaten_Container"
        self.source = "/appdata/abinitio/data/EDW/TestData/TestdatenContainer"
        self.source_host = "blbbdaientw01"
        self.user = None

    def get_username(self):
        #self.user = pwd.getpwuid(os.getuid())[0]
        #return pwd.getpwuid(os.getuid())[0]
        return "oliver"

    def sync(self):
        dry_run = input("wollen sie einen Dry-run durchführen?(j/n)" )
        if dry_run == "j":
            dryrun = "n"
        elif dry_run == "n":
            dryrun = ""
        else:
            print("Falsche Eingabe!")

        command = "rsync -aPzbch{dryrun} --stats --delete --backup-dir='/appdata/abinitio/data/EDW/TestData/backup'  {user}@{source_host}:{source} {target}".format(dryrun = dryrun,user=self.user,source_host=self.source_host,source = self.source,target=self.target)
        os.system(command)