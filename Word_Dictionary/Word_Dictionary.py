import os


class DicT:
    S_no = 0
    d = {}
    file = open(
        "C:/Users/a2z/OneDrive - HANSRAJ COLLEGE/Desktop/Class materials/Python Project/Word_Dictionary/file.txt",
        "r+")
    inventory = open(
        "C:/Users/a2z/OneDrive - HANSRAJ COLLEGE/Desktop/Class materials/Python Project/Word_Dictionary/inventory.txt",
        "r+")

    def __init__(self, wrd, mean):
        self.wrd = wrd
        self.mean = mean

    def new(self):
        run = True
        self.wrd = input("Enter word: ")
        for line in DicT.inventory:
            if self.wrd in line:
                run = False
                break
        if run:
            self.mean = input("Enter the meaning: ")
            DicT.file.seek(0, os.SEEK_END)
            DicT.inventory.seek(0, os.SEEK_END)
            DicT.inventory.write(str(self.wrd) + "\n")
            DicT.file.write(str(self.wrd + " = " + self.mean + "\n"))
        else:
            print("\nAlready in Personal Dictionary !!")
            pass

    def word(self, wrd):
        for line in DicT.file:
            if (wrd + " = ") in line:
                print(line)

    def remove(self, wrd):
        run = True
        for line in DicT.inventory:
            if self.wrd in line:
                run = False
                break
        if run:
            print("f")

    def __str__(self):
        return str(DicT.file.read())
