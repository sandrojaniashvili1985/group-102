# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     new = []
#     for i in range(n):
#         new.append(int(i) * x)
        
#     print(new[1:])
    
# count_by(2, 5)
    
    
    
    
# def count_sheep(n):
#     print("".join("{} sheep...".format(i) for i in range(1, n+1)))
# count_sheep(5)



# x = "sandro janiashvili "

# # n = 5

# # print("".join("{} ".format(i) + x for i in range(1, n+1)))
# print(x)

# DataPoints = [0,12,24]
# print (str(DataPoints[0]) + "\t" + str(DataPoints[1]) + "\n" + str(DataPoints[2]))

# def get_average(marks):
#     marks_sum = 0
#     marks_len = 0
    
#     for i in marks:
#         marks_sum += i 
#         marks_len += 1
#     print(average)
# average = marks_sum // marks_len   
# get_average([1, 5, 87, 45, 8, 8])


# def get_average(marks):
#     i = 0 
#     sum = 0
#     while i < len(marks):
#         sum += int(marks[i])
#         i += 1
        
#     print(sum // len(marks))
    
# get_average([1, 5, 87, 45, 8, 8])
# get_average([2,5,13,20,16,16,10])


# def get_average(marks):
#     average = sum(marks) // len(marks)
#     print(average)
    
# get_average([1, 5, 87, 45, 8, 8])
# get_average([2,5,13,20,16,16,10])

# x = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
# print(x[1][1])

# def get_grade(s1, s2, s3):
#     # Code here
#     average = (s1 + s2 + s3) / 3
    
#     return "F" if average < 60 or "D" elif average < 70 or "C" if average < 80 or "B" if average <90 else: "A" 
    
# get_grade(90, 92, 98)



# def get_grade(s1, s2, s3):
#     mean = sum([s1,s2,s3])/3
#     if mean>=90: print('A')
#     elif mean>=80: print('B')
#     elif mean>=70: print('C')
#     elif mean>=60: print('D')
#     else:
#         print('F')
    
# get_grade(90, 5, 95)


# from threading import activeCount


# def get_grade(s1, s2, s3):
#     ave = (s1 + s2 + s3) / 3
#     print({100: "A", ave >= 80 :"B", ave >= 70: "C", ave >= 60: "D", ave < 60: "F"}[ave])
#     #print(ave)    
# get_grade(100, 100, 100)
   
    
# def update_light(current):
#     print({"green": "yellow", "yellow": "red", "red": "green"}[current])
    
# update_light("green")


# def sum_array(arr):
#     if len(arr) < 3:
#         print(0)
#     max1 = max(arr)
#     min1 = min(arr)
#     sum_arr = 0
#     for i in arr:
#         sum_arr += i
#     #print(max1, min1)
#     #print(sum_arr - min1 - max1)
#     print(len(arr))
# sum_array([6, 2])
# sum_array([-6, -20, -1, -10, -12])


# def remove_exclamation_marks(s):
#     print(s.replace("!", "?"))
    
    
# remove_exclamation_marks("sandro! janiashvi!li!")


# x = 20 
# y = 30
# a = sum(x,y)



# def get_planet_name(id):
#     print({
#          1: "Mercury",
#          2: "Venus",
#          3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id))
    
# get_planet_name(4)

# def get_planet_name(id):
#     #new_id = 100 - id
#     print({1: "s",
#      2: "a",
#      "!": 5 + 7,
#      4: "d",
#      5: "r",
#      6: "o"}.get(id > 0, None))
# get_planet_name(5)
