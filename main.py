# Task 1

squares = [x ** 2 for x in range(1, 11)]
print(squares)


# Task 2

def generate_square(start, end):
    return [x ** 2 for x in range(start, end + 1)]



print(generate_square(1, 10))


# Task 3

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []  # Task 5 handle the smaller end value then range
        return [x**2 for x in range(start, end + 1)]


square_gen = SquareGenerator()

squares = square_gen.generate_squares(1, 10)


# Task 4

import math

square_roots = [math.sqrt(square) for square in squares]
print(square_roots)

# Task 6

from square_generator.square_generator import SquareGenerator, ConcreteSquareGenerator

square_gen1 = ConcreteSquareGenerator()
squares = square_gen1.generate_squares(1,10)
print(squares)


from square_generator.square_generator import CubicGenerator

cubic_gen = CubicGenerator()

squares = square_gen1.generate_squares(1, 10)

cubes = cubic_gen.generate_squares(1,10)

print(squares, cubes)

# Task 9
from square_generator.square_generator import RaiseError
try:
    cubic_gen = CubicGenerator()
    squares_try = square_gen.generate_squares(10, 1)
    cubes_try = cubic_gen.generate_squares(10, 1)
except RaiseError as e:
    print(e)



