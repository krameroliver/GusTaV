import os,sys
import re
keywords = ["system","regression_job","bootstraper","checkout","start-ende","benarichtigung"]


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

    def interpret(self):
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

        for k in self.initial_belegung.keys():
            print(k+": "+self.initial_belegung[k])