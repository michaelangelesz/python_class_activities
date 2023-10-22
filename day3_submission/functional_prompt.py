# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
def flatten_and_sort(array):
    arr = []
    for i in array:
        if type(i) == list:
            arr += flatten_and_sort(i)
        else:
            arr.append(i)

    return sorted(arr)

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
The flatten_and_sort() function ensures data immutability by not modifying the input array directly. Instead, it creates a new list arr and appends the elements of the input array to it. This ensures that the input array remains unchanged.

Is this solution a pure function? Why or why not?
This solution is a pure function because it does not have any side effects and always returns the same output for a given input. It does not modify any external state or rely on any external state.

Is this solution a higher order function? Why or why not?
This solution is not a higher order function because it does not take any functions as arguments or return any functions as output.

Would it have been easier to solve this problem using a different programming style?
It may have been easier to solve this problem using a different programming style, such as object-oriented programming or procedural programming. However, functional programming is a good fit for this problem because it involves transforming a list of data into a new list of data, which is a common use case for functional programming.

Why in particular is functional programming a helpful paradigm when solving this problem?
Functional programming is a helpful paradigm when solving this problem because it emphasizes immutability and pure functions, which can help to reduce bugs and make the code easier to reason about. Additionally, functional programming provides powerful tools for working with lists and other collections, such as map, filter, and reduce, which can be used to transform data in a concise and expressive way.
'''


# test cases
print(flatten_and_sort([]))  # Output: []
print(flatten_and_sort([[], [1]]))  # Output: [1]
print(flatten_and_sort([[], [], [], [2], [], [1]]))  # Output: [1, 2]
print(flatten_and_sort([1, 3, 5, 7, 9]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([9, 7, 5, 3, 1]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([[1], [3], [5], [7], [9]]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([[9], [7], [5], [3], [1]]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([[1, 3, 5], [7, 9]]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([[9, 7], [5, 3, 1]]))  # Output: [1, 3, 5, 7, 9]
print(flatten_and_sort([[1, 3, 5], [7, 9], [11, 13]]))  # Output: [1, 3, 5, 7, 9, 11, 13]
print(flatten_and_sort([[5, 7, 9], [11, 13], [1, 3]]))  # Output: [1, 3, 5, 7, 9, 11, 13]