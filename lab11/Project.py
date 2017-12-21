from Job import Job
class Project(Job):
    def __init__(self, numb=0, prodName=0, category=0, statusProj=0, results=0, task=0):
        self.numb = numb
        self.prodName = prodName
        self.category = category
        self.statusProj = statusProj
        self.results = results
        self.task = task

    def setProject(self, prodName, category, statusProj, task):
        self.prodName = prodName
        self.category = category
        self.statusProj = statusProj
        self.task = task

    def __str__(self):
        temp = " Имя проекта: " + str(self.prodName) + ", категория: " + str(self.category) \
         + ", статус проекта: " + str(self.statusProj) + ", ЗАДАЧИ: " + str(self.task.__str__())
        return temp