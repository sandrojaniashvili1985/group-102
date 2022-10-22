# ინთით შეიტანეთ თქვენი სახელი და გვარი
#ტერმინალით გამოიტანეთ რომელ ინდექსზე არის ხმოვანი



# full_name = input("name and sarname: ")

# i = 0

# while i < len(full_name):
#     if full_name[i] in "aeiou":
#         print(str(i) + full_name[i])
#     i += 1
# x = 1
# for i in range(5):
#     for j in range(4):
#         print(x ,"sandro")
#         x += 1
# x = 0
# for i in range(5):
#     age_of_user = int(input("enter your age: "))
    
#     if age_of_user > 3 :
#         x += 100
# print(x)

# num = int(input("enter numbar"))

# for i in range(1,num):
#     if i % 2 == 1:
#         if i % 3 == 0:
#             print("learn")
#         elif i % 5 == 0:
#             print("solo")
#         elif i % 3 == 0 and i % 5 == 0:
#             print("sololearn")
#         else:
#             print(i)

# user_wheight = float(input("enter your wheight: "))
# user_height = float(input("enter your height: "))

# bmi = user_wheight / (user_height ** 2)

# if bmi < 18.5 :
#     print("underwheit")
# elif bmi > 18.5 and bmi < 25 :
#     print("normal")
# elif bmi > 25 and bmi < 30 :
#     print("overwheit")
# else: 
#     bmi < 30 
#     print("obesity")
# print(bmi)

my_list = ["xinkali", "mwvadi", "lobiani", "qababi", "xachapuri", "wyali"]
prices = [10, 15, 5, 25, 18, 3]
i = 0
for food in my_list:
    print(food + " girs " + str(prices[i]) + " lari")
    i += 1