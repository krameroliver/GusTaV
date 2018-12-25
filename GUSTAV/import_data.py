import os,sys
import shutil
from sys import platform as _platform
import re


global source; source = ''
global target; target = ''
global project; project = ''


def system_config():
    print()
    if re.match("win",sys.platform):
        print("Windows")
        globals().update(source = 'c:/appdata/abinitio/data/EDW/Testdata/aktuellerAbzug/input_data/EDW/')
        globals().update(target = 'C:/appdata/abinitio/data/EDW/Testdata/TestDatenContainer')
    elif re.match("linux",sys.platform):
        print("Linux")
        globals().update(source='/appdata/abinitio/data/EDW/Testdata/aktuellerAbzug/input_data/EDW/')
        globals().update(target='/appdata/abinitio/data/EDW/Testdata/TestDatenContainer')
    print("target: "+target)

    #os.mkdirs(source,777)


#def get_highest_version():




def get_projects():
    p = {str(e):i for e,i in enumerate(sorted(os.listdir(source))) if os.path.isdir(os.path.join(source,i))}
    return p

def read_dates_to_copy():
    print("Fuer welches projekt sollen neue Daten importiert werden?")
    proj = get_projects()
    for k in sorted(proj.keys()):
        print("\t{key}: {value}".format(key=k,value=proj[k]))
    selection = input("Auswahl: ")
    project = proj[selection]
    globals().update(project=project)
    globals().update(source=source + project + '/')
    dates ={str(e):i for e,i in enumerate(sorted(os.listdir(source))) if os.path.isdir(source)}
    print("Fuer welches Testdatum wollen sie neue daten importieren?")
    for k in dates.keys():
        print("\t{key}: {value}".format(key=k,value=dates[k]))
    selection = input("Auswahl: ")
    date = dates[selection]
    globals().update(source=source + date + '/')

    target_p = target + "/" + project
    versions_highest = sorted(os.listdir(target_p),reverse=True)[0]
    versions_highest = int(versions_highest.replace("V",""))
    next_version = versions_highest+1

    new_folder = target_p + "/V" + str(next_version)
    if re.match("win", sys.platform):
        print("copy output")
    else:
        os.system("mkdir -p "+ new_folder.replace('/','\\' ) )
        os.system("cp "+source+"* "+new_folder.replace('/','\\' ))




system_config()
read_dates_to_copy()
