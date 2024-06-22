salary = int(input("Enter Salary Amount: "))


class SalaryNotInRangeError1(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary Not In(5000,15000) range"):
        self.salary = salary
        self.message = "Salary is " + str(self.salary) + " " + message
        super().__init__(self.message)


if not 5000 < salary < 15000:
    raise SalaryNotInRangeError1(salary)

# class SalaryNotInRangeError2(Exception):
#     def __init__(self,message="Salary Not In(5000,15000) range"):
#         super().__init__(message)


# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError2
