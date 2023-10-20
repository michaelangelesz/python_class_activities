# A function that accepts no arguments and is named say_hello and returns nothing; it just prints hello.
def say_hello():
    print("hello")

# A sum function that accepts two integers and returns the sum.
def sum(a, b):
    return a + b

# An average function that accepts two numbers and returns the average.
def average(a, b):
    return (a + b) / 2

# A function that accepts a first name and a last name and formats them to "{last_name}, {first_name}" (returns a string).
def format_name(first_name, last_name):
    return f"{last_name}, {first_name}"

# A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.
def create_student_info(first_name, last_name, graduation_year, student_number):
    return [first_name, last_name, graduation_year, student_number]

# A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def is_above_18(age):
    return age > 18

# A function that takes a string and prints the string in reverse (no return value).
def reverse_string(string):
    print(string[::-1])

#############################

say_hello() # this calls the function and prints "hello"


print(sum(3, 5))
# ~or~
result = sum(3, 5)
print(result)  # Output: 8


print(average(1, 3))
# ~or~
result = average(1, 3)
print(result)  # Output: 2


result = format_name("Michael", "Angelesz")
print(result)  # Output: Angelesz, Michael


result = create_student_info("Michael", "Angelesz", 2023, 123456)
print(result)  # Output: ['Michael', 'Angelesz', 2023, 123456]


result = is_above_18(20)
print(result)  # Output: True
# to return false
result = is_above_18(16)
print(result)  # Output: False


reverse_string("Hello, World!")  # Output: !dlroW ,olleH