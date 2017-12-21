# filename: application.py
# -*- coding: cp1251 -*-
from people import *
import os
import sys
import time
# ���������� ������������ ������� ������� ��� ����������� ��������� CP1251
"""������ �������� �������� � ���������� ������ Application, ������������� ������-������ ����������"""
class Application:
    """������ ����� ���������� ������-������ ���������� �� ��������� ���� ��������"""
    # �������� ������� ������ - ����� �������� ��� ���� ����������� ������
    fullName = str()  # Application.fullName - ��������� ������������� ����� �������� � ��
    date = str()      # Application.date     - ��������� ������������� ���� �������� � ��
    day = 0           # Application.day      - ���� ��������
    month = 0         # Application.month    - ����� ��������
    year = 0          # Application.year     - ��� ��������
    daysOfMonth = [0, 31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]  # ������ ���������� ���� � ������� ��� �� ����������� ����
    def __init__(self):
        """����������� ������ Application �������� �� ������ ��������� ���������
        ���� ��������, ����������� �������� ���������� ������ � ������������� ���
        ��� �������� �� ���������."""
        self.fileName = None  # ��� ����� ��
        self.status = False   # ������ ���������, ��������� � ������������ � ����� ��
        # self.status = False ��������, ��� ���� �� �� �������� ���� ��� ��������
        # self.status = True ��������, ��� ���� �� �������� � ������ ���������
        self.f = None  # ������ �� �������� ������, ��������� � ��
        self.fileStatus = False  # ������� ������, ��������������� ��� ���������� �������� �������������
        # ���������� ����� ��
        self.birthdays = []  # ��� �������� ���������� ������ ��������� ������ ������ ������� ���� ��������
        self.mode = False  # ����� ������� ���������: False - ������� ����� ���� ��, True - ������� ������������ ����
        self.date = None
        self.d = [r"�����������", r"�������", r"�����", r"�������",
                  r"�������", r"�������", r"�����������"]
        self.m = ["" , r"������", r"�������", r"�����", r"������", r"���", r"����",
                  r"����", r"�������", r"��������", r"�������", r"������", r"�������"]
        self.t = time.localtime()  # �������� ������� �������� ���� � �������
        self.ageStatus = False  # ���� �� ��������� ��������� ���������� �������� ����� ��� ������� ��
    # END class constructor Application.__init__()

    def __del__(self):
        print(r">>> ������ ��������� ��������� / The work of the program is completed.")

    def run(self):
        """����� �������� �� ���������� ������-������, �� ���� ���������� ������������������ ������ ��������"""
        self.startMenu()  # ���������� ����� ������ � ������ ��: '��������� �����' ��� '������� ������������'
        self.mainMenu()   # ���������� ����������� ���� ������������, ��������� � ������ ��������� �������� ������
    # END method Application.run()

    def startMenu(self):
        """������ ����� ������ ������������ ���  ����������� �������� ������ ������ ������ � ������ �� ���� ��������"""
        print(r"=== ��������� - �������� ���� �������� =====================")
        print("= �������: %11s %s %s %s %02d:%02d:%02d = %02d.%02d.%04d =" %
              (self.d[self.t[6]], self.t[2], self.m[self.t[1]], self.t[0],
               self.t[3], self.t[4], self.t[5],
               self.t[2], self.t[1], self.t[0]))
        print(r"============================================================")
        print(r"������� ����� ���� �� ���� �������� (Y/N) : ", end='')
        choice = input()
        if choice == 'Y' or choice == 'y':
            # ������������ ������ '�������' ����� ���� ��
            self.fileName = input(">>> ������ ��� ������ ����� ��� �� : ")
            print(">>> �� ����� : %s " % self.fileName)
        else:
            # ������������ ������ ������ � ����� ��������� � ����������� ������ ��
            # ��������� ����� ����� ����� ��
            self.fileName = input(">>> ������� ��� ����� �� : ")
            fileStatus =  os.access(self.fileName, os.F_OK)  # �������� ������������� ���������� �����
            if not fileStatus:  # ���� ���������� ������� ��������� ���� - ��������, ������� ������� ��� �����
                print("���� � ����� ������ �������!")
                sys.exit(1)  # ������ ��������� ����������� �������� � ������� ���������������� ���������
            # ��������� ������ ����� �� ����� ��������� � ������� ��������� ���������
            with open(self.fileName, mode='r', encoding='cp1251') as f:
                for line in f:
                    line = line.strip(' ')
                    print(line, end='')  # ����������� �� ����� ������
                    # ������ ��������� ������ �������� ������ � ������� <���> : <��.��.����>
                    # ����������� ������ ����� ���������� � ������� � ������ self.birthdays
                    # ������������, ��� ���� �������� ������ � ��������� �������
                    line = line.split(':')  # line - ������ �����, ���������� �� ����������� ������, ����������� - ':'
                    if len(line) != 2:      # �� ����� ������� ������, ���������� ������ � �������� �������
                        continue            # ���������� ������, ���������� �������� ������ � ����� � ��� ��������
                    else:
                        Application.fullName = line[0].strip(' ')  # ������� � ������������ ������, ���������� ��� ��������
                        Application.date = line[1]          # ������� ������ ���� ��������, �� ����� ����������
                        self.dateParsing(Application.date)  # ����� ������ �������� ���� - ������� ������ ��.��.����
                        temp = People(Application.fullName, Application.day, Application.month, Application.year)
                        self.birthdays.append(temp)  # �������� ����� ������ � ��
                # END circle for - ��������� ��� ������ �� ����� ��
            # ����� ������ ���� ����� �� ����� � �� ���������, ���� ����� ������������� ������ =)
            #self.f = open(self.fileName, mode="r", encoding="cp1251")

        self.mainMenu()
    # END method Application.startMenu()

    def mainMenu(self):
        """��������� ���� ���������, ��������� � ��������� ��������� ��������
        ������������� ������ � ������"""
        while True:
            command=input(">> Enter the Command >> ")
            command = command.strip(' ')
            if command == 'help':
                self.help()
            elif command == 'new':
                print("Input new")
                self.new()
            elif command == 'new_pars':
                self.newParsing()
            elif command == 'find_name':
                self.find_name()
            elif command == 'find_birthday':
                self.find_birthday()
            elif command == "change":
                self.change()
            elif command == "show":
                self.show()
            elif command == 'age':
                self.age()
            elif command == 'show_age':
                self.showAgeAll()
            elif command == 'today':
                self.today()
            elif command == 'next_birthday':
                self.nextBirthday()
            elif command == 'prev_birthday':
                self.prevBirthday()
            elif command == 'delete':
                self.deleteRecord()
            elif command == "exit":
                print("Input exit")
                # ���������� ��������� ��������� � ���� ��
                self.closeDB()
                sys.exit()
            else:
                print(r"ERROR : Uncknow team/����������� �������")
    # END method Application.mainMenu()

    def help(self):
        """������ ����� ����� ������������ ��� ����������� ������� � ������ ����������"""
        print(r"=== ��������� - �������� ���� �������� ========================================")
        print(r"=== ������� ===================================================================")
        print(r"= ��������� ������������ ��������� ������� ====================================")
        print(r"= help   - ���������� ������� ������� � ������ ���������                      =")
        print(r"= new    - ������� ����� ������ � ������� ��                                  =")
        print(r"= new_pars - ������� ����� ������ ��� �� (������� ������)                     =")
        print(r"= find_name - ����� ������ '�� �����' � ����������� ��                        =")
        print(r"= find_birthday - ����� ��� ������ � �� � ��������� ����� ��� ��������        =")
        print(r"= change - �������� ������������ ������ � ������� ��                          =")
        print(r"= show   - ���������� ��� ������ � ������� ��                                 =")
        print(r"= age - ��������� �������� �������� ��� ���� ������� � ��                     =")
        print(r"= show_age - ��������� � ���������� �������� �������� ���� ������� ��         =")
        print(r"= today - ������� ������ �� �� ���� ��������, ������������ �� ������� ����    =")
        print(r"= next_birthday - ���������� ������, ��������������� ���������� ��� ��������  =")
        print(r"= prev_birthday - ���������� ������, ��������������� ����������� ��� �������� =")
        print(r"= exit   - ����� �� ���������                                                 =")
        print(r"===============================================================================")
    # END method Application.help()

    def new(self):
        """������� ����� ������ ��� �� ���� ��������"""
        sign = False  # ��������� ���������� ������, ������������ ��� ������� ���������� ����� ������
        print(r">>> ������� ��� �������� : ", end='')
        newName = input()
        newName = newName.strip(' ')
        print(r">>> ������� ������ ��� ��� ��������:")
        try:
            newDay = int(input(r">>> ���� : "))
        except ValueError:
            print(">>> INPUT ERROR! ������ ����� ��� ��������")
            return
        try:
            newMonth = int(input(r">>> ����� : "))
        except ValueError:
            print(">>> INPUT ERROR! ������ ����� ������ ��������")
            return
        try:
            newYear = int(input(r">>> ��� : "))
        except ValueError:
            print(">>> INPUT ERROR! ������ ����� ���� ��������")
            return
        temp = People(newName, newDay, newMonth, newYear)
        print(">>> ������� ����� ������ � �� : %s" % (temp))
        self.birthdays.append(temp)
    # END method Application.new()

    def dateParsing(self, line):
        """����� ������������ ��� ��������� ������, ���������� ������ ��� ��������.
        ����������� �������� �� ������������ ������� ��.��.���� / DD.MM.YYYY"""
        day = 0    # ��������� ����������, ������������ ��� ������������ ��������� �������� ���
        month = 0  # ������
        year = 0   # � ���� ��������
        listStr = line.split('.')  # ������ ������ ���� ����������� �� ������ ����� �� ����������� '.' (�����)
        lenListStr = len(listStr)  # ���������� ������� � ������ ����
        if lenListStr != 3:
            print(">>> ERROR! ������ � ������ ������ ����: �������� ��������� ������, ����������� ������!")
            return
        else:
            try:
                day = int(listStr[0])    # �������� ������ ���� ������ � ����������� ��� � ������� int()
            except ValueError:
                print(">>> ERROR: �������� ������ ��� ���� ���� (�� ����� �����)!")
                return
            try:
                month = int(listStr[1])  # �������� ������ ���� ������ � ����������� ��� � ������� int()
            except ValueError:
                print(">>> ERROR: �������� ������ ��� ���� ����� (�� ����� �����)!")
                return
            try:
                year = int(listStr[2])  # �������� ������ ���� ������ � ����������� ��� � ������� int()
            except ValueError:
                print(">>> ERROR: �������� ������ ��� ���� ����� (�� ����� �����)!")
                return
            # �������� ������ ���� �� ������������ ��������
            if 1 <= month <= 12 and 1 <= day <= 31:
                # ������ � ��������� ���������� ��������� ��������
                # print("%02d.%02d.%04d" % (day, month, year))
                Application.day = day
                Application.month = month
                Application.year = year
                return True  # ������� �������� �������

    def newParsing(self):
        """������ ����� ������������� ����������� �������� ������ ������ ��� ��������, �������� �������������.
        � ������ ����������� �������� ������� ����� ������. ���� ������������ ������ ����� ������ �
        ������������ �������, ������� �������� ���� ������ � ������� ����������������� ���������."""
        counter = 0   # ��������� ���������� ������ - ������� ���������� ������� ����� ������.
        sign = False  # ��������� ���������� - ������� ��������� ����� ������ ��� ������ �� � ��
        fullName = str()  # ��������� ���������� ��� �������� ������ <�����>
        while counter < 3:
            print("> %s ������� >" % (counter+1))
            print(">>> ������� ������ ��� ����� ������ �� � ������� <���>:<����>\n"
                  ">>> -------------------------------------------------------------------------------------------\n"
                  ">>> ���� <���> ������ ��������� ��������� ������������� ����� ��������\n"
                  ">>> �������������� ������ : '���' ���� '��� �������'. ���� <���> �� ����� ��������� ������ ':'\n"
                  ">>> ���� <����> �������� � ������� ��.��.����\n"
                  ">>> -------------------------------------------------------------------------------------------")
            line = input(">>> ")
            listStr = line.split(':')
            if len(listStr) != 2:
                print(">>> INPUT ERROR! / ������ �����! - ������� ���������� ������\n"
                      ">>> � ��� ����� ��� �������!")
                counter += 1  # ���������� �������� ���������� ����������� ��������� ������
                continue
            if self.dateParsing(listStr[1]):
                fullName = listStr[0].strip(' ')  # ��������� ������ �����
                sign = True  # ������ ������� � ���������� �������
                break
        if sign == True:
            print("> ����� ������ � �� > %s : %02d.%02d.%02d" % (fullName,
                                                                 Application.day, Application.month, Application.year))
            temp = People(fullName, Application.day, Application.month, Application.year)
            self.birthdays.append(temp)  # �������� ����� ������ � ��

    def show(self):
        """����� ������������ ��� ����������� ����������� ��.
        ����������� ������ �� ������� � ���������� ������ self.birthdays"""
        counter = len(self.birthdays)
        if len(self.birthdays) == 0:
            print(r"= ���� ������ ����� - ��� �� �������� �� ����� ������ =")
        else:
            ind = 1
            print(r"= ������� ���������� �� ���� �������� =================")
            for i in self.birthdays:
                print(">> %2d >> %s" % (ind, i))
                ind += 1
            print(r"= �������� ��� ������ �� ���� �������� ================")
    # END method Application.show()

    def find_name(self):
        """����� ������������ ��� ����������� �������� """
        res = []   # ������ ������� �������, ��������������� ������� ������
        index = 0  # ��������� ���������� - ����� ������
        count = 0
        print(r">> Find Name >> ����� ������ ��� ������� � ��")
        name=input(r">> Find Name >> ������� ��� : ")
        for i in self.birthdays:
            if i.name == name:  # � �� ������� ��������������� ������
                res.append(index)
                count += 1      # ������� ���������� �������, ��������������� ������� ������
            index += 1  # ���������� ��� ������ � ������ - ����������� ������ ��������� ������
        print(r">> Find Name >> ������� %d ������� ��������������� ������� ������" % count)
        if count > 0:  # ���� � �� ���������� ������, ��������������� �������
            print(r">> Find Name >> Result : ��������� ������")
            for i in range(count):
                print(r">> Find Name >> ������ #%2d - %s" % (res[i]+1, self.birthdays[res[i]]))
    # END method Application.find_name()
    
    def find_birthday(self):
        """����� ��� ������ ���� ��������"""
        res = [] # ������ ������� �������, ��������������� ������� ������
        index = 0  # ��������� ���������� - ����� ������
        count = 0
        print(r">> Find Birthday >> ������� ���� �������� ��� ������ �������")
        line = input(">> Find Birthday >> ").strip(' ')
        if self.dateParsing(line):
            for i in self.birthdays:
                if i.date == line:
                    res.append(index)
                    count += 1
                index += 1
            print(r">> Find Birthday >> ������� %d ������� ��������������� ������� ������" % count)
            if count > 0:  # ���� � �� ���������� ������, ��������������� �������
                print(r">> Find Birthday >> Result : ��������� ������")
                for i in range(count):
                    print(r">> Find Birthday >> ������ #%2d - %s" % (res[i]+1, self.birthdays[res[i]]))
    # END method Application.find_birthday()
    
    def change(self):
        """����� ������������ ��� �������� ������ � �� ���� ��������"""
        print(r">> Change >> ������� ����� ������, ���������� ��������� ")
        try:
            index = int(input(r">> Change >> "))
        except ValueError:
            print(r">> Change >> ERROR: Number is uncorrecr - ������� ������ ����� \n"
                  ">> Change >> ����� �������� ������ ������������� ��������.")
            return  # ���������� ������ ������� Application.change()
        if index < 0:
            print(r">> Change >> ERROR : Negative count - ������� ������������� ��������\n"
                  ">> Change >> �������� ������ ������������� �������������� ������.")
            return  # ���������� ������ ������� Application.change()
        if index > len(self.birthdays):
            print(r">> Change >> �� �������� ������ %d �������!" % len(self.birthdays))
            return  # ���������� ������ ������� Application.change()
        # ���� ������������ ���� ���������� �������� ������ ������
        print(r">> Change >> ������� �������� ������ %d : %s" % (index, self.birthdays[index - 1]))
        print(r">> Change >> ��������. ��� ������ �������������, '���' (1) ��� '���� ��������' (2)")
        choice = input(r">> Change (1/2) ? >> ")
        try:
            choice = int(choice)
        except ValueError:
            print(r">> Change >> ERROR: Command is uncorrect. �o����� ������� �������!")
            return
        # �� ���������� � ������. �������� ������ - ������� ���������� ������ People.
        if choice == 1:  # ��������� ������ �����
            line = input(r">> Change : ������� ��� >> ")
            Application.fullName = line.strip(' ')  # ������� ������ ������� � ������ � � ����� �����...
            date = self.birthdays[index-1].setName(Application.fullName)  # ������ ������� �������� ���� ��������
        elif choice == 2:  # ��������� ������ ���� ��������
            line = input(r">> Change : ������� ���� (��.��.����)>> ")
            Application.date = line.strip(' ')
            print(r">> New Date >> %s" % Application.date)
            self.dateParsing(Application.date)  # ����� ������ �������� ���� - ������� ������ ��.��.����
            # ������ �������� ������ Application.day, Application.month, Application.year - �������� ����� ��������
            # ������ ����� �������� ������� ��� ������� - ���������� ������ People, �������� ������
            self.birthdays[index-1].date = Application.date
            print(r"Application.day = %d" % Application.day)
            self.birthdays[index-1].day = Application.day
            self.birthdays[index-1].month = Application.month
            self.birthdays[index-1].year = Application.year
        else:
            print(r">> Change >> ERROR: Command input error - ������ ����� �������!")
            return
        print(r">> Change >> ����� �������� ������ %d : %s" % (index, self.birthdays[index - 1]))
    # END method Application.change()

    def deleteRecord(self):
        """����� ��� �������� ������ �� ��������� �� ���� ��������."""
        countRecords = len(self.birthdays)
        print(r">> Delete >> �������� ������ �� ��������� �� (����������� � ����������� ������)")
        print(r">> Delete >> �� �������� %d �������" % countRecords)
        print(r">> Delete >> ������� ����� ������, ���������� �������� : ", end='')
        try:
            numb = int(input())
        except ValueError:
            print(r">> Delete >> ��������� �������� �� ����� ���� ������������� � ��������� �������!")
            return
        if 0 < numb <= countRecords:
            del self.birthdays[numb-1]
        else:
            print(r">> Delete >> ��������� ����� ������ ����� ��� ����������� ���������!")
            return
        print(r">> Delete >> ������ ������� �������.")
    # END method Application.deleteRerords

    def age(self):
        """����� ������������ ��� ���������� �������� �������� - ������ ���.
        �������� ������ ������� �� ��������� ������� ����
        self.t[0] - ���, self.t[1] - �����, self.t[2] - ����"""
        for i in self.birthdays:  # ���� �������� ��������� ������ ��
            # ���������� ��������� �������� �������� ��� ������� �������� ������.
            # ��� ����� ���������� ���������� ��������� ��� �������� ������������ ������� ����: ��� ��� ��� ��� ���?
            # ����������� ������� �������� - ���� �������� � ���� ���� ��� ��� � ������� ����� ������� ����� ���������
            # �������� ���� � ����� ��������
            i.age = self.t[0] - i.year # �������������� ������ ��������, ������� ��������� ���������
            # ���������� ������������ ������� ��������: ����� ���� �������� ��� ������?
            if i.month > self.t[1]:  # ���, ���� �������� � ���� ���� ��� �� ���. ��� �� ��������.
                i.age -= 1  # ������ ���������
            elif i.month == self.t[1] :  # ���� ���� �������� � ������� ������
                if i.day > self.t[2] :   # �� �� ��� �� ��������, ��
                    i.age -= 1           # ������������ �������� �������� ������ ���
        # �� ���������� ������� ����� ����� ������������ �������� ������� �������� ��� ���� ������� � ��
        print(r">> Age >> ��������� ���������� �������� �������� ��� ���� ������� ��.")
        self.ageStatus = True
    # END method Application.age()

    def showAgeAll(self):
        """������ ����� ���������� �������� ���� ������� �� � �������������� �������� �������� ������ ���"""
        if self.ageStatus == False:
            self.age()
            self.ageStatus = True
        index = 1
        print(r">> Age >> �������� �������� ��� �����, ��������� � �� ��������� ���� ��������")
        for i in self.birthdays:
            print(">> %2d >> %s >> ������� : %2d" % (index, i.name, i.age))
            index += 1
    # END method Application.showAgeAll()

    def today(self):
        """������ ����� ������� ���������� � ������� ���� �������� ������������ �� ������� ����.
        �������� ������� ���� �������� � ���������: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        res = []  # ������ ������ ������� �������, ���� ��� �������� ��� ������� ���������� �� ������� ������
        index = 0  # ��������� ��������� ��� ������ � ��������� ������
        for i in self.birthdays:
            if i.month == self.t[1] and i.day == self.t[2]:
                res.append(index)
            index += 1
        count = len(res)
        print(r">> Today >> ����������� ����� ������� ��, ��� ������� ���� ��� �������� ���������� �� �������.")
        print(">> Today >> ������� %s �������" % (count))
        if count != 0:
            for i in range(count):
                print(">> Today >> %s" % self.birthdays[res[i]].name)
            print(r">> Today >> Finish ")
        pass
    # END method Application.today()

    def nextBirthday(self):
        """������ ����� ���� � �� ������ � ��������� ��� �������� ������������ ������� ����.
        �������� ������� ���� �������� � ���������: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        numbBirthDay = []  # ������ ������ ��� �������� ��� �� ����������� ����
        nextBirthDay = []  # ������ ������� ����, ��� ������� � ������� ���� ���� �������� ��� �� ��������
        index = 0
        for i in self.birthdays:
            numb = 0
            numbMonth = i.month
            if numbMonth == 1:  # ��� ������
                numb = i.day
            else:
                numb = i.day
                for j in range(1,numbMonth):
                    numb += Application.daysOfMonth[j]
                    # � ���������� numb ����������� ���������� ����, ��������� �� ��� �������� � ������ ����
            numbBirthDay.append(numb)
        numbToday = 0  # ����� �������� ��� ������������ ������ �������� ����
        numb = 0
        if self.t[1] == 1:  # ���� ������ ������
            numb = self.t[2]
        else:
            numb = self.t[2]
            for j in range(1, self.t[1]):
                numb += Application.daysOfMonth[j]
                # � ���������� numb ����������� ���������� ����, ��������� �� ��� �������� � ������ ����
        findNextBirthday = 0
        index = 0
        minDif = 365  # ����������� �������� ����������� �������� � ����
        for i in numbBirthDay:
            if i > numb :  # ���������� ���� ��� ��� ��������, ��������� � ������ ����, ������ ���������� ���� ������� ����
                dif = i - numb
                if dif < minDif:
                    minDif = dif
                    findNextBirthday = index
            elif i < numb :
                dif = i + (365 - numb)
                if dif < minDif:
                    minDif = dif
                    findNextBirthday = index
            index += 1
        print(r">> Next Birthday >> %s" % self.birthdays[findNextBirthday])
    # END method Application.nextBirthday()

    def prevBirthday(self):
        """������ ����� ���� � �� ������ � ��������� ��������� ��� �������� ������������ ������� ����.
        �������� ������� ���� �������� � ���������: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        numbBirthDay = []  # ������ ������ ��� �������� ��� �� ����������� ����
        prevBirthDay = []  # ������ ������� ����, ��� ������� � ������� ���� ���� �������� ��� ��������
        index = 0
        for i in self.birthdays:
            numb = 0
            numbMonth = i.month
            if numbMonth == 1:  # ��� ������
                numb = i.day
            else:
                numb = i.day
                for j in range(1,numbMonth):
                    numb += Application.daysOfMonth[j]
                    # � ���������� numb ����������� ���������� ����, ��������� �� ��� �������� � ������ ����
            numbBirthDay.append(numb)
        numbToday = 0  # ����� �������� ��� ������������ ������ �������� ����
        numb = 0
        if self.t[1] == 1:  # ���� ������ ������
            numb = self.t[2]
        else:
            numb = self.t[2]
            for j in range(1, self.t[1]):
                numb += Application.daysOfMonth[j]
                # � ���������� numb ����������� ���������� ����, ��������� �� ��� �������� � ������ ����
        findPrevBirthday = 0
        index = 0
        minDif = 365  # ����������� �������� ����������� �������� � ����
        for i in numbBirthDay:
            if i > numb :  # ���������� ���� ��� ��� ��������, ��������� � ������ ����, ������ ���������� ���� ������� ����
                dif = i - (365 - numb)
                if dif < minDif:
                    minDif = dif
                    findPrevBirthday = index
            elif i < numb :
                dif = numb - i
                if dif < minDif:
                    minDif = dif
                    findPrevBirthday = index
            index += 1
        print(r">> Previous Birthday >> %s" % self.birthdays[findPrevBirthday])
    # END method Application.prevBirthday()

    def loadDB(self):
        """����� ������������ ��� ������ ������ �� ����� �� � ������ ������ � ������ self.birthdays.
        ��� ����� �� self.fileName �������� ��� ������ ������ Application.startMenu() � ������� � ����������
        �������� ����������� �������� ���������� �����."""
        pass
    # END method Application.loadDB()

    def closeDB(self):
        """����� ������������ ��� ���������� ������ � ���� ��. ��� ���������� �� ���������� �������
        ������ ����������� ���������� � ���� �� - ����� ������ ������������ ������ ������ �������.
        ������ �� ������ self.birthdays ������������ � ���� � ������, ��������� � ��������� self.fileName."""
        self.f = open(self.fileName, mode='w', encoding='cp1251')
        # ���� ������������� ������ ������ �� ������ self.birthday, ����������� ������ �� ����������
        # ������ People
        for line in self.birthdays:
            self.f.writelines(str(line)+'\n')
        self.f.close()
    # END method Application.closeDB

# END class Application

if __name__ == "__main__":
    app = Application()
    app.run()
