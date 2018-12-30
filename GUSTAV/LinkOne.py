import os,sys


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


def link():
    Projects = {str(e):i for e,i in enumerate(get_next_instance(src))}
    selected_project = print_menue(Projects,"Welches Projekt Wollen sie neu verlinken?")
    #print(Project)
    Versions = {str(e):i for e,i in enumerate( get_next_instance(os.path.join(src,Projects[selected_project]))  )}
    selected_version = print_menue(Versions,"Welche Version soll verlinkt werden?")
    source = os.path.join(src,Projects[selected_project],Versions[selected_version])
    target = os.path.join(tgt,Projects[selected_project])
    #os.link(source,target)
    #print("ln -s {source} {target}".format(source=source,target=target))
    os.system("ln -s {source} {target}".format(source=source,target=target))
    print("PIPI fein!")
