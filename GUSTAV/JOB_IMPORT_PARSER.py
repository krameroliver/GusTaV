import os,sys
import re
keywords = ["system","regression_job","bootstraper","checkout","start-ende","benarichtigung"]
from time import sleep

class Job_Import_Parser(object):
    def __init__(self):
        self.initial_belegung = {
            "system" :"1706_EDW_(ci_test)",
            "regression_job":"True",
            "bootstraper":"True",
            "checkout":"True",
            "start-ende":"True",
            "benarichtigung":"True"
        }
#das ist ein test
    def copy(answer=0,job=""):
        if answer = 1:
            print("copy {job} nach jobgeneration".format(job=job))

    def copy_temp_jobs(self,copy=[]):
        if len(copy)<5:
            print ("error: Abfragen nicht korrekt ausgefüllt.")
        else:
            print (copy)


            quit()

    def interpret_job_def(self):
        in_file = open(r"C:\Users\okramer\Documents\Python\jobdef\job_def.ok_job","r")
        lines = in_file.readlines()
        in_file.close()
        for para in keywords:
            for line in lines:
                #print("line: "+line)
                if re.match(r"<{para}>".format(para=para),line.strip()):
                    replace=re.sub(r"<{para}>".format(para=para),"",line)
                    replace = re.sub(r"</{para}>".format(para=para), "", replace)
                    self.initial_belegung["{para}".format(para=para)]=replace.strip()


    def print_menue(self,menue={},frage=""):
        keys = sorted(menue.keys())
        print(frage)
        for entry in keys:
            print("\t{entry} {meaning}".format(entry=entry,meaning=menue[entry]))
        selection = input("Auswahl: ")
        print("")
        return selection


    def write_job_def(self):
        options = {1:"ja",2:"nein",3:"exit"}
        cc_sys={1:"1706_EDW",
                 2:"1706_EDW_(ci_test)",
                 3:"1706_EDW_(stabilize)",
                 4:"1706_EDW_(nightly)",
                 5:"1706_EDW_FTEST(ftest)",
                 6:"1706_EDW_MAIN(ftest)",
                 7:"1706_EDW_MAIN(tint)",
                 8:"1706_EDW_MONTHLY(ftest)"}

        while True:
            selection_import = self.print_menue(options,"Wollen sie Jobs ind CC importieren?")



            if selection_import == "1":
                selection_system = self.print_menue(cc_sys,"In welches system sollen die Jobs importiert werden?")
                #print(selection_system)
                cc_system = cc_sys[int(selection_system)]
                selection_regression_job = self.print_menue(options, "Wollen sie den regression Job ins CC importieren?")
                selection_bootstraper = self.print_menue(options, "Wollen sie den bootstraper Jobs ins CC importieren?")
                selection_checkout = self.print_menue(options, "Wollen sie den checkout Jobs ins CC importieren?")
                selection_start_ende = self.print_menue(options, "Wollen sie die Start und Ende Jobs ins CC importieren?")
                selection_benarichtigung = self.print_menue(options,
                                                        "Wollen sie den benarichtigungs Job ins CC importieren?")
                copy_array=[selection_regression_job,selection_bootstraper,selection_checkout,selection_start_ende,selection_benarichtigung]
                copy_array = [int(i) for i in copy_array]
                self.copy_temp_jobs(copy_array)

            elif selection_import == "2":
                print("kein jobimport exit")
                sleep(5)
                quit()
            elif selection_import == "3":
                quit()
            else:
                print("falsche eingabe")