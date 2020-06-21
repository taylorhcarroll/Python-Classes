import datetime


class Employee:
    def __init__(self, name, title, date):
        self.name = name
        self.job_title = title
        self.start_date = date


class Company:
    def __init__(self, name, address, ind_type):
        self.name = name
        self.address = address
        self.industry_type = ind_type
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def report(self):
        stringOutput = ''' '''
        for employee in self.employees:
            stringOutput += f'''* {employee.name}
             '''
        print(
            f'''
            {self.name} is in the {self.industry_type} industry and has the following employees:
            {stringOutput}
            ''')
        print()


keeper1 = Employee("John Billington", "Chief Keeper",
                   datetime.datetime(2020, 6, 3))
keeper2 = Employee("Jane Goodall", "Ape Research",
                   datetime.datetime(2020, 6, 9))

gameDesigner1 = Employee(
    "Shigeru Miyamoto", "Game Designer", datetime.datetime(1986, 6, 7))
gameEngineer1 = Employee("Taylor Carroll", "", datetime.datetime(1984, 5, 8))

Zoo = Company("Nashville Zoo", "123 Monkey Ave", "Research")

Nintendo = Company("Nintendo", "64 Mario Court", "Entertainment")

Zoo.add_employee(keeper1)
Zoo.add_employee(keeper2)
Nintendo.add_employee(gameDesigner1)
Nintendo.add_employee(gameEngineer1)

Zoo.report()
Nintendo.report()
