class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeDatabase:
    def _init_(self, employees):
        self.employees = employees

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def print_employees(self):
        for emp in self.employees:
            print(emp)


if __name__ == "_main_":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    emp_database = EmployeeDatabase(employees)

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input())

    if choice == 1:
        emp_database.sort_by_age()
    elif choice == 2:
        emp_database.sort_by_name()
    elif choice == 3:
        emp_database.sort_by_salary()
    else:
        print("Invalid choice")

    emp_database.print_employees()