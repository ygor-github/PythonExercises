class Employee:
    def __init__(self, nome, email):
        self.name = nome
        self.email = email
        self.hours = {}
        self.hourly_rate = {}

    def hours_record(self, month, hours):
        if month not in self.hours:
            self.hours[month] = hours

    def hourly_salary_record(self, month, value):
        if month not in self.hourly_rate:
            self.hourly_rate[month] = value

    def calculate_salary(self, month):
        if month not in self.hours or month not in self.hourly_rate:
            print('"Nonexistent month"')
        else:
            return self.hours[month] * self.hourly_rate[month]

    def __repr__(self):
        return f'Employee: {self.name}, \nEmail: {self.email}, \nHours/Month: {self.hours}, \nSalary/Hour: {self.hourly_rate}'

