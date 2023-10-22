# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"


# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2


# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def flame_jet(self, podracer):
        podracer.condition = "trashed"


'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

This solution demonstrates three of the four pillars of OOP:

Encapsulation: The Podracer, AnakinsPod, and SebulbasPod classes encapsulate data and behavior related to podracers. Each class has its own set of attributes and methods that are specific to that class.

Inheritance: The AnakinsPod and SebulbasPod classes inherit from the Podracer class, which allows them to reuse the attributes and methods defined in the Podracer class. This helps to reduce code duplication and makes the code easier to maintain.

Polymorphism: The AnakinsPod and SebulbasPod classes have their own unique methods (boost and flame_jet, respectively) that are not defined in the Podracer class. However, because they inherit from the Podracer class, they can be used in the same way as Podracer objects. This allows for greater flexibility and extensibility in the code.
'''

'''
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

It may have been easier to implement a solution to this problem using a different coding style, such as procedural programming. However, OOP provides a number of benefits, such as encapsulation, inheritance, and polymorphism, that can make the code more modular, reusable, and easier to maintain.
'''

'''
How in particular did Object Oriented Programming assist in the solving of this problem?

Object-oriented programming assisted in the solving of this problem by allowing us to define classes that encapsulate data and behavior related to podracers. By using inheritance, we were able to reuse code from the Podracer class in the AnakinsPod and SebulbasPod classes, which helped to reduce code duplication and make the code easier to maintain. Additionally, by using polymorphism, we were able to write code that can work with objects of different classes in a flexible and extensible way.

'''


# PODRACER CLASS TESTS
# Create a new Podracer instance with max_speed 100, condition "perfect", and price 1000.
podracer = Podracer(100, "perfect", 1000)

# Print the initial values of the attributes.
print(podracer.max_speed)  # Output: 100
print(podracer.condition)  # Output: "perfect"
print(podracer.price)  # Output: 1000

# Call the repair() method to update the condition of the podracer.
podracer.repair()

# Print the updated value of the condition attribute.
print(podracer.condition)  # Output: "repaired"

# ANAKINSPOD CLASS TESTS
# Create a new AnakinsPod instance with max_speed 100, condition "perfect", and price 1000.
anakins_pod = AnakinsPod(100, "perfect", 1000)

# Print the initial value of the max_speed attribute.
print(anakins_pod.max_speed)  # Output: 100

# Call the boost() method to update the max_speed of the podracer.
anakins_pod.boost()

# Print the updated value of the max_speed attribute.
print(anakins_pod.max_speed)  # Output: 200

# SEBULBASPOD CLASS TESTS
# Create a new SebulbasPod instance with max_speed 100, condition "perfect", and price 1000.
sebulbas_pod = SebulbasPod(100, "perfect", 1000)

# Print the initial value of the condition attribute.
print(sebulbas_pod.condition)  # Output: "perfect"

# Call the flame_jet() method to update the condition of the podracer.
sebulbas_pod.flame_jet(podracer)

# Print the updated value of the condition attribute.
print(podracer.condition)  # Output: "trashed"


# Finally, create an instance of each class and test all of your methods.
pod1 = Podracer(100, "perfect", 1000)
pod2 = AnakinsPod(100, "perfect", 1000)
pod3 = SebulbasPod(100, "perfect", 1000)
print(pod1.condition)
pod1.repair()
print(pod1.condition)
print(pod2.max_speed)
pod2.boost()
print(pod2.max_speed)
print(pod3.condition)
pod3.flame_jet(pod1)
print(pod1.condition)