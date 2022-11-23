# def is_uppercase(inp):
#     new_inp = inp.upper()
#     if new_inp == inp:
        
#     print(inp)
#     print(new_inp)
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")


# def expression_matter(a, b, c):
#     min1 = min(a, b, c)
#     print(min1)
# expression_matter(1, 8, 2)


# def between(a,b):
#     print(list(range(a, b+1)))
# between(-5,5)


# def correct(s):
#     #print(s.replace("5", "S").replace("1", "I").replace("0", "O"))
#     print(s.translate(str.maketrans("501L", "SOIl")))
# correct("L0ND0N")

# def fix_the_meerkat(arr, letter):
#     #print(arr[::-1])
#     # arr.reverse()
#     # print(str.arr(arr.count(letter)))
#     new = str(arr)
#     x = new.count("t")
#     print(type(new))
#     print(x)
    
# fix_the_meerkat(["tail", "bttody", "thead", "t"], "t")

# def find_diffetence(a,b):
#     x = abs(a[0]*a[1]*a[2]) - (b[0]*b[1]*b[2]))
#     print(abs(x))
# find_diffetence([2, 2, -4], [4, 5, 1])



# txt = "565543"

# x = txt.isnumeric()
# # 7
# # is number pythonPython By Nhut Le on Apr 25 2022 ThankComment
# import numbers

# variable = 5
# print(isinstance(5, numbers.Number))



# def index(array, n):
#     try:
#         print(array[n] ** n)
#     except:
#         print(-1)
# index([1, 2, 3, 4],3)


# x = [ 4, 5 ,56, 7]
# y = [ 45, 78, 1]
# print(sorted(x + y))


# x = ["bitcoin", "a s a", "a a a", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
# x1 = "***".join(sorted(x)[1])
# print(x1)

# def divisible_by(numbers, divisor):
#     x = [i for i in numbers if i % divisor == 0]
#     print(x)
# divisible_by([1, 4, 50, 8], 2)

# x = '"bitcoin", "Asa", "a a a", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"'
# x1 = x.capitalize()
# print(x1)


# x = "aba"
# x1 = x.lo()
# print(x1)



# def arr(n=0): 
#     x = list(range(n))
#     print(x)
# arr()



# def multi_table(number):
#     i = 1
#     while i < 11:
#         print("{}*{}={}".format(i,number,i * number))
#         i += 1
# multi_table(9)



# def name_shuffler(str):
#     #your code here
#     new_str = str.split(" ")
#     print(new_str[1] + new_str[0])
# name_shuffler("sandro janiashvili")

# import math
# x = [1, 4, 7, 9, 8]
# new_x =[]
# for char in x:
#     if math.sqrt(char) == 

# import math
# x = [1, 4, 7, 9, 100]
# new_x = []
# for char in x:
#     if math.sqrt(char) == int(math.sqrt(char)):
#         new_x.append(int(math.sqrt(char)))
#     else:
#         new_x.append(char ** 2)
# print(new_x)
    
    
# class ball(objeqt):
#     def __init__(self , type = "regular"):
#         self.ball_type = type
    
    
    
# class Ball(object):
#     def __init__(self,ball_type='regular'):
#         self.ball_type = ball_type
#     def __TomFoolery__(ball_type):
#         self.ball_type = "HUGE" ## HAHA HAD TO



# def warn_the_sheep(queue):
#     x = 71 
#     print(chr(x))
#     print(ord("a"))
#     print()
# warn_the_sheep("21")

# def find_multiples(int, limit):
#     # Your code here
#     x =[]
#     x1 = 0 
#     while x1 < limit:
#         x1 += int
#         x.append(x1)
#     if x[-1] > limit:
#         print(x[0:-1])
#     else:
#         print(x)
# find_multiples(3,12)



# def find_multiples(int, limit):
#     x = list(range(int, limit +1, int))
#     print(x)
# find_multiples(2, 6)


# import re
# def replace_dots(str):
#     print(re.sub(r".", "-", str))
    
# replace_dots("one.two.three")

# u
# x = "one.two.three"
# x1 = x.replace(".", "-")
# x1.upper()
# print(x1)


# def mouth_size(animal): 
#     print("small" if animal.lower() == "alligator" else "wird")
# mouth_size("alligato")


#def merge_arrays(arr1, arr2):
    # arr3 = arr1 + arr2
    # arr3.sort()
    # arr4 = []
    # for char in arr3:
    #     if char not in arr4:
    #         arr4.append(char)
    # #print(arr3)
    # print(arr4)
#     y = "sandro"
#     if y is
#     y.capitalize()
#     x = sorted(set(arr1 + arr2))
#     print(x)
# merge_arrays([1,2,3,4], [5,6,7,8])
# merge_arrays([1,3,5,7,9,10,], [10,8,6,4,2])


# def to_binary(n):
#     x = bin(n)
#     print(x[2:])
    
# to_binary(11)

# def to_binary(n):
#     x = ""
#     char = n
#     while char > 0:
#         x += str(char % 2)
#         char = char // 2
#     print(x[::-1])     
# to_binary(11)


# def pipe_fix(nums):
#     x = list(range(nums[0],nums[-1] +1)) 
#     print(x)
    
# pipe_fix([1, 2, 3, 12])
# pipe_fix([6, 9])

# x = [1,5, 8, 4, 0]
# x.sort()
# print(x)

# def flip(d, a):
#     a.sort()
#     print(a)
# flip('R', [3, 2, 1, 2])


# def generate_range(min, max):
#     x = list(range(max+min)[min:max+1])
#     print(x)
# generate_range(-2,10)




