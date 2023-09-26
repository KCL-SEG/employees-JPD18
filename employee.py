"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    """Base class for all employees."""
    def __init__(self, name):
        self.name = name
        self.compensations = []

    def add_compensation(self, compensation):
        """Add a compensation scheme to the employee."""
        self.compensations.append(compensation)

    def get_pay(self):
        """Calculate and return the total pay for the employee."""
        return sum(compensation.calculate() for compensation in self.compensations)

    def __str__(self):
        descriptions = [str(compensation) for compensation in self.compensations]
        return f"{self.name} {' '.join(descriptions)}. Their total pay is {self.get_pay()}."

class Salary:
    """Salary-based compensation."""
    def __init__(self, annual_salary):
        self.annual_salary = annual_salary

    def calculate(self):
        """Return the annual salary."""
        return self.annual_salary

    def __str__(self):
        return f"works on a monthly salary of {self.calculate()}"

class Wage:
    """Wage-based compensation."""
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate(self):
        """Return the total wage based on hours worked."""
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

class BonusCommission:
    """Bonus Commission-based compensation."""
    def __init__(self, commission_amount):
        self.commission_amount = commission_amount

    def calculate(self):
        """Return the commission amount."""
        return self.commission_amount

    def __str__(self):
        return f"and receives a bonus commission of {self.commission_amount}"

class Commission:
    """Commission based on completed tasks."""
    def __init__(self, commission_per_task, num_tasks):
        self.commission_per_task = commission_per_task
        self.num_tasks = num_tasks

    def calculate(self):
        """Return the commission based on number of tasks."""
        return self.commission_per_task * self.num_tasks

    def __str__(self):
        return f"and receives a commission for {self.num_tasks} contract(s) at {self.commission_per_task}/contract"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.add_compensation(Salary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.add_compensation(Wage(25,100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.add_compensation(Salary(3000))
renee.add_compensation(Commission(200,4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.add_compensation(Wage(25,150))
jan.add_compensation(Commission(220,3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.add_compensation(Salary(2000))
robbie.add_compensation(BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.add_compensation(Wage(30,120))
ariel.add_compensation(BonusCommission(600))


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
