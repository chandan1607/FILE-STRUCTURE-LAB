class student:
    def __init__(self, li=[]):
        con = ''
        self.list = li
        fi = open("index.txt", "r")
        pos = fi.tell()
        line = fi.readline()
        while line:
            con = ''
            a = line.split("|")
            con = con + str(a[0]) + "|" + str(pos) + "|"
            if (a[0][0] != "*"):
                self.list.append(con)
            pos = fi.tell()
            line = fi.readline()

        self.list.sort()
        fi.close()

    def getstu(self):
        self.name = input("Enter Name")
        self.usn = input("Enter USN")
        self.branch = input("Enter Branch")
        self.sem = input("Enter The SEM")

    def pack(self):
        char = ''
        self.getstu()
        st = ""
        st = st + self.name + "|" + self.usn + "|" + self.branch + "|" + self.sem + "|"
        fi = open("record.txt", "r")

        line = fi.readline()
        while line:
            line = fi.readline()
        pos = fi.tell()
        fi.close()
        file = open("index.txt", "a")
        position = file.tell()
        con = self.usn + "|" + str(pos) + "|"
        file.write(con)
        file.write("\n")
        file.close()
        f = open("record.txt", "a")
        f.write(st)
        f.write("\n")
        f.close()
        char = char + self.usn + "|" + str(position)
        self.list.append(char)
        self.list.sort()

    def unpack(self):
        fi = open("record.txt", "r")
        line = fi.readline()
        a = line.split("|")
        while line:
            if (a[0][0] != "*"):
                n = a[0]
                u = a[1]
                b = a[2]
                s = a[3]
                print("Name:", n)
                print("USN:", u)
                print("Branch: ", b)
                print("SEM: ", s)
            line = fi.readline()
            a = line.split("|")
        fi.close()

    def search(self):
        nam = input("Enter USN of The Student")

        flag = self.binarysearch(nam)
        if (flag == -1):
            print("Not There In The Record File")
        else:
            lin = self.list[flag]
            a = lin.split("|")
            pos = a[1]
            file = open("index.txt", "r+")
            file.seek(int(pos))
            l = file.readline()
            c = l.split("|")
            posi = c[1]
            fi = open("record.txt", "r+")
            fi.seek(int(posi))
            line = fi.readline()
            b = line.split("|")
            name = b[0]
            usn = b[1]
            branch = b[2]
            sem = b[3]
            print("Name:", name)
            print("USN:", usn)
            print("Branch: ", branch)
            print("SEM: ", sem)

    def binarysearch(self, nam):
        lis = []
        l = 0
        r = len(self.list)
        for i in range(0, r):
            a = self.list[i].split("|")
            lis.append(a[0])

        while (l <= r):
            m = (l + r) // 2
            if (nam == lis[m]):
                return m
            if (lis[m] < nam):
                l = m + 1
            else:
                r = m - 1

        return -1

    def delete(self):
        nam = input("Enter USN of The Student")
        flag = self.binarysearch(nam)
        if (flag == -1):
            print("Not There In The Record File")
        else:
            line = self.list[flag]
            a = line.split("|")
            pos = int(a[1])
            f = open("index.txt", "r+")
            f.seek(pos)

            l = f.readline()
            b = l.split("|")
            first = b[0][0]
            f.seek(pos)
            f.write(line.replace(first, "*"))
            position = b[1]

            file = open("record.txt", "r+")
            file.seek(int(position))
            line = file.readline()
            a = line.split("|")
            first = a[0][0]
            file.seek(int(position))
            file.write(line.replace(first, "*"))
            file.close()
            del self.list[flag]
            self.list.sort()
            print(nam, " as deleted")


s = student()
n = int(input(
    "1. Enter the Student Details \n2. To Unpack \n 3. To Search a Student \n4. To Delete a Student \n5. To Exit"))
while (n != 5):
    if (n == 1):
        s.pack()
    if (n == 2):
        s.unpack()
    if (n == 3):
        s.search()
    if (n == 4):
        s.delete()
    n = int(input(
        "1. Enter the Student Details \n2. To Unpack \n 3. To Search a Student \n4. To Delete a Student \n5. To Exit"))
