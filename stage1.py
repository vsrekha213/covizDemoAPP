import os
import csv

from datetime import date
def adminauthorization():
    os.system("cls")
    print("Welcome")
    adminchoice = int(input(" 1. View \n 2. Add \n 3. Update \n"))
    if adminchoice == 1:
        with open("E:\\CPS\\admin.csv") as fp:
            obj = csv.reader(fp)
            a_table = []
            for row in obj:
                a_table.append(row)
            length_list = [len(element) for row in a_table for element in row]
            column_width = max(length_list)
            for row in a_table:
                row = "".join(element.ljust(column_width + 2) for element in row)
                print(row)
                print("-"*130)
        return

    if adminchoice == 2:
        os.system("cls")
        tdDate = date.today().strftime("%d/%m/%Y")
        covaxinAvailablity = int(input("Covaxin Availablity : "))
        covishieldAvailablity = int(input("Covaxin Availablity : "))
        row = [tdDate, covaxinAvailablity, covishieldAvailablity, covaxinAvailablity, covishieldAvailablity]
        with open("admin.csv","a") as fp:
            obj = csv.writer(fp)
            obj.writerow(row)
        return

    if adminchoice == 3:
        os.system("cls")
        dateupdate = input("Enter date in [dd-mm-yy] format : \t")
        with open("E:\\CPS\\admin.csv") as fp:
            obj = csv.reader(fp)
            a_table = []
            for row in obj:
                a_table.append(row)
        print(len(a_table))
        lis = []
        for i in range(len(a_table)-1):
            lis.append([i,a_table[i][0]])
        print(lis)
        index = 0
        if dateupdate in lis[-1]:
            for i in range(len(lis)):
                if lis[i][-1] == dateupdate:
                    index = lis[i][0]
            print(index)
            updatechoice = int(input("1. Date 2.Covaxin Availablity 3.Covishield Availablity 4.Remaining_Covaxin 5.Remaining_Covishield"))
            updatevalue  = int(input("enter value"))
            a_table[index-2][updatechoice-2] = updatevalue
            # a_table[]

        else:
            print("sorry we coludn't fetch the details for ",dateupdate,"date")
    else:
        print("Try again")
        return



def admin():
    print("ADMIN PORTAL")
    ids = int(input("Enter your Admin Id : \t"))
    pwd = input("Enter your Password : \t")
    chance = 0
    while chance <= 3:
        if chance == 3:
            print("Invalid user name or password")
            authentication()
            break
        if ids == 123 and pwd == "admin":
            adminauthorization()
            break
        chance += 1


def user():
    pass


def authentication():
    os.system("cls")
    print("*" * 10, "Welcome to Coviz", "*" * 10)
    ch = int(input("Choose \n 1. ADMIN Login  \n 2. User Login \n "))
    if ch == 1:
        os.system("cls")
        admin()
    elif ch == 2:
        user()
    else:
        print("Sorry Couldn't process")


if __name__ == '__main__':
    authentication()
