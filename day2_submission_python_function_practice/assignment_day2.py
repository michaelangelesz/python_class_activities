# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(l):
    result = 1
    for i in l:
        result *= i
    return result


# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    result = ""
    for i in range(len(s)):
        result += s[len(s) - i - 1]
    return result


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)



# max_num() test cases
print(max_num(1, 2, 3))  # Output: 3
print(max_num(5, 3, 1))  # Output: 5
print(max_num(-1, -2, -3))  # Output: -1

# mult_list() test cases
print(mult_list([1, 2, 3]))  # Output: 6
print(mult_list([5, 3, 1]))  # Output: 15
print(mult_list([-1, -2, -3]))  # Output: -6
print(mult_list([1, 2, 3, 4]))  # Output: 24
print(mult_list([5, 10, 2]))  # Output: 100
print(mult_list([-1, 2, -3, 4]))  # Output: 24

# rev_string() test cases
print(rev_string("hello"))  # Output: olleh
print(rev_string("world"))  # Output: dlrow
print(rev_string("python"))  # Output: nohtyp
print(rev_string("aibophobia"))  # Output: aibophobia 

# num_within() test cases
print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5))  # Output: False
print(num_within(10, 10, 10))  # Output: True
print(num_within(10, 1, 10))  # Output: True
print(num_within(10, 1, 9))  # Output: False

# pascal() test cases
pascal(5)
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
pascal(10)
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1
pascal(0)
# Output: invalid number of rows
pascal(-1)
# Output: invalid number of rows
