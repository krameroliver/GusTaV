from GUSTAV.consols import getTerminalSize
from GUSTAV.SYNC import SyncInputData
from GUSTAV.JOB_IMPORT_PARSER import Job_Import_Parser


class MENUE(object):

    def __init__(self):
        pass

    def entw_menue(self):
        print("Einbinden der Testdaten")
        menue_points = {1: "Einzelprojekt", 2: "Alle Projekte", 3: "Copy Testdata to Tint", 4: "Exit"}
        while True:
            options = menue_points.keys()
            for entry in sorted(options):
                print("\t", entry, menue_points[entry])

            selection = input("Auswahl: ")
            if selection == '1':
                print("LINK_ONE")
            elif selection == '2':
                print("LINK_ALL")
            elif selection == '3':
                print("COPY")
            elif selection == '4':
                quit()
            else:
                print("Unknown Option Selected!")
            print("")

    def tint_menue(self):
        print("Bereitstellen der Daten auf TINT.")
        menue_points = {1: "Copy Testdata to Tint",2: "jobimport", 3: "Exit"}
        while True:
            options = menue_points.keys()

            for entry in sorted(options):
                print("\t", entry, menue_points[entry])

            selection = input("Auswahl: ")
            print("")
            if selection == '1':
                print ("COPY beginnt")
                s_i_d = SyncInputData()
                s_i_d.sync()

            elif selection == "2":
                jip=Job_Import_Parser()
                #jip.interpret()
                jip.write_job_def()
            elif selection == '3':
                quit()
            else:
                print("Unknown Option Selected!")
            print("")

    def initial(self):
        TARDIS = ["######################################################################",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                Das Generalisierte und standardisierte              #",
                  "#                    Testartefakte Verwaltungstool                   #",
                  "#                             GusTaV                                 #",
                  "#                   version: 4,59084371199880305320...               #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "#                                                                    #",
                  "######################################################################"]
        w = getTerminalSize()[0]
        for l in TARDIS:
            print(l.center(w, " "))