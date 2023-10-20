# Please complete the following functions.

# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for a in args:
        print(a)

alias_arb_args = arb_args

alias_arb_args(1, 2, 3, "hello", [4, 5, 6])

arb_args(1, 2, 3, "hello", [4, 5, 6])


# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(a, b):
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    print(add(a, b) + multiply(a, b))

inner_func(2, 3)


# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

lunch_lady("John", "Pizza")
lunch_lady("John")


# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(a, b):
    return a + b, a * b

result = sum_n_product(2, 3)
print(result)


# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args


# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    print(sum(args) / len(args))

arb_mean(1, 2, 3, 4, 5)


# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    longest = ""
    for a in args:
        if len(a) > len(longest):
            longest = a
    return longest

result = arb_longest_string("hello", "world", "python", "programming")
print(result)