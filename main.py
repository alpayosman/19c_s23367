# Task 1

squares = [x ** 2 for x in range(1, 11)]
print(squares)


# Task 2

def generate_square(start, end):
    return [x ** 2 for x in range(start, end + 1)]


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(generate_square(start, end))
