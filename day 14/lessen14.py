# def generate_range(min, max, step):
#     x = list(range(min, max+1,step))
    
#     print(x)
    
#     #print(list(range(11)[min]))
# generate_range(-1, 10, 2)


# def hex_to_dec(s):
#     x = int(s, base = 16)
#     print(x)
# hex_to_dec("b")


# def doors(n):
#     x = []
#     for num in range(n):
#         x.append(0)
    
#     #for char in n:
#     print(x) 
# doors(5)      

# y = "gtrasxzvwb"
# x = "asdhgbewis"
# x1 = "".join(sorted(set(x + y)))
# print(x1)

# x = [1,0,0,1]
# y = len(x)
# print(y)

# def binary_array_to_number(arr):
#     print(int("".join(map(str, arr)), 2))
# binary_array_to_number([1,1,1,1])

# #x = [21, 5, 8, 98]
# num= ["sandro", "nika", "ana"]
# num.reverse()
# x = num
# #x = " ".join(num)
# print(x)
# import math
# def door(n):
#     math.sqrt(n)

# x1 = 2
# x = [1,2,3,4,5,6,7,8,9]
# y = list(range(x[1],x[x1*2],2))
# print(y)

# def doors(n):
#     # Enjoy
#     # Thanks!

#     # doorstates should save how often each door
#     # has been accessed
#     doorstates = [0] * n
    
#     # open doors
#     opendoors = 0
    
#     # for every door from 1 to n
#     for i in range(1, n + 1):
        
#         # for every door the student
#         # can access
#         for j in range(i, n + 1, i):
            
#             # add 1 to how often this
#             # door has been accessed
#             doorstates[j - 1] += 1
    
#     # for each door
#     for count in doorstates:
        
#         # if the door has been opened
#         # and closed so many times so that
#         # the door is open at the end
#         if (count + 1) % 2 == 0:
            
#             # add one open door
#             opendoors += 1
            
#     return opendoors    

#     # i cant even believe i did this



# def doors(n):
#     arr = [0] * n
#     for i in range(1,n+1):
#         for j in range(i,n+1,i):
#             if arr[j-1] == 0:
#                 arr[j-1] = 1
#             else: 
#                 arr[j-1] = 0
    
    
    
#     print(arr)
# doors(100)



# def doors(n):
#     arr = [0] * n
#     for i in range(1,n+1):
#         for j in range(i,n+1,i):
#             if arr[j-1] == 0:
#                 arr[j-1] = 1
#             elif arr[j-1] == 1:
#                 arr[j-1] = 0
#     print(arr)
#     sum = 0
#     for x in arr:
#         sum += x
#     print(sum)
# doors(10)
            
# n = 18           
# x = [-1,-89,-3,-2,7,8,3,4,5]
# y = []
# for i in range(n):
#     y.append(x[i])
# print(y)


# def bin_to_decimal(inp):
#    x = int(inp,2)
#    print(x)
# bin_to_decimal("1010111100")


# def my_join(arr):
#    my_arr = ""
#    for i in arr:
#       my_arr += str(i)
#    print(my_arr)
# my_join([2, 5, 8,])


# num = 2437.68

# # Way 1: String Formatting

# '{:,}'.format(num)
# >>> '2,437.68'


# # Way 2: F-Strings

# f'{num:,}'
# >>> '2,437.68'


# # Way 3: Built-in Format Function

# format(num, ',')
# >>> '2,437.68'

# x = 3
# y = "{:0.2f}".format(x)
# print(y)


# x = 2
# print("{:0.2f}".format(x))

# def get_size(w,h,d):
#     #your code here
    
#    s = 2 * (w*h+h*d+w*d)
#    print(s)
# get_size(1,2,2)


# def damage(hilse,damage):
#    x = max(0,hilse-damage)
#    print(x)
# damage(40,30)




# def change(name):
#    x = "".join(name)

# import re
# def user(username):
#    x = re.match("^[a-z0-9_]{4,16}",username)
#    if x:
#       print(True)
#    else:
#       print(False)
# user("sand123!/")



# def swap_values(args): 
#     x = args[0]
#     args[0] = args[1]
#     args[1] = x
#     print([args[1],args[0]])
# swap_values([1, 2])


# def fuzz_buzz(n):
#     x = []
#     for char in range(n):
#         x.append(char+1)
#     print(x)
# fuzz_buzz(10)

# y = ""
# x = "605000"
# for char in x:
#     if char == "0":
#          x = x.removesuffix("0")
# #rint(x.removesuffix("0"))
# print(x)


