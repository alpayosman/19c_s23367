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
