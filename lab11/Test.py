from Employee import Employee
from Job import Job
from Project import Project

def test():
    employee1 = Employee()
    employee1.setPeople("Pavel", 27.06, 21)
    employee1.setEmployee(65743821, 1.11, "programmer")

    employee2 = Employee()
    employee2.setPeople("Anton", 11.11, 25)
    employee2.setEmployee(999999, 3.11, "manager")

    task1 = Job()
    task1.setJob("сложная задача", employee1, "удачи МЭН")

    task2 = Job()
    task2.setJob("лёгкая задача", employee2, "не облажайся")

    project = Project()
    project.setProject("INTEL8080", "commercial", "active", [task1.__str__(), task2.__str__()])
    file = open("test.txt", "w")
    file.write(project.__str__())
    print(project.__str__())

test()