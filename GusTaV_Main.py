import GUSTAV.MENUE as menue

host = "entw"

def main():
    m = menue.MENUE()
    m.initial()
    if host == "tint":
        m.tint_menue()
    elif host == "entw":
        m.entw_menue()

if __name__ == "__main__":
    main()