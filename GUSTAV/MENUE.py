from consols import getTerminalSize



class MENUE(object):

    def __init__(self):
        pass

    def entw_menue(self):
        print("Einbinden der Testdaten")
        menue_points = {1: "Einzelprojekt", 2: "Alle Projekte", 3: "Copy Testdata to Tint", 4: "Exit"}
        while True:
            options = menue_points.keys()
            options.sort()
            for entry in options:
                print("\t", entry, menue_points[entry])

            selection = raw_input("Auswahl: ")
            if selection == '1':
                EP()
            elif selection == '2':
                AllProjects.link_menue()
            elif selection == '3':
                copy_to_tint()
            elif selection == '4':
                quit()
            else:
                print("Unknown Option Selected!")
            print("")

    def tint_menue(self):
        print("Bereitstellen der Daten auf TINT.")
        menue_points = {1: "Copy Testdata to Tint", 2: "Exit"}
        while True:
            options = menue_points.keys()
            options.sort()
            for entry in options:
                print("\t", entry, menue_points[entry])

            selection = raw_input("Auswahl: ")
            if selection == '1':
                copy_to_tint()
            elif selection == '2':
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