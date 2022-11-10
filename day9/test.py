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
# repeat_str(3,"aa1 ")

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
# square_sum([1, 2, -3, 4])

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
# def digitize(n):
#     new_n = str(n)
#     new_nn = []
#     i = len(new_n)
#     while i > 0:
#         new_nn.append(int(new_n[i-1]))
#         i -= 1
#     print(new_nn)
# digitize(35231)

# def abbrev_name(name):
#     abbrev_name1 = ""
#     i = 0
#     while i < len(name):
#         if name[i] == " ":
#             abbrev_name1 = "{}.{}".format(name[0].capitalize(), name[i+1].capitalize())
#         i += 1
#     print(abbrev_name1)
# abbrev_name("sandro janiashvili")


# def past(h, m, s):
#     ms = (h * 60 * 60 * 1000) + (m * 60 * 1000) + (s * 1000)
#     print(ms) 
# past(1, 0, 0)

# def make_upper_case(s):
#     new_s = ""
#     for i in s:
#         new_s += i.capitalize()
#     print(new_s)
    
# make_upper_case("dsandro")

# def count_positives_sum_negatives(arr):
#     count_positives = 0 
#     sum_negatives = 0
#     new_arr = []
#     i = 0
#     while i < len(arr):
#         if arr[i] > 0:
#             count_positives += 1
#         elif arr[i] < 0:
#             sum_negatives += arr[i]
#         i += 1
#     if arr == []:
#         print(new_arr)
#     else:
#         new_arr.append(count_positives)
#         new_arr.append(sum_negatives)
#         print(new_arr)
# count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])
# count_positives_sum_negatives([])

# def is_divisible(n,x,y):
#     #your code here
#     if n // x == 0 and n // y == 0:
#         print("True")
#     else:
#         print("False")
# is_divisible(3, 2, 2)
# is_divisible(12, 3, 4)

# def fake_bin(x):
#     print(''.join('0' if c < '5' else '1' for c in x))
# fake_bin([5, 4, 8, 8, 9, 1, 2,])

# def check(seq, elem):
#     for i in seq:
#         if i == elem:
#             print(True)
#         elif i != elem:
#             print(False)
            
# check([78, 117, 110, 99, 104, 117, 107, 115], 8)
# check([101, 45, 75, 105, 99, 107], 107)
# check([80, 117, 115, 104, 45, 85, 112, 115])

# def reverse_seq(n):
#     new_n = []
#     i = n
#     while i > 0:
#         new_n.append(i)
#         i -=1
#     print(new_n)
# reverse_seq(5)



# def human_years_cat_years_dog_years(human_years):
#     #Your code here
#     cat_years = 24
#     dog_years = 24
#     new = [human_years,cat_years,dog_years]
#     i = 2
#     if human_years == 1:
#         cat_years = 15  
#         dog_years = 15
#     elif human_years == 2:
#         cat_years = 24
#         dog_years = 24
#     else:
#         while i < human_years:
#             cat_years += 4
#             dog_years += 5
#             i += 1
#     print(human_years, cat_years, dog_years)    
# human_years_cat_years_dog_years(1)
# human_years_cat_years_dog_years(2)
# human_years_cat_years_dog_years(3)


# def square_digits(num):
#     new_str = str(num)
#     new_str_square = ""
#     i = 0
#     while i < len(new_str):
#         new_str_square += str(int(new_str[i]) ** 2)
#         i += 1
#     print(new_str_square)
#square_digits(9132)
        


# def square_digits(num):
#     new_num = str(num)
#     for i in new_num:
#         int(i) ** 2
#     print(new_num[0])
# square_digits(911)


# def high_and_low(numbers):
#     # ...
#    num = sorted(numbers.split(), key=int)
#    print(num)
# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")


# def better_than_average(class_points, your_points):
#     # Your code here
#     sum = 0
    
#     for i in class_points:
#         sum += i
#     average = sum / len(class_points)   
#     if your_points > average:
#         print(True)
#     elif your_points < average:
#         print(False)
# better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)
# better_than_average([2, 1, 3], 5)
#better_than_average()


# def grow(arr):
#     mult = 1
#     for i in arr:
#         mult *= int(i)
#     print(mult)
# grow([2, 2, 2, 2, 2, 2])


# def smash(words):
#     new_words = ""
#     for i in words:
#         if i != ",":
#             new_words += str(i) + " "
    
#     print(new_words[0:-1])
          
          
# smash(["hello", "world"])


# def smash(words):
#     print(" ".join(words))
# smash(["hello", "world"])


# def string_to_array(s):
#     #your code here
#     new_s = []
#     new_s1 = []
#     i = 0
#     x = 0
#     n = 0
#     while i < len(s):
#         if s[i] == " ":
#             new_s.append(i)
#         i += 1
#     for x in new_s:
#         new_s1.append(s[n:x])
#         n = x + 1
#     new_s1.append(s[n:])    
#     print(new_s)
#     print(new_s1)
# string_to_array("Robin Singh sandro janiashvili giorgi afciauri")


# def string_to_array(s):
#     new_s = []
#     new_s = s.split(" ")
#     print(new_s)
    
    
#string_to_array("Robin Singh sandro janiashvili giorgi afciauri")

# x = "sandro janiashvili"
# n_x = []
# n_x.append(x[0:6])
# print(n_x)

# def reverse_words(s):
#     new_s = s.split(" ")
#     rev_words = ""
#     i = len(new_s) - 1
#     while i >= 0:
#         rev_words += new_s[i]
#         rev_words += " "
#         i -= 1
    
#     return rev_words[:-1]



# x = 7 % 6
# print(x)


# def how_much_i_love_you(nb_petals):
#     print(["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1])
# how_much_i_love_you(5)

 
#print([21, 45, 78, 9,][1])



def fix_the_meerkat(arr):
    new_arr = arr.replace(remark(arr[0],arr[-1]))
    print(new_arr)
fix_the_meerkat(["tail", "body", "head"])