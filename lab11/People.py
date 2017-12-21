class People:
    def __init__(self, name=0, HB=0, age=0, country=0,
                 specialty=0, job=0, income=0, INN=0,
                    pension=0, OMS=0):
        self.name = name
        self.HB = HB
        self.age = age
        self.country = country
        self.specialty = specialty
        self.job = job
        self.income = income
        self.INN = INN
        self.pension = pension
        self.OMS = OMS

    def setPeople(self, name, HB, age):
        self.name = name
        self.HB = HB
        self.age = age

    def __str__(self):
        temp = " Имя человека: " + str(self.name) + ", дата рождения: " + str(self.HB) + ", возраст: " + str(self.age)
        return temp