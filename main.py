# Task 1

squares = [x ** 2 for x in range(1, 11)]
print(squares)


# Task 2

def generate_square(start, end):
    return [x ** 2 for x in range(start, end + 1)]


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(generate_square(start, end))


# Task 3

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return [] # Task 5 handle the smaller end value then range
        return [x**2 for x in range(start, end + 1)]


square_gen = SquareGenerator()

squares = square_gen.generate_squares(1, 10)
print(squares)

# Task 4

import math

square_roots = [math.sqrt(square) for square in squares]
print(square_roots)

# Task 6

from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
squares = square_gen.generate_the_squares(1,10)
print(squares)


#Task 8
class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):

        if end < start:
            return []
        return [x ** 3 for x in range(start, end + 1)]


square_gen = SquareGenerator()
cubic_gen = CubicGenerator()


squares = square_gen.generate_the_squares(1, 10)


cubes = cubic_gen.generate_cubes(1, 10)

print(squares, cubes)