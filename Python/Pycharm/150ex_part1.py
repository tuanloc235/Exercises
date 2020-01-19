# # Exercise 1
# # Write a Python program to print the following string in a specific format (see the output).
# # Sample String: "Twinkle, twinkle, little star, How I wonder what you are!
# # Up above the world so high, Like a diamond in the sky.
# # Twinkle, twinkle, little star, How I wonder what you are!"
# # print("Twinkle, twinkle, little star, "
# #       "\n\tHow I wonder what you are! "
# #       "\n\t\tUp above the world so high, "
# #       "\n\t\tLike a diamond in the sky. "
# #       "\nTwinkle, twinkle, little star, "
# #       "\n\tHow I wonder what you are!")
# #
# # Write a Python program to get the Python version you are using.
# # A string containing the version number of the Python interpreter plus
# # additional information on the build number and compiler used. This string
# # is displayed when the interactive interpreter is started.
# import  sys
# print("Python version")
# print(sys.version)
# print("Python version infomation")
# print(sys._version_info)
#
# # Exercise 3
# # Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print("Current date and time :")
# print(now.strftime("%Y-%m-%d  %H:%M:%S"))
#
# # Exercise 4
# # Write a Python program which accepts the radius of a circle from the user and compute the area.
# from math import  pi
# pi = pi
# num = float(input("Input the radius of circle : "))
# print("Print area of the circle with the radius "+ str(num)+' is '+ str(pi*num*num))
#
# # Exercise 5
# # Write a Python program which accepts the user's first and last name
# # and print them in reverse order with a space between them.
# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname + " " + fname)
#
#
# # Exercise 6
# # Write a Python program which accepts a sequence of comma-separated numbers
# # from user and generate a list and a tuple with those numbers.
# #
# # Sample data: 3, 5, 7, 23
# #
# # Python list:
# #
# # A list is a container which holds comma separated values (items or elements)
# # between square brackets where items or elements need not all have the same type.
# # In general, we can define a list as an object that contains multiple data items (elements).
# # The contents of a list can be changed during program execution.
# # The size of a list can also change during execution, as elements are added or removed from it.
# #
# # Python tuple:
# #
# # A tuple is container which holds a series of comma separated values (items or elements)
# # between parentheses such as an (x, y) co-ordinate.
# # Tuples are like lists, except they are immutable
# # (i.e. you cannot change its content once created) and can hold mix data types.
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
#
# # Exercise 7
# # Write a Python program to accept a filename from the user and print the extension of that.
# #
# # Sample filename: abc.java
# #
# # Python str.rsplit(sep=None, maxsplit=-1) function:
# #
# # The function returns a list of the words of a given string using a separator as the delimiter string.
# #
# # If maxsplit is given, the list will have at most maxsplit+1 elements.
# # If maxsplit is not specified or -1, then there is no limit on the number of splits.
# # If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
# # The sep argument may consist of multiple characters.
# # Splitting an empty string with a specified separator returns [''].
# filename = input("Enter filename : ")
# file = filename.split('.')
# print("The extension of the file is "+repr(file[-1]))
#
# # Exercise 8
# # Write a Python program to display the first and last colors from the following list.
# # color_list = ["Red","Green","White" ,"Black"]
# color_list = ["Red","Green","White" ,"Black"]
# print("%s and %s"%(color_list[0],color_list[-1]))
#
# # Exercise 9
# # Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# #
# # exam_st_date = (11, 12, 2014)
# # Sample Output: The examination will start from : 11 / 12 / 2014
# exam_st_date = (11,12,2014)
# print('%s/%s/%s'%(exam_st_date))
#
# # Exercise 10
# # Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# #
# # Sample value of n is 5
# #
# # Python int(x, base=10):
# #
# # The function returns an integer object constructed from a number or string x, or return 0
# # if no arguments are given. If x is a number, return x.__int__().
# # For floating point numbers, this truncates towards zero.
# #
# # If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance
# # representing an integer literal in radix base
# # The literal can be preceded by + or - (with no space in between) and surrounded by whitespace
# # A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35.
# # The default base is 10.
# # The allowed values are 0 and 2-36. Base-2, -8, and -16
# # literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code.
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)
#
# # Exercise 11
# # Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# # Sample function: abs()
# print(abs.__doc__)
#
# # Exercise 12
# # Write a Python program to print the calendar of a given month and year.
# # Note: Use 'calendar' module.
# # Python calendar.month(theyear, themonth, w=0, l=0):
# #
# # The function returns a month’s calendar in a multi-line string using the
# # formatmonth() of the TextCalendar class.
# # 'l' specifies the number of lines that each week will use.
# import calendar
# month = int(input("Enter month : "))
# year = int(input("Enter year :"))
# print(calendar.month(theyear=year,themonth=month))
#
#
# # Exercise 13
# # Write a Python program to print the following 'here document'.
# #
# # Sample string:
# # a string that you "don't" have to escape
# # This
# # is a ....... multi-line
# # heredoc string --------> example
# text_ex = '''
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# '''
#
# # Exercise 14
# # Write a Python program to calculate number of days between two dates.
# #
# # Python datetime.date(year, month, day) :
# #
# # The function returns date object with same year, month and day. All arguments are required.
# # Arguments may be integers, in the following ranges:
# #
# # MINYEAR <= year <= MAXYEAR
# # 1 <= month <= 12
# # 1 <= day <= number of days in the given month and year
# # If an argument outside those ranges is given, ValueError is raised.
# #
# # Note: The smallest year number allowed in a date or datetime object. MINYEAR is 1.
# # The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
# from datetime import  date
# dt1 = date(2014,7,2)
# dt2 = date(2014,7,14)
# print(dt2-dt1)
#
# # Exercise 15
# # Write a Python program to get the the volume of a sphere with radius 6.
# #
# # Python: Volume of a Sphere
# #
# # A sphere is a three-dimensional solid with no face, no edge, no base and no vertex.
# # It is a round body with all points on its surface equidistant from the center.
# # The volume of a sphere is measured in cubic units.
# #
# # The volume of the sphere is : V = 4/3 × π × r3 = π × d3/6.
#
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)

# Exercise 16
# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

# def difference(n):
#     if n > 17:
#         return abs(17-n)*2
#     return abs(17-n)
# print(difference(22))
# print(difference(14))
#

# Exercise 17
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
# def near_thousand(n):
#     return (abs(1000-n)<=100) or (abs(2000-n)<=100)
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))
#

# exercise 18
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
# def sum_thrice(x, y, z):
#     sum = x + y + z
#
#     if x == y == z:
#         sum = sum * 3
#     return sum
#
#
# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

# Exercise 19
# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
# def new_string(n):
#     if len(n) >= 2 and n[0:2]=='Is':
#         return n
#     return 'Is'+n
# print(new_string('Array'))
# print(new_string('Isarray'))
#
#
# #Exercise 20
# #Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result
#
# print(larger_string('abc', 2))
# print(larger_string('.py', 3))

# # Exercise 21
# # Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")


# #Exercise 22
# #Write a Python program to count the number 4 in a given list.
# def list_count_for(n):
#     k = 0
#     for i in range(len(n)):
#         if int(n[i])==4:
#             k += 1
#     return k
# m = [1, 4, 6, 7, 4]
# print(str(list_count_for(m)))

#Exercise 23
#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
# def substring_copy(str,n):
#     result = ''
#     if len(str) < 2:
#         for i in range (n):
#             result += str
#         return result
#     for i in range (n):
#         result += str[0:2]
#     return result
# print(substring_copy('abcdef',3))
# print(substring_copy('a',6))

#Exercise 24
#Write a Python program to test whether a passed letter is a vowel or not.
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))

# # Exercise 25
# # Write a Python program to check whether a specified value is contained in a group of values.
# #
# # Test Data:
# # 3 -> [1, 5, 8, 3] : True
# # -1 -> [1, 5, 8, 3] : False
# def check_value_contained(n):
#     li = [1,5,8,3]
#     return  n in li
# print(check_value_contained(3))
# print(check_value_contained(-1))

# #Exercise 26
# #Write a python program to create a histogram from a given list of interger
# li = [2,3,6,5]
#
# def histogram(li):
#     for i in li:
#         for j in range (int(i)):
#             print('@',end='')
#         print('\r')
# histogram(li)

# #Exercise 27
# #Write a Python program to concatenate all elements in a list into a string and return it.
# li = [1,5,12,2]
# def concatenate_list_data(li):
#     result = ''
#     for i in li:
#         result += str(i)
#     return result
# print(concatenate_list_data(li))

# #Exercise 28
# #Write a Python program to print out all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# for i in numbers:
#     number = int(i)
#     if number == 237:
#         break
#     elif number %2 == 0:
#         print(number)

# # Exercise 29
# # Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# #
# # Test Data:
# # color_list_1 = set(["White", "Black", "Red"])
# # color_list_2 = set(["Red", "Green"])
# # Expected Output :
# # {'Black', 'White'}
#
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
# print(color_list_1.difference(color_list_2))

# # Exercise 30
# # Write a Python program that will accept the base and height of a triangle and compute the area.
# #
# # Python: Area of a triangle
# #
# # A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry. A triangle with vertices A, B, and C is denoted triangle ABC.
# #
# # Vertex of a triangle: The point at which two sides of a triangle meet.
# # Altitude of a triangle: The perpendicular segment from a vertex of a triangle to the line containing the opposite side.
# # Base of a triangle: The side of a triangle to which an altitude is drawn.
# # Height of a triangle: The length of an altitude.
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
#
# area = b*h/2
# print("area = ", area)

Exercise 31













