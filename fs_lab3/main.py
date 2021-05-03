class Student:
    def __init__(self, name=None, usn=None, branch=None, sem=None):
        self.n = name
        self.u = usn
        self.b = branch
        self.s = sem

    def pack(self):
        str = ""
        str = str + self.n + "|" + self.u + "|" + self.b + "|" + self.s + "|"
        str += "\n"
        f = open("students.txt", "a")
        f.write(str)
        print(str)
        f.close()

    def unpack(self):
        fi = open("students.txt", "r")
        line = fi.readline()
        a = line.split("|")

        while line:
            if (a[0][0] != "*"):
                name = a[0]
                usn = a[1]
                branch = a[2]
                sem = a[3]
                print("Name:", name)
                print("USN:", usn)
                print("Branch: ", branch)
                print("SEM: ", sem)

            line = fi.readline()
            a = line.split("|")
        fi.close()

    def search(self, reg):

        fi = open("students.txt", "r+")
        pos = fi.tell()
        line = fi.readline()
        length = len(line)

        a = line.split("|")
        while line:
            if (a[0][0] != "*"):
                name = a[0]
                usn = a[1]
                branch = a[2]
                sem = a[3]
                if (usn == reg):
                    print("Name:", name)
                    print("USN:", usn)
                    print("Branch: ", branch)
                    print("SEM: ", sem)
                    print(" If You Want to Modify Enter yes ")
                    n = input()
                    if n == "yes":
                        fi.seek(pos)
                        na = input("Which Field You Want to Modify? \n1.Name\n2.USN\n3.Branch\n4.SEM\n")
                        if na == "1":
                            name = input("Enter Name")
                        elif na == "2":
                            usn = input("Enter USN")
                        elif na == "3":
                            branch = input("Enter Branch")
                        elif na == "4":
                            sem = input("Enter the SEM")
                        var = ""
                        var = var + name + "|" + usn + "|" + branch + "|" + sem + "|"
                        length2 = len(var)

                        if (length2 < length):
                            fi.write(var)
                            fi.write("\n")
                            print(var)
                            print("Record Successfully Modified!")
                            fi.close()
                            break

                        else:
                            first = a[0][0]
                            fi.write(line.replace(first, "*"))
                            while line:
                                pos = fi.tell()
                                line = fi.readline()
                            fi.seek(pos)
                            fi.write(var)
                            print("Record Successfully Modified!")
                            fi.write("\n")
                            fi.close()
                            break

            pos = fi.tell()
            line = fi.readline()
            length = len(line)
            a = line.split("|")
        fi.close()


s = Student()
n = int(input("1. Enter the Student Detail 1 \n2. Unpack the File Content 2\n3. Search a Student in File\n4. Exit\n"))

while n != 4:
    if n == 1:
        name = input("Enter Name")
        usn = input("Enter USN")
        branch = input("Enter Branch")
        sem = input("Enter the SEM")
        s = Student(name, usn, branch, sem)
        s.pack()
    if n == 2:
        s.unpack()
    if n == 3:
        USNtosearch = input("Enter the USN ")
        s.search(USNtosearch)
    n = int(input(
        "1. Enter the Student Detail 1 \n2. Unpack the File Content 2\n3. Search a Student in File\n4. Exit\n"))
