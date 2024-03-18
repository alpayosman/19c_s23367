from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass
class ConcreteSquareGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise RaiseError(f"End must be greater than start")
        return [x ** 2 for x in range(start, end + 1)]
# Task 8

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise RaiseError(f"End must be greater than start")
        return [x ** 3 for x in range(start, end + 1)]

# Task 9
class RaiseError (Exception):
    pass

