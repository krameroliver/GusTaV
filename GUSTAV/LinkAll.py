import os,sys
import re
from time import sleep

src = r"/appdata/abinitio/data/EDW/Testdata/TestDataContainer"
tgt = r"/appdata/abinitio/data/EDW/Testdata/ENTWICKLUNG"
log = r"/appdata/abinitio/data/EDW/Testdata/link.log"

def get_next_instance(path):
    sub_dirs = os.listdir(path=path)
    instances = [i for i in sub_dirs if os.path.isdir(os.path.join(path,i))]
    return instances

def print_menue(menue={},frage=""):
    keys = sorted(menue.keys())
    print(frage)
    for entry in keys:
        print("\t{entry} {meaning}".format(entry=entry,meaning=menue[entry]))
    selection = input("Auswahl: ")
    print("")
    return selection



def link_all():
    print("WARNING: Es werden nur fuer den SIT test zugelassene Versionen Verlinkt!")
    print("WARNUNG: Es wird die neuste Version aller Projekte verlinkt!")
    options = {1: "ja", 2: "nein", 3: "exit"}

    selection = print_menue(options,"Wollen sie die Verlinkung wirklich starten?")

    if selection == "1":

        all_projects = get_next_instance(src)
        print (all_projects)
        pattern = "V[0-9]*"
        for i in all_projects:
            versions = [v for v in get_next_instance(os.path.join(src,i)) if os.path.isdir(os.path.join(src,i,v)) and re.match(pattern,v)]
            versions = sorted(versions,reverse=True)
            #print(versions)
            source = os.path.join(src,i,versions[0])
            target = os.path.join(tgt, i)
            print("#####################################################################################################")
            print("source: "+source)
            print("target: "+target)
            print(
                "#####################################################################################################")
            #os.link(source, target)
            os.system("ln -s {source} {target}".format(source=source,target=target))
            print("PIPI fein!")
    elif selection == "2":
        print("GusTaV beendet sich in 5 Sekunden!")
        sleep(5)
        quit()
    elif selection == "3":
        quit()
    else:
        print("Falsche Eingabe!")