# def get_drink_by_profession(param):
#     # code me!
#     x = {
#     "Jabroni":	        "Patron Tequila",
#     "School Counselor":	"Anything with Alcohol",
#     "Programmer":	    "Hipster Craft Beer",
#     "Bike Gang Member":	"Moonshine",
#     "Politician":	    "Your tax dollars",
#     "Rapper":	        "Cristal",
#      	}
#     #print(x.get(param.title()))
#     y = x["Programmer"]
#     h = x.get("Politician")
#     print(x.get("Rapper"))
#     print(y)
#     print(h)
# get_drink_by_profession("khffd")






# import math
# x = 2 
# print(math.pi)


# def subtract_sum(n):
#     str_n = str(n)
#     sum = 0
#     x1 = n
#     x = 0
#     while x1 >= 100:
#         str_n = str(x)
#         for char in str_n:
#             sum += int(char)
#         x = (n - sum)
#         x1 = x
#     print(x)
# subtract_sum(2253)
# #subtract_sum(325)
# def doble(nn):
#     x = {1:'kiwi',2:'pear',3:'kiwi',4:'banana',5:'melon',6:'banana',7:'melon',
#          8:'pineapple',9:'apple',10:'pineapple',11:'cucumber',12:'pineapple',
#          13:'cucumber',14:'orange',15:'grape',16:'orange',17:'grape',18:'apple',
#          19:'grape',20:'cherry',21:'pear',22:'cherry',23:'pear',24:'kiwi',
#          25:'banana',26:'kiwi',27:'apple',28:'melon',29:'banana',30:'melon',
#          31:'pineapple',32:'melon',33:'pineapple',34:'cucumber',35:'orange',
#          36:'apple',37:'orange',38:'grape',39:'orange',40:'grape',41:'cherry',
#          42:'pear',43:'cherry',44:'pear',45:'apple',46:'pear',47:'kiwi',
#          48:'banana',49:'kiwi',50:'banana',51:'melon',52:'pineapple',53:'melon',
#          54:'apple',55:'cucumber',56:'pineapple',57:'cucumber',58:'orange',
#          59:'cucumber',60:'orange',61:'grape',62:'cherry',63:'apple',
#          64:'cherry',65:'pear',66:'cherry',67:'pear',68:'kiwi',69:'pear',
#          70:'kiwi', 71:'banana',72:'apple',73:'banana',74:'melon',
#          75:'pineapple',76:'melon',77:'pineapple',78:'cucumber',79:'pineapple',
#          80:'cucumber',81:'apple',82:'grape',83:'orange',84:'grape',85:'cherry',
#          86:'grape',87:'cherry',88:'pear',89:'cherry',90:'apple',91:'kiwi',
#          92:'banana',93:'kiwi',94:'banana',95:'melon',96:'banana',97:'melon',
#          98:'pineapple',99:'apple',100:'pineapple'}
    
    
#     print(x.get(nn))
# doble(subtract_sum(1872))


# x = "sandro jniashvili misha janiashvili"
# x.items()
# print(x)


# def array(str):
#     new = str.split(",")
#     new_x = " ".join(new[1:-1])
#     print(new_x)
# array("2,5,4,7,8,ghh,yuut")

# def zipped(aa,bb,cc):
#      x = list(zip(aa,bb,cc))
#      #print(x)
#      x = "".join("".join(mini_sia) for mini_sia in zip(aa,cc,bb))
#      print(x)
    
# zipped(["a","b","c","d"],["1","2","3","4"],["sandro","misha","dato","nika"])

#return ''.join(''.join(a) for a in zip(one, two, three))





# x = [21,54,65,8,7,2,]
# sum = 0
# for char in x:
#     sum += int(char)
# print(sum)

# # 3
# 16
# 17 a = [4, 1, 2, 3]

# 18 b = list(range(1, 6, 2))
# 19 for i in a:
# b. append(a[i + 1] + a[i])


# a = 5

# if a % 2 != 0:
# 	raise Exception("The number shouldn't be an odd integer")



# s = "sandro"
  
# try:
#     num = int(s)
# except "sandro":
#     raise ValueError("ar mushaobs")
# print(num)


# x= 2.23556
# #y = "{:0.2f}".format(x)
# y = round(x,2)
# print(y)




# def add(str_1):
#      new = str_1.split()
#      i = 0
#      for char in new:
#           new[i] += " " + str(len(char))
#           i +=1
#      print(new)
     
     
     
# add("sandro misha nika tamuna")


# x = [2,5,1,8,6]
# x.sort()
# j = 0
# for i in x:
#      if i != j:
#           x.append(j)
#           break
#      j += 1
# x.sort()
# print(x)

#    x = re.match("^[a-z0-9_]{4,16}",username)
# import re
# xx = "g urueducationisfun"
# #r1 = re.findall(r"^\w+",xx)
# r2 = re.search(r"[A-Za-z]+",xx)
# print(r2)

import re
def username(name):
    x = input("your name ")
    x1 = x.re.match(r"[A-Za-z]"{6,12}, name)
    print(x1)
    
username("sandro")
