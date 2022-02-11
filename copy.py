import pandas as pd
import numpy as np


def add():
    df = pd.read_csv("csv_report.csv")
    ch = "y"
    while ch == "y" or ch == "Y":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        roll = int(input("Enter the roll:"))
        name = input("Enter the name :")
        Class = input("Enter the Class & Sec :")
        fname = input("Enter the Father name :")
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(" MARKS OF TERM TERM I")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        acc1 = float(input("Enter the marks Accounts: "))
        eco1 = float(input("Enter the marks Economics:"))
        eng1 = float(input("Enter the marks English:"))
        bs1 = float(input("Enter the marks Business:"))
        ip1 = float(input("Enter the marks IP :"))
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("MkRKS OF TERM II")
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        acc2 = float(input("Enter the marks Accounts:"))
        eco2 = float(input("Enter the marks Economics:"))
        eng2 = float(input("Enter the marks English:"))
        bs2 = float(input("Enter the marks Business:"))
        ip2 = float(input("Enter the marks IP :"))
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        r = df.shape[0]
        df.loc[r, :] = [roll, name, Class, fname, acc1, eco1, eng1, bs1, ip1,
                        acc2, eco2, eng2, bs2, ip2]
        print("Record Inserted Successfuly:")
        ch = input("Want to add more(Y/N):")
        df.to_csv("csv_report.csv", index=False)


def view():
    df = pd.read_csv("csv_report.csv")
    if df.shape[0] == 0:
        print("No record Found")
    else:
        print(df)


def delete():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Before Deletion ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    df = pd.read_csv("csv_report.csv")
    if df.shape[0] == 0:
        print("No record Found")
    else:
        print(df)
    idx = int(input("Enter the index to delete"))
    df.drop(idx, axis=0, inplace=True)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("After Deletion ")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(df)
    df.to_csv("csv_report.csv", index=False)


def search():
    df = pd.read_csv("csv_report.csv")
    roll = int(input("Ehter the roll num ber:"))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Your Record")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(df[df.loc[:, "Roll"] == roll])


def update():
    df = pd.read_csv("csv_report.csv")
    print("Before Updation")
    print(df)

    idx = int(input("Enter the index to modify :"))
    roll = int(input("Enterthe roll:"))
    name = input("Enter the name ")
    Class = input("Enter the Class & section :")
    fname = input("Enter the Father name :")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("MARKS OF TERM TERM I")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    acc1 = float(input("Enter the marks Accounts: "))
    eco1 = float(input("Enter the marks Economics:"))
    eng1 = float(input("Enter the marks English:"))
    bs1 = float(input("Enter the marks Business:"))
    ip1 = float(input("Enter the marks IP :"))
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("MkRKS OF TERM II")
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    acc2 = float(input("Enter the marks Accounts:"))
    eco2 = float(input("Enter the marks Economics:"))
    eng2 = float(input("Enter the marks English:"))
    bs2 = float(input("Enter the marks Business:"))
    ip2 = float(input("Enter the marks IP :"))
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    df.loc[idx, :] = [roll, name, Class, fname, acc1, eco1, eng1, bs1, ip1,
                      acc2, eco2, eng2, bs2, ip2]
    print("Record Updated Successfuly:")
    df.to_csv("csv_report.csv", index=False)


def generate():
    df = pd.read_csv("csv_report.csv")
    # print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    roll = float(input("Enter the roll number :"))
    # print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
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
    print("-----------------------------------------")
    print("| TAGORE INTERNATIONAL SCHOOL |")
    print("-----------------------------------------")
    r, n, c, fn = df1.Roll[0], df.name[0], df.Class[0], df.fname[0]
    print("| Roll No : ", "\t", r, "\t\t\t\t\t|")
    print("| Name : ", "\t", n, "\t\t|")
    print("| Class : ", "\t", c, "\t\t\t\t|")
    print("| Father Name : ", "\t", fn, "\t\t|")
    print("|----------------------------------------")
    print("| Term I Term II |")
    print("-----------------------------------------")
    a, e, en, b, i = df.acc1[0], df.eco1[0], df.eng1[0], df.bs1[0], df.ip1[0]
    a2, e2, en2, b2, i2 = df.acc2[0], df.eco2[0], df.eng2[0], df.bs2[0], df.ip2[0]
    print("| Accounts : ", "\t", a, "\t", a2, "\t\t|")
    print("| Economics : ", "\t", e, "\t", e2, "\t\t|")
    print("| English : ", "\t", en, "\t", en2, "\t\t|")
    print("| Bs : ", "\t", b, "\t", b2, "\t\t|")
    print("| IP : ", "\t", i, "\t", i2, "\t\t|")
    print("----------------------------------------")

    df1 = df1[df1.loc[:, "Roll"] == roll]
    t, p, g = df1.Total[0], df1.Per[0], df1.Grade[0]
    print("| Total : ", "\t", "\t", t, "\t\t|")
    print("| Percentage : ", "\t", "\t", p, "\t\t|")

    print("| Grade : ", "\t", "\t", g, "\t\t|")
    print("-----------------------------------------")
    print()


while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("= Student csv_report Card Management System =")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("1. To add record")
    print("2. To search a record")
    print("3. To delete a record")
    print("4. To view all record")
    print("5. To update a record")
    print("6. To generate a reort card")
    print("0. To Exit")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
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
