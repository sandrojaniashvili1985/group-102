# from lessen9 import revers_arr
# from lessen9 import max_scores
# from lessen9 import multiplay
# students = ["nika", "natia", "iva", "gela", "elene", "???"]
# students2 = ["lana", "xatia", "koba", "soso"]
# # revers_arr(students)
# # revers_arr(students2)
# #max_scores(58,30)
# print(multiplay(10,5))
# def solushen(string):
#     my_str = ""
#     i = len(string)
#     while i > 0:
#         my_str += (string[i-1])
#         i -= 1
#     print(my_str)
# solushen("world")
# def positive_sum(arr):
#     # Your code here
#     sum = 0
#     for i in arr:
#         if i > 0:
#             sum += i
#         else:
#             sum += 0
#     print(sum)
# positive_sum([1, 2, 3, 4, -5, -6])
# def repeat_str(repeat, string):
#     new_str = ""
#     i = 0
#     while i < repeat:
#         new_str += string
#         i +=1
    
#     print(new_str)
# repeat_str(3,"aa ")

# def remove_char(s):
#     new_s = ""
#     i = 1
#     while i < len(s)-1:
#         new_s += s[i]
#         i += 1
#     print(new_s)
# remove_char("sworldk")

# def square_sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i ** 2
#     print(sum)
# square_sum([1, 2, -3])

#def summation(num):
#     new_num = 0
#     for i in range(num + 1):
#         new_num += i
#     print(new_num)
# summation(8)

# def count_sheeps(sheep):
#     sum = 0
#     for i in sheep:
#         if i :
#             sum += 1
#         else:
#             sum += 0
#     print(sum)
# count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True,True])

# def liters(time):
#     sum = time // 2
#     print(sum)
# liters(8.5)
# def litres(time):
#     sum = time // 2
    
#     return "'should return {} litre' ".format(int(sum))
#from ast import iter_fields


# def century(year):
#     cent = 0
#     if year % 100 == 0:
#         cent = (year / 100) 
#     else:
#         cent = (year // 100) + 1
        
#     print(int(cent))
# century(8)

# def basic_op(operator, value1, value2):
#     new_basic_op = 0
#     if operator == "+":
#         new_basic_op = value1 + value2
#     elif operator == "-":
#         new_basic_op = value1 - value2
#     elif operator == "*":
#         new_basic_op = value1 * value2
#     elif operator == "/":
#         new_basic_op = value1 / value2
#     print(new_basic_op)
# basic_op("*", 2, 5)

# def basic_op(operator, value1, value2):
#     calculator = {}{}{}.format(value1,operator,value2)
#     print(calculator)
# basic_op("+", 5, 7)

# def digitize(n):
#     new_n = []
#     i = len(n)
#     while i > 0:
#         new_n.append(n[i-1])
#         i -= 1
#     print(new_n)
# digitize([1,3,2,5,3])


# x = [1,3,2,5,3,8]
# # print(range(len(x)))
# for i in range(len(x)):
#     print("sandro")
def digitize(n):
    new_n = str(n)
    new_nn = []
    i = len(new_n)
    while i > 0:
        new_nn.append(int(new_n[i-1]))
        i -= 1
    print(new_nn)
digitize(35231)