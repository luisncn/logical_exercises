"""
This class has the functionality through 4 methods of executing the main
mathematical operations, addition, subtraction, multiplication and division,
in addition to that it validates the data entered.
"""


class Calculator:
    def __init__(self):
        print("Calculator is running...")

    @staticmethod
    def validator(name_method, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"{name_method}: Solo debe contener números")

        if len(args) < 2:
            raise ValueError(
                f"{name_method}: Requiere al menos dos argumentos")

    def addition(self, *args):
        self.validator('addition', *args)
        total = sum(args)
        return total

    def subtract(self, *args):
        self.validator('subtract', *args)
        result = args[0]
        result -= sum(args[1:])
        return result

    def multiplication(self, *args):
        self.validator('multiplication', *args)
        total = 1
        for multiply in args:
            total = total * multiply
        return total

    def division(self, *args):
        self.validator('division', *args)
        if 0 in args:
            raise ValueError("División por cero no está permitida")
        result = args[0]
        for arg in args[1:]:
            result /= arg
        return result


# Operations
my_calculator = Calculator()
addition = my_calculator.addition(23, 33, 22, 22, 123)
subtraction = my_calculator.subtract(10, 23, 23, 112)
multiplication = my_calculator.multiplication(12, 23, 12, 33)
division = my_calculator.division(10, 5, 12)

print(
    f"My addition is: {addition}\n"
    f"My substraction is: {subtraction}\n"
    f"My multiplication is: {multiplication}\n"
    f"My division is: {division}\n"
)
