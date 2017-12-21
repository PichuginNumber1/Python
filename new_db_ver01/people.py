# filename: people.py
"""Модуль для представления класса People"""
class People:
    """Класс для представления информации о человека в БД"""
    def __init__(self, name, day, month, year):
        """Перегруженный конструктор по умолчанию класса People"""
        self.name = name  # строка - имя человека
        # Атрибуты - данные для рождения
        self.day = day
        self.month = month
        self.year = year
        # строка - день рождения - birthday в формате даты DD:MM:YYYY
        self.date = "%02d.%02d.%04d" % (self.day, self.month, self.year)
        self.age = None   # число - возраст полных лет
    # END class constructor People.__init__()

    def __str__(self):
        """toString - метод для преобразования экземпляра класса в строку - str()"""
        description = str()  # пустая строка для формирования результата
        description = "%s : %s" % (self.name, self.date)
        return description  # строковое представление данных экземпляра класса People
    # END method People.__str__()

    def setName(self, name):
        """Метод для задания значения атрибута name экземпляра класс People"""
        self.name = name
    # END method People.setName()

    def getName(self):
        """Метод возвращает значение атрибута экземпляра класса People.name"""
        return self.name
    # END method People.getName()

    def setDate(self, date):
        """Метод для задания значения атрибута date экземпляра класса People"""
        self.date = date
    # END method People.setDate()

    def getDate(self):
        """Метод возвращает значение даты дня рождения человека, связанного с экземпялром класса People"""
        return self.date
    # END method People.getDate()

    def setAge(self):
        """Метод для формирования значения возраста человека в годах относительно текущей даты"""
        age = 0
    # END method People.setAge()

    def getAge(self):
        """Метод возвращает значение возраста человека - количество полных лет"""
        return self.age
    # END method People.getAge()
# END class People
if __name__ == "__main__":
    # Если  данный модуль является главным файлом проекта...
    Bob = People("Bob", 2, 1, 2017)
    print(Bob)