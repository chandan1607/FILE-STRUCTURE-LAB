
array = []

class student:
    def __init__(self, usn, name, sem, branch):
        self.usn = usn
        self.name = name
        self.sem = sem
        self.branch = branch


    def pack(self,file):
        record = self.usn+"|"+self.name+"|"+self.sem+"|"+self.branch+"|"

        if len(record) > 45:
            print("Exceeded")
        while len(record) <46:
            record += "#"
        record += "\n"

        file.write(record)

    def modifyUsn(self):
        newUsn = input("enter your usn")
        self.usn = newUsn

    def modifyName(self):
        newName = input("enter your name")
        self.name = newName

    def modifySem(self):
        newSem = input("enter your sem")
        self.sem = newSem

    def modifyBranch(self):
        newBranch = input("enter your branch")
        self.branch = newBranch


def unpack():
    with open("students.txt", "r") as file:
        for line in file:
            fields = line.strip("#\n").split("|")[:-1]
            array.append(student(fields[0],fields[1],fields[2],fields[3]))


def search():

    got = False
    for i in array:
        if key == i.usn:
            got=True
            print("record found")
            while True:
                option = input(
                    "Select The Data To Modify\n1.Usn\n2.Name\n3.Sem\n4.branch\n 5.Exit\t"
                )
                if option == "1":
                    i.modifyUsn()
                elif option == "2":
                    i.modifyName()
                elif option == "3":
                    i.modifySem()
                elif option == "4":
                    i.modifyBranch()
                elif option == "5":
                    break


    if not got:
        print("\n----Record Not Found----\n")





while True:
    choice = input("1.Insert Student Details\n2.Search and Modify Student Details\n3.Exit\n "
                   "Enter your choice ")


    if choice == "1":
        usn = input("Enter USN \t")
        name = input("Enter Name \t")
        sem = input("Enter Sem \t")
        branch = input("Enter Branch \t")
        newStudent = student(usn,name,sem,branch)
        with open("students.txt", "a+") as file:
            newStudent.pack(file)


    elif choice == "2":
        array = []
        unpack()
        key = input("Enter The USN search & modify\n")
        search()
        with open("students.txt", "w+") as file:
            for i in array:
                i.pack(file)
    elif choice == "3":
        break
    else:
        print ("not found")
array = []

class student:
    def __init__(self, usn, name, sem, branch):
        self.usn = usn
        self.name = name
        self.sem = sem
        self.branch = branch


    def pack(self,file):
        record = self.usn+"|"+self.name+"|"+self.sem+"|"+self.branch+"|"

        if len(record) > 45:
            print("Exceeded")
        while len(record) <46:
            record += "#"
        record += "\n"

        file.write(record)

    def modifyUsn(self):
        newUsn = input("enter your usn")
        self.usn = newUsn

    def modifyName(self):
        newName = input("enter your name")
        self.name = newName

    def modifySem(self):
        newSem = input("enter your sem")
        self.sem = newSem

    def modifyBranch(self):
        newBranch = input("enter your branch")
        self.branch = newBranch


def unpack():
    with open("students.txt", "r") as file:
        for line in file:
            fields = line.strip("#\n").split("|")[:-1]
            array.append(student(fields[0],fields[1],fields[2],fields[3]))


def search():

    got = False
    for i in array:
        if key == i.usn:
            got=True
            print("record found")
            while True:
                option = input(
                    "Select The Data To Modify\n1.Usn\n2.Name\n3.Sem\n4.branch\n 5.Exit\t"
                )
                if option == "1":
                    i.modifyUsn()
                elif option == "2":
                    i.modifyName()
                elif option == "3":
                    i.modifySem()
                elif option == "4":
                    i.modifyBranch()
                elif option == "5":
                    break


    if not got:
        print("\n----Record Not Found----\n")





while True:
    choice = input("1.Insert Student Details\n2.Search and Modify Student Details\n3.Exit\n "
                   "Enter your choice ")


    if choice == "1":
        usn = input("Enter USN \t")
        name = input("Enter Name \t")
        sem = input("Enter Sem \t")
        branch = input("Enter Branch \t")
        newStudent = student(usn,name,sem,branch)
        with open("students.txt", "a+") as file:
            newStudent.pack(file)


    elif choice == "2":
        array = []
        unpack()
        key = input("Enter The USN search & modify\n")
        search()
        with open("students.txt", "w+") as file:
            for i in array:
                i.pack(file)
    elif choice == "3":
        break
    else:
        print ("not found")

















