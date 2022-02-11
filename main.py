import pandas as pd
from colorama import Fore, Back, Style

file = "csv_report.csv"
run = True
idle="spyder"
bright=""
if idle=="spyder":
    bright=""
elif idle=="pycharm":
    bright = Style.BRIGHT

def INPUT(txt, TYPE):
    global run
    if run:
        try:
            if TYPE == 'int':
                i = int(input(txt))
            elif TYPE == 'float':
                i = float(input(txt))
            elif TYPE == 'str':
                i = input(txt)
            else:
                pass
            return i
        except:
            print(Fore.RED + "ERROR:"+Style.RESET_ALL, f"Only {TYPE} value supported")
            run = False


def add():
    global ch, run

    df = pd.read_csv(file)
    ch = "y"
    while ch == "y":
        run = True
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        roll = INPUT("Enter the roll:", "int")
        if run:
            name = input("Enter the name :")
            Class = input("Enter the Class & Sec :")
            fname = input("Enter the Father name :")

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" MARKS OF TERM TERM I")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        acc1 = INPUT("Enter the marks Accounts: ", "float")
        eco1 = INPUT("Enter the marks Economics:", "float")
        eng1 = INPUT("Enter the marks English:", "float")
        bs1 = INPUT("Enter the marks Business:", "float")
        ip1 = INPUT("Enter the marks IP :", "float")
        if run:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("MkRKS OF TERM II")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        acc2 = INPUT("Enter the marks Accounts:", "float")
        eco2 = INPUT("Enter the marks Economics:", "float")
        eng2 = INPUT("Enter the marks English:", "float")
        bs2 = INPUT("Enter the marks Business:", "float")
        ip2 = INPUT("Enter the marks IP :", "float")
        if run:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            r = df.shape[0]
            df.loc[r, :] = [roll, name, Class, fname, acc1, eco1, eng1, bs1, ip1,acc2, eco2, eng2, bs2, ip2]

            print("Record Inserted Successfully:")
            df.to_csv(file, index=False)
        ch = input("Want to add more(Y/N):").lower()
    run = True


def view():
    df = pd.read_csv(file)
    if df.shape[0] == 0:
        print("No record Found")
    else:
        print(df)


def delete():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Before Deletion ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    df = pd.read_csv(file)
    if df.shape[0] == 0: 
        print("No record Found")
    else:
        print(df)
    idx = int(input("Enter the index to delete"))
    df.drop(idx, axis=0, inplace=True)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("After Deletion ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(df)
    df.to_csv(file, index=False)


def search():
    df = pd.read_csv(file)
    roll = int(input("Enter the roll number:"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your Record")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(df[df.loc[:, "Roll"] == roll])


def update():
    df = pd.read_csv(file)
    print("Before Updation")
    print(df)

    idx = int(input("Enter the index to modify :"))
    roll = int(input("Enter the roll:"))
    name = input("Enter the name ")
    Class = input("Enter the Class & section :")
    fname = input("Enter the Father name :")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("MARKS OF TERM TERM I")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    acc1 = INPUT("Enter the marks Accounts: ", "float")
    eco1 = INPUT("Enter the marks Economics:", "float")
    eng1 = INPUT("Enter the marks English:", "float")
    bs1 = INPUT("Enter the marks Business:", "float")
    ip1 = INPUT("Enter the marks IP :", "float")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("MkRKS OF TERM II")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    acc2 = INPUT("Enter the marks Accounts:", "float")
    eco2 = INPUT("Enter the marks Economics:", "float")
    eng2 = INPUT("Enter the marks English:", "float")
    bs2 = INPUT("Enter the marks Business:", "float")
    ip2 = INPUT("Enter the marks IP :", "float")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    df.loc[idx, :] = [roll, name, Class, fname, acc1, eco1, eng1, bs1, ip1,
                      acc2, eco2, eng2, bs2, ip2]
    print("Record Updated Successfuly:")
    df.to_csv(file, index=False)


def generate():
    df = pd.read_csv(file)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    roll = float(input("Enter the roll number :"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    df1 = pd.DataFrame()
    df1["Roll"] = df["Roll"]

    df1["Total"] = df["acc1"] + df["eco1"] + df["eng1"] + df["bs1"] + df["ip1"] + df["acc2"] + df["eco2"] + df["eng2"] + \
                   df["bs2"] + df["ip2"]
    df1["Per"] = df1["Total"] / 10
    for row, col in df1.iterrows():
        if col.Per > 90:
            df1["Grade"] = "A"
        elif col.Per > 80:
            df1["Grade"] = "B"
        elif col.Per > 70:
            df1["Grade"] = "C"
        else:
            df1["Grade"] = "FAIL"

    df = df[df.loc[:, "Roll"] == roll]
    print(Back.WHITE+Fore.BLACK+"-----------------------------------------"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+bright + "|      TAGORE INTERNATIONAL SCHOOL      |" + Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"-----------------------------------------"+Style.RESET_ALL)
    r, n, c, fn = df1.Roll[0], df.name[0], df.Class[0], df.fname[0]
    print(Back.WHITE+Fore.BLACK+"|"+ bright + " Roll No" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":", r, " " * (39 + -11 - len(str(r)))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright + " Name" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ n+ " " * (41 + -8 - len(n))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright + " Class" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ c+ " " * (41 + -9 - len(c))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright + " Father Name" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ fn+ " " * (41 + -15 - len(fn))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|----------------------------------------"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+bright + "|          Term I  Term II              |" + Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"-----------------------------------------"+Style.RESET_ALL)
    a, e, en, b, i = df.acc1[0], df.eco1[0], df.eng1[0], df.bs1[0], df.ip1[0]
    a2, e2, en2, b2, i2 = df.acc2[0], df.eco2[0], df.eng2[0], df.bs2[0], df.ip2[0]
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Accounts" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t", a, "\t", a2," "*15 ,"|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Economics" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t", e, "\t", e2," "*15 ,"|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "English" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t", en, "\t", en2," "*15 ,"|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Bs" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t\t", b, "\t", b2," "*15 ,"|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "IP" + Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t\t", i, "\t", i2," "*15 ,"|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"-----------------------------------------"+Style.RESET_ALL)

    df1 = df1[df1.loc[:, "Roll"] == roll]
    t, p, g = df1.Total[0], df1.Per[0], df1.Grade[0]
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Total"+ Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t", t, " " * (30 - len(str(t)))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Percentage"+ Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":", p, " " * (26 - len(str(p)))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"|"+ bright+ "Grade"+ Style.RESET_ALL+Back.WHITE+Fore.BLACK+ ":"+ "\t", g, " " * (30 - len(str(g)))+ "|"+Style.RESET_ALL)
    print(Back.WHITE+Fore.BLACK+"-----------------------------------------"+Style.RESET_ALL)
    print()

while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(bright+"= Student Report Card Management System ="+Style.RESET_ALL)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. To add record")
    print("2. To search a record")
    print("3. To delete a record")
    print("4. To view all record")
    print("5. To update a record")
    print("6. To generate a report card")
    print("0. To Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ch = int(input("Enter Your Choice 1 to 6 : "))
    if ch < 1 or ch > 6:
        break
    elif ch == 1:
        add()
    elif ch == 2:
        search()
    elif ch == 3:
        delete()
    elif ch == 4:
        view()
    elif ch == 5:
        update()
    elif ch == 6:
        generate()
