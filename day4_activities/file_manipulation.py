'''
Error Handling

Your task for this activity is to complete the program by gracefully handling any errors that might come your way. There are many ways to do this, but for this activity you will be creating a class to manipulate files, called FileManipulator. To successfully create this class, complete the following steps:

  1. Create the FileManipulator class and implement the constructor. The constructor should accept the name of a file to read in and should continually prompt for input if the name given causes an error. Make sure that you give an informative message if an error is raised.

  2. Implement the reverse() function. This function should accept the name of a file to write to and should write each line of the original file to this new file. However, in the new file, although the line order will be the same, the string that makes each line will be reversed. So "cheese" will become "eseehc". Be careful not to add an extra newline character at the beginning of the file. Make sure that errors are handled elegantly, and appropriate error messages are given.

GIVEN START CODE:
https://replit.com/@SD-Team/Python-1042#main.py

# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''


class FileManipulator:
  def __init__(self, fileName):
    self.contents = None
    while self.contents == None:
      try:
        myfile = open(fileName, 'r') # Open a file for 
        self.contents = myfile.readlines() # Read in the content by line.
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e), e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
      
  def reverse(self,fileName):
    while True:
      try:
        myfile = open(fileName, 'w') # Open a file for writing
        revContent = [x.strip()[::-1] for x in self.contents]
        for i in range(len(revContent)):
          if i == (len(revContent)-1):
            myfile.write(revContent[i])
          else:
            myfile.write(revContent[i] + '\n') # write desired output to file
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e),e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
        break
  
  #bonus
  def upper(self,fileName):
    while True:
      try:
        myfile = open(fileName, 'w') # Open a file for writing
        upperContent = [x.strip().upper() for x in self.contents]
        for i in range(len(upperContent)):
          if i == (len(upperContent)-1):
            myfile.write(upperContent[i])
          else:
            myfile.write(upperContent[i] + '\n') # write desired output to file
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e),e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
        break
      
  def lower(self,fileName):
    while True:
      try:
        myfile = open(fileName, 'w') # Open a file for writing
        lowerContent = [x.strip().lower() for x in self.contents]
        for i in range(len(lowerContent)):
          if i == (len(lowerContent)-1):
            myfile.write(lowerContent[i])
          else:
            myfile.write(lowerContent[i] + '\n') # write desired output to file
      except (FileNotFoundError, TypeError, OSError) as e:
        print(type(e),e)
        fileName = input("Please enter a valid file name: ")
      else:
        myfile.close()
        break
        

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
f.upper("tmp3.txt")
f.lower("tmp4.txt")

f = FileManipulator("file_2_manipulate.txt")
print(f.contents)
f.reverse("file_2_manipulate2.txt")
f.upper("file_2_manipulate3.txt")