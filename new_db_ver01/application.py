# filename: application.py
# -*- coding: cp1251 -*-
from people import *
import os
import sys
import time
# Приложение поддерживает кодовую таблицу для отображения Кириллицы CP1251
"""Модуль содержит описание и реализацию класса Application, определяющего бизнес-логику приложения"""
class Application:
    """Данный класс определяет бизнес-логику приложения БД менеджера дней рождений"""
    # Атрибуты объекта класса - общие атрибуты для всех экземпляров класса
    fullName = str()  # Application.fullName - строковое представление имени человека в БД
    date = str()      # Application.date     - строковое представление даты рождения в БД
    day = 0           # Application.day      - день рождения
    month = 0         # Application.month    - месяц рождения
    year = 0          # Application.year     - год рождения
    daysOfMonth = [0, 31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]  # список количества дней в месяцах для не високосного года
    def __init__(self):
        """Конструктор класса Application отвечает за работу программы менеджера
        дней рождений, опеределяет атрибуты экземпляра класса и устанавливает для
        них значения по умолчанию."""
        self.fileName = None  # имя файла БД
        self.status = False   # статус программы, связанный с подключением к файлу БД
        # self.status = False означает, что файл БД не загружен либо уже выгружен
        # self.status = True означает, что файл БД загружен в память программы
        self.f = None  # ссылка на файловый объект, связанный с БД
        self.fileStatus = False  # Атрибут класса, предназначенный для выполнения проверки существования
        # указанного файла БД
        self.birthdays = []  # при создании экземпляра класса создается пустой список записей дней рождений
        self.mode = False  # Режим запуска программы: False - создать новый файл БД, True - открыть существующий файл
        self.date = None
        self.d = [r"понедельник", r"вторник", r"среда", r"четверг",
                  r"пятница", r"суббота", r"воскресенье"]
        self.m = ["" , r"января", r"февраля", r"марта", r"апреля", r"мая", r"июня",
                  r"июля", r"августа", r"сентября", r"октября", r"ноября", r"декабря"]
        self.t = time.localtime()  # получаем текущее значение даты и времени
        self.ageStatus = False  # Была ли выполнена процедура вычисления возраста людей для записей БД
    # END class constructor Application.__init__()

    def __del__(self):
        print(r">>> Работа программы завершена / The work of the program is completed.")

    def run(self):
        """Метод отвечает за реализацию бизнес-логики, то есть определяет последовательность вызова процедур"""
        self.startMenu()  # Определяем режим работы с файлом БД: 'причитать новый' или 'открыть существующий'
        self.mainMenu()   # Отобразить программное меню пользователя, связанное с циклом обработки вводимых команд
    # END method Application.run()

    def startMenu(self):
        """Данный метод класса предназначен для  организации процесса выбора режима работы с файлом БД дней рождений"""
        print(r"=== Программа - менеджер дней рождений =====================")
        print("= Сегодня: %11s %s %s %s %02d:%02d:%02d = %02d.%02d.%04d =" %
              (self.d[self.t[6]], self.t[2], self.m[self.t[1]], self.t[0],
               self.t[3], self.t[4], self.t[5],
               self.t[2], self.t[1], self.t[0]))
        print(r"============================================================")
        print(r"Создать новый файл БД дней рождений (Y/N) : ", end='')
        choice = input()
        if choice == 'Y' or choice == 'y':
            # Пользователь выбрал 'Создать' новый файл БД
            self.fileName = input(">>> Введит имя нового файла для БД : ")
            print(">>> Вы ввели : %s " % self.fileName)
        else:
            # Пользователь выбрал работу с ранее созданным и сохраненным файлом БД
            # Процедура ввода имени файла БД
            self.fileName = input(">>> Введите имя файла БД : ")
            fileStatus =  os.access(self.fileName, os.F_OK)  # проверка существования указанного файла
            if not fileStatus:  # Если невозможно открыть указанный файл - возможно, неверно указано имя файла
                print("Путь к файлу указан неверно!")
                sys.exit(1)  # Работа программы завершается досрочно с выводом диагностического сообщения
            # Процедура чтения даных из файла выполнена в формате менеджера контекста
            with open(self.fileName, mode='r', encoding='cp1251') as f:
                for line in f:
                    line = line.strip(' ')
                    print(line, end='')  # Извлекаемая из файла строка
                    # Каждая считанная строка содержит данные в формате <ИМЯ> : <ДД.ММ.ГГГГ>
                    # Прочитанные данные нужно пропарсить и занести в список self.birthdays
                    # Предполагаем, что файл содержит данный в указанном формате
                    line = line.split(':')  # line - список строк, выделенных их прочитанной строки, разделитель - ':'
                    if len(line) != 2:      # Из файла считана строка, содержащая данные в неверном формате
                        continue            # Игнорируем строку, содержащую неверные данные о имени и дне рождения
                    else:
                        Application.fullName = line[0].strip(' ')  # Считана и сформирована строка, содержащая имя человека
                        Application.date = line[1]          # Считана строка даты рождения, ее нужно пропарсить
                        self.dateParsing(Application.date)  # Вызов метода парсинга даты - разбора строки ДД.ММ.ГГГГ
                        temp = People(Application.fullName, Application.day, Application.month, Application.year)
                        self.birthdays.append(temp)  # Добавить новую запись в БД
                # END circle for - прочитаны все строки из файла БД
            # После чтения всех строк из файла в БД программы, файл будет гарантировано закрыт =)
            #self.f = open(self.fileName, mode="r", encoding="cp1251")

        self.mainMenu()
    # END method Application.startMenu()

    def mainMenu(self):
        """Отсновное меню программы, связанное с процессом обработки вводимых
        пользователем команд и данных"""
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
                # Сохранение внесенных изменений в файл БД
                self.closeDB()
                sys.exit()
            else:
                print(r"ERROR : Uncknow team/Неизвестная команда")
    # END method Application.mainMenu()

    def help(self):
        """Данный метод класс предназначен для отображения справки о работе приложения"""
        print(r"=== Программа - менеджер дней рождений ========================================")
        print(r"=== СПРАВКА ===================================================================")
        print(r"= Программа поддерживает следующие команды ====================================")
        print(r"= help   - Отобразить краткую справку о работе программы                      =")
        print(r"= new    - Создать новую запись в текущей БД                                  =")
        print(r"= new_pars - Создать новую запись для БД (Парсинг строки)                     =")
        print(r"= find_name - Найти запись 'по имени' в загруженной БД                        =")
        print(r"= find_birthday - Найти все записи в БД с указанной датой дня рождения        =")
        print(r"= change - Изменить существующую запись в текущей БД                          =")
        print(r"= show   - Отобразить все записи в текущей БД                                 =")
        print(r"= age - Вычислить значение возраста для всех записей в БД                     =")
        print(r"= show_age - Вычислить и отобразить значения возраста всех записей БД         =")
        print(r"= today - Вывести записи из БД дней рождений, приходящиеся на текущую дату    =")
        print(r"= next_birthday - Отобразить запись, соответствующую ближайшему дню рождения  =")
        print(r"= prev_birthday - Отобразить запись, соответствующую предыдущему дню рождения =")
        print(r"= exit   - Выход из программы                                                 =")
        print(r"===============================================================================")
    # END method Application.help()

    def new(self):
        """Создать новую запись для БД дней рождений"""
        sign = False  # Локальная переменная метода, используется для анализа успешности ввода данных
        print(r">>> Введите имя человека : ", end='')
        newName = input()
        newName = newName.strip(' ')
        print(r">>> Введите данные для дня рождения:")
        try:
            newDay = int(input(r">>> День : "))
        except ValueError:
            print(">>> INPUT ERROR! Ошибка ввода Дня рождения")
            return
        try:
            newMonth = int(input(r">>> Месяц : "))
        except ValueError:
            print(">>> INPUT ERROR! Ошибка ввода Месяца рождения")
            return
        try:
            newYear = int(input(r">>> Год : "))
        except ValueError:
            print(">>> INPUT ERROR! Ошибка ввода Года рождения")
            return
        temp = People(newName, newDay, newMonth, newYear)
        print(">>> Создана новая запись в БД : %s" % (temp))
        self.birthdays.append(temp)
    # END method Application.new()

    def dateParsing(self, line):
        """Метод предназначен для обработки строки, содержащей данные дня рождения.
        Выполняется проверка на соответствие формату ДД.ММ.ГГГГ / DD.MM.YYYY"""
        day = 0    # Локальные переменные, используются для формирования числового значения дня
        month = 0  # меняца
        year = 0   # и года рождения
        listStr = line.split('.')  # строка записи даты разбивается на список строк по разделителю '.' (точка)
        lenListStr = len(listStr)  # количество записей в строке даты
        if lenListStr != 3:
            print(">>> ERROR! Ошибка в строке записи даты: неверное количетво блоков, разделенных точкой!")
            return
        else:
            try:
                day = int(listStr[0])    # Выделяем первый блок списка и преобразуем его к формату int()
            except ValueError:
                print(">>> ERROR: Неверный формат для поля ДЕНЬ (не целое число)!")
                return
            try:
                month = int(listStr[1])  # Выделяем второй блок списка и преобразуем его к формату int()
            except ValueError:
                print(">>> ERROR: Неверный формат для поля МЕСЯЦ (не целое число)!")
                return
            try:
                year = int(listStr[2])  # Выделяем третий блок списка и преобразуем его к формату int()
            except ValueError:
                print(">>> ERROR: Неверный формат для поля МЕСЯЦ (не целое число)!")
                return
            # Проверка данных даты на корректность значения
            if 1 <= month <= 12 and 1 <= day <= 31:
                # Данные в логически допустимом диапазоне значений
                # print("%02d.%02d.%04d" % (day, month, year))
                Application.day = day
                Application.month = month
                Application.year = year
                return True  # Парсинг завершен успешно

    def newParsing(self):
        """Данный метод демонстрирует возможности парсинга строки данных дня рождения, вводимых пользователем.
        В методе реализована проверка попыток ввода данных. Если пользователь трижды введт данные в
        неправильном формате, функция завершит свою работу с выводом соответствующеего сообщения."""
        counter = 0   # Локальная переменная метода - счетчик количества попыток ввода данных.
        sign = False  # Локальная переменная - признак успешного ввода данных для записи их в БД
        fullName = str()  # Локальная переменная для хранения данных <Имени>
        while counter < 3:
            print("> %s попытка >" % (counter+1))
            print(">>> Введите данные для новой записи БД в формате <ИМЯ>:<ДАТА>\n"
                  ">>> -------------------------------------------------------------------------------------------\n"
                  ">>> Поле <ИМЯ> должно содержать строковое представление имени человека\n"
                  ">>> Поддерживаемый формат : 'ИМЯ' либо 'ИМЯ ФАМИЛИЯ'. Поле <ИМЯ> не может содержать символ ':'\n"
                  ">>> Поле <ДАТА> задается в формате ДД.ММ.ГГГГ\n"
                  ">>> -------------------------------------------------------------------------------------------")
            line = input(">>> ")
            listStr = line.split(':')
            if len(listStr) != 2:
                print(">>> INPUT ERROR! / Ошибка ввода! - Введите корректные данные\n"
                      ">>> У Вас всего три попытки!")
                counter += 1  # Увеличение счетчика количества неправильно введенных данных
                continue
            if self.dateParsing(listStr[1]):
                fullName = listStr[0].strip(' ')  # введенные данные имени
                sign = True  # Данные введены в правильном формате
                break
        if sign == True:
            print("> Новая запись в БД > %s : %02d.%02d.%02d" % (fullName,
                                                                 Application.day, Application.month, Application.year))
            temp = People(fullName, Application.day, Application.month, Application.year)
            self.birthdays.append(temp)  # Добавить новую запись в БД

    def show(self):
        """Метод предназначен для отображения содержимого БД.
        Программные данные БД связаны с содержимым списка self.birthdays"""
        counter = len(self.birthdays)
        if len(self.birthdays) == 0:
            print(r"= База данных пуста - она не содержит ни одной записи =")
        else:
            ind = 1
            print(r"= Текущее содержимое БД дней рождений =================")
            for i in self.birthdays:
                print(">> %2d >> %s" % (ind, i))
                ind += 1
            print(r"= Выведены все записи БД дней рождений ================")
    # END method Application.show()

    def find_name(self):
        """Метод предназначен для организации процесса """
        res = []   # Список номеров записей, удовлетворяющих условию поиска
        index = 0  # Локальная переменная - Номер записи
        count = 0
        print(r">> Find Name >> Поиск данных дня человка в БД")
        name=input(r">> Find Name >> Введите имя : ")
        for i in self.birthdays:
            if i.name == name:  # В БД найдета соответствующая запись
                res.append(index)
                count += 1      # подсчет количества записей, соответствующих условию поиска
            index += 1  # перебираем все записи с вписке - уваличиваем номера элементов списка
        print(r">> Find Name >> Найдено %d записей удовлетворяющих условию поиска" % count)
        if count > 0:  # Если в БД содержатся записи, удовлетворяющие условию
            print(r">> Find Name >> Result : Результат поиска")
            for i in range(count):
                print(r">> Find Name >> Запись #%2d - %s" % (res[i]+1, self.birthdays[res[i]]))
    # END method Application.find_name()
    
    def find_birthday(self):
        """Метод для поиска дней рождений"""
        res = [] # Список номеров записей, удовлетворяющих условию поиска
        index = 0  # Локальная переменная - Номер записи
        count = 0
        print(r">> Find Birthday >> Введите день рождения для поиска записей")
        line = input(">> Find Birthday >> ").strip(' ')
        if self.dateParsing(line):
            for i in self.birthdays:
                if i.date == line:
                    res.append(index)
                    count += 1
                index += 1
            print(r">> Find Birthday >> Найдено %d записей удовлетворяющих условию поиска" % count)
            if count > 0:  # Если в БД содержатся записи, удовлетворяющие условию
                print(r">> Find Birthday >> Result : Результат поиска")
                for i in range(count):
                    print(r">> Find Birthday >> Запись #%2d - %s" % (res[i]+1, self.birthdays[res[i]]))
    # END method Application.find_birthday()
    
    def change(self):
        """Метод предназначен для внесения данных в БД дней рождений"""
        print(r">> Change >> Введите номер записи, подлежащей изменению ")
        try:
            index = int(input(r">> Change >> "))
        except ValueError:
            print(r">> Change >> ERROR: Number is uncorrecr - Неверно указан номер \n"
                  ">> Change >> Может вводится только целочисленное значение.")
            return  # Прерывание работы функции Application.change()
        if index < 0:
            print(r">> Change >> ERROR : Negative count - Введено отрицательное значение\n"
                  ">> Change >> Вводится только положительное значениеномера записи.")
            return  # Прерывание работы функции Application.change()
        if index > len(self.birthdays):
            print(r">> Change >> БД содержит только %d записей!" % len(self.birthdays))
            return  # Прерывание работы функции Application.change()
        # Если пользователь ввел правильное значение номера записи
        print(r">> Change >> Текущее значение записи %d : %s" % (index, self.birthdays[index - 1]))
        print(r">> Change >> Выберете. что именно редактировать, 'Имя' (1) или 'Дату рождения' (2)")
        choice = input(r">> Change (1/2) ? >> ")
        try:
            choice = int(choice)
        except ValueError:
            print(r">> Change >> ERROR: Command is uncorrect. Кoманда указана неверно!")
            return
        # БД содержится в списке. Элементы списка - объекты экземпляры класса People.
        if choice == 1:  # Изменение данных имени
            line = input(r">> Change : Введите имя >> ")
            Application.fullName = line.strip(' ')  # Удалить лишние пробелы в начале и в конце имени...
            date = self.birthdays[index-1].setName(Application.fullName)  # читаем текущее значение даты рождения
        elif choice == 2:  # Изменение данных даты рождения
            line = input(r">> Change : Введите дату (ДД.ММ.ГГГГ)>> ")
            Application.date = line.strip(' ')
            print(r">> New Date >> %s" % Application.date)
            self.dateParsing(Application.date)  # Вызов метода парсинга даты - разбора строки ДД.ММ.ГГГГ
            # Теперь атрибуты класса Application.day, Application.month, Application.year - содержат новые значения
            # Запись новых значений атрибут для объекта - экземпляра класса People, элемента списка
            self.birthdays[index-1].date = Application.date
            print(r"Application.day = %d" % Application.day)
            self.birthdays[index-1].day = Application.day
            self.birthdays[index-1].month = Application.month
            self.birthdays[index-1].year = Application.year
        else:
            print(r">> Change >> ERROR: Command input error - Ошибка ввода команды!")
            return
        print(r">> Change >> Новое значение записи %d : %s" % (index, self.birthdays[index - 1]))
    # END method Application.change()

    def deleteRecord(self):
        """Метод для удаления записи из локальной БД дней рождений."""
        countRecords = len(self.birthdays)
        print(r">> Delete >> Удаление записи из локальной БД (загруженной в оперативную память)")
        print(r">> Delete >> БД содержит %d записей" % countRecords)
        print(r">> Delete >> Введите номер записи, подлежащей удалению : ", end='')
        try:
            numb = int(input())
        except ValueError:
            print(r">> Delete >> Введенное значение не может быть преобразовано к числовому формату!")
            return
        if 0 < numb <= countRecords:
            del self.birthdays[numb-1]
        else:
            print(r">> Delete >> Введенный номер записи лежит вне допустимого диапазона!")
            return
        print(r">> Delete >> Запись успешно удалена.")
    # END method Application.deleteRerords

    def age(self):
        """Метод предназначен для вычисления значения возраста - полных лет.
        Атрибуты класса связаны со значением текущей даты
        self.t[0] - год, self.t[1] - месяц, self.t[2] - день"""
        for i in self.birthdays:  # Цикл перебора элементов списка БД
            # Необходимо вычислить значение возраста для каждого элемента списка.
            # Для этого необходимо определить положение дня рождения относительно текущей даты: уже был иле еще нет?
            # Формируется нулевая гипотеза - день рождения в этом году уже был и возраст равен разнице между значением
            # текущего года и годом рождения
            i.age = self.t[0] - i.year # предарительная оценка возраста, которая потребует уточнения
            # Попытаемся опровергнуть нулевую гипотезу: месяц даты рождения уже прошел?
            if i.month > self.t[1]:  # Нет, день рождения в этом году еще не был. Год не завершен.
                i.age -= 1  # Вносим коррекцию
            elif i.month == self.t[1] :  # Если день рождения в текущем месяце
                if i.day > self.t[2] :   # Но он еще не наступил, то
                    i.age -= 1           # корректируем значение возраста полных лет
        # По завершению данного цикла будут сформированы значения величны возраста для всех записей в БД
        print(r">> Age >> Выполнено вычисление значения возраста для всех записей БД.")
        self.ageStatus = True
    # END method Application.age()

    def showAgeAll(self):
        """Данный метод отображает значения всех записей БД и соответстующие значения возраста полных лет"""
        if self.ageStatus == False:
            self.age()
            self.ageStatus = True
        index = 1
        print(r">> Age >> Значения возраста для людей, внесенных в БД менеджера дней рождений")
        for i in self.birthdays:
            print(">> %2d >> %s >> Возраст : %2d" % (index, i.name, i.age))
            index += 1
    # END method Application.showAgeAll()

    def today(self):
        """Данный метод выводит информацию о записях дней рождения приходящихся на текущую дату.
        Значения текущей даты хранятся в атрибутах: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        res = []  # пустой список номеров записей, дата дня рождения для которых приходится на текущий момент
        index = 0  # Локальная перемнная для работы с индексами списка
        for i in self.birthdays:
            if i.month == self.t[1] and i.day == self.t[2]:
                res.append(index)
            index += 1
        count = len(res)
        print(r">> Today >> Выполняется поиск записей БД, для которых дата дня рождения приходится на сегодня.")
        print(">> Today >> Найдено %s записей" % (count))
        if count != 0:
            for i in range(count):
                print(">> Today >> %s" % self.birthdays[res[i]].name)
            print(r">> Today >> Finish ")
        pass
    # END method Application.today()

    def nextBirthday(self):
        """Данный метод ищет в БД запись о ближайшем дне рождения относительно текущей даты.
        Значения текущей даты хранятся в атрибутах: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        numbBirthDay = []  # список номера дня рождения для не високосного года
        nextBirthDay = []  # список номеров даты, для которых в текущем году день рождения еще не наступил
        index = 0
        for i in self.birthdays:
            numb = 0
            numbMonth = i.month
            if numbMonth == 1:  # это январь
                numb = i.day
            else:
                numb = i.day
                for j in range(1,numbMonth):
                    numb += Application.daysOfMonth[j]
                    # В переменной numb формируется количество дней, прошедших до дня рождения с начала года
            numbBirthDay.append(numb)
        numbToday = 0  # Номер текущего дня относительно начала текущего года
        numb = 0
        if self.t[1] == 1:  # если сейчас январь
            numb = self.t[2]
        else:
            numb = self.t[2]
            for j in range(1, self.t[1]):
                numb += Application.daysOfMonth[j]
                # В переменной numb формируется количество дней, прошедших до дня рождения с начала года
        findNextBirthday = 0
        index = 0
        minDif = 365  # формируемое значение минимальной разности в днях
        for i in numbBirthDay:
            if i > numb :  # количество дней для дня рождения, прошедших с начала года, больше количества дней текущей даты
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
        """Данный метод ищет в БД запись о последнем прошедшем дне рождения относительно текущей даты.
        Значения текущей даты хранятся в атрибутах: self.t[0] - Year, self.t[1] - Month self.t[2] - Day."""
        numbBirthDay = []  # список номера дня рождения для не високосного года
        prevBirthDay = []  # список номеров даты, для которых в текущем году день рождения уже наступил
        index = 0
        for i in self.birthdays:
            numb = 0
            numbMonth = i.month
            if numbMonth == 1:  # это январь
                numb = i.day
            else:
                numb = i.day
                for j in range(1,numbMonth):
                    numb += Application.daysOfMonth[j]
                    # В переменной numb формируется количество дней, прошедших до дня рождения с начала года
            numbBirthDay.append(numb)
        numbToday = 0  # Номер текущего дня относительно начала текущего года
        numb = 0
        if self.t[1] == 1:  # если сейчас январь
            numb = self.t[2]
        else:
            numb = self.t[2]
            for j in range(1, self.t[1]):
                numb += Application.daysOfMonth[j]
                # В переменной numb формируется количество дней, прошедших до дня рождения с начала года
        findPrevBirthday = 0
        index = 0
        minDif = 365  # формируемое значение минимальной разности в днях
        for i in numbBirthDay:
            if i > numb :  # количество дней для дня рождения, прошедших с начала года, больше количества дней текущей даты
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
        """Метод предназначен для чтения данных из файла БД и записи данных в список self.birthdays.
        Имя файла БД self.fileName задается при вызове метода Application.startMenu() в котором и выолняется
        проверка возможности открытия указанного файла."""
        pass
    # END method Application.loadDB()

    def closeDB(self):
        """Метод предназначен для сохранения данных в файл БД. При сохранении БД происходит процесс
        записи обновленной информации в файл БД - новые данные записываются поверх старых записей.
        Данные из списка self.birthdays записываются в файл с именем, связанным с атрибутом self.fileName."""
        self.f = open(self.fileName, mode='w', encoding='cp1251')
        # Цикл поэлементного чтения данных из списка self.birthday, содержащего ссылки на экземпляры
        # класса People
        for line in self.birthdays:
            self.f.writelines(str(line)+'\n')
        self.f.close()
    # END method Application.closeDB

# END class Application

if __name__ == "__main__":
    app = Application()
    app.run()
