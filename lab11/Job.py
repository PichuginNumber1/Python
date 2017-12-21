from Employee import Employee
class Job(Employee):
    def __init__(self, dataTime=0, planData=0, task=0, employee=0, message=0):
        self.dataTime = dataTime
        self.planData = planData
        self.task = task
        self.employee = employee
        self.message = message

    def setJob(self, task, employee, message):
        self.task = task
        self.employee = employee
        self.message = message

    def __str__(self):
        temp = " Конкретное задание: " + str(self.task) + ", работник на задаче: " + str(self.employee.__str__()) + ", комментарий: " +  str(self.message)
        return temp