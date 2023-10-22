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


# test the say_hello function
say_hello() # this calls the function and prints "hello"


# test the sum function
print(sum(3, 5))
# ~or~
result = sum(3, 5)
print(result)  # Output: 8


# test the average function
print(average(1, 3))
# ~or~
result = average(1, 3)
print(result)  # Output: 2


# test the format_name function
print(format_name("Michael", "Angelesz"))  # Output: Angelesz, Michael
# ~or~
result = format_name("Michael", "Angelesz")
print(result)  # Output: Angelesz, Michael


# test the create_student_info function
print(create_student_info("Michael", "Angelesz", 2023, 123456))
# ~or~
result = create_student_info("Michael", "Angelesz", 2023, 123456)
print(result)  # Output: ['Michael', 'Angelesz', 2023, 123456]


# test the is_above_18 function
print(is_above_18(20)) # Output: True
print(is_above_18(15)) # Output: False
# ~or~
result = is_above_18(20)
print(result)  # Output: True
# to return false
result = is_above_18(16)
print(result)  # Output: False


# test the reverse_string function
reverse_string("Hello, World!")  # Output: !dlroW ,olleH