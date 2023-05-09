normal = [
    "Print largest and smallest values out of two.",
    "Print largest and smallest values out of three.",
    "Check whether a given number is odd or even.",
    "Check whether a given number is divisible by 10 or not.",
    "Accept age of a person. If age is less than 18, print minor otherwise Major.",
    "Accept a number from the user. And print number of digits in it.",
    "Accept a year value from the user. Check whether it is a leap year or not.",
    "Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.",
    "Print absolute value of a given number.",
    "Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.",
    "Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.",
    "Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )",
    "Convert number 0 to 19 to its equivalent words. E.g. 0 → zero, 19 → nineteen.",
    "Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:\n\nMarks Range\tGrade\nAbsent\t\tNA\n0 – 39\t\tF\n40 – 44\t\tP\n45 – 49\t\tC\n50 – 54\t\tB\n55 – 59\t\tB+\n60 – 69\t\tA\n70 – 79\t\tA+\n80 – 100\tO"
]


string = [
    "Count how many vowels are there in a string. Accept the string from the user.",
    "Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.",
    "Accept two strings. Check whether one string is there in another string.",
    "Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”."
]


tuple = [
    "A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))",
    "A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age",
    "Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.",
    "Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.",
    "Remove empty tuple(s) from the list of tuples.",
    "Modify an element of a tuple.",
    "Delete an element of a tuple."
]


_set = [
    "Write a program that converts words present in a list into uppercase and stores them in a set.",
    "Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.",
    "Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.",
    "A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B."
]

oop = [
"Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.",
"Write a program that implements a Matrix class and performs addition, multiplication and transpose operations on 3x3 matrices.",
"Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.",
"Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.",
"Write a program that creates and uses a Time class to perform various time arithmetic operations.",
"Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.",
"Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)",
"Implement a String class containing the following functions: a. Overloaded += operator function to perform string concatenation b. Method toLower() to convert upper case letters to lower case. c. Method toUpper() to convert lower case letters to upper case."
]   



api = "sk-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"

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai

openai.api_key = api

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)