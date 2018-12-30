import GUSTAV.MENUE as menue
import os


host = os.environ["PI"]
#host = "entw"

def main():
    m = menue.MENUE()
    m.initial()
    if host == "tint".upper():
        m.tint_menue()
    elif host == "entw".upper():
        m.entw_menue()

if __name__ == "__main__":
    main()
