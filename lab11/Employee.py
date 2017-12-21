from People import People
class Employee(People):
    def __init__(self, id=0, naim=0, status=0, project=0, zp=0, bonus=0, exStatus=0, exProject=0):
        super().__init__()
        self.id     = id
        self.naim   = naim
        self.status = status
        self.project = project
        self.zp     = zp
        self.bonus  = bonus
        self.exStatus = exStatus
        self.exProject = exProject

    def setEmployee(self, id, naim, status):
        self.id = id
        self.naim = naim
        self.status = status

    def __str__(self):
        temp = " ID работника: " + str(self.id)+ ", дата найма: " + str(self.naim) + ", статус: " +  str(self.status) + " информация по человеку:" + super().__str__()
        return temp