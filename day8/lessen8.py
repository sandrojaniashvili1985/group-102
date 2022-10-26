# ფუნქციონალური პროგრამირება
# def wish_good_day(name, day):
#     print(name + " karg dges gisurveb " + str(day) + " oqtomberi")
# names = ["sandro", "shako", "beqa", "tamuna", "lasha"]
# for name in names:
#     wish_good_day(name, 17)
# def shekreba(num1,num2):
#     sum = num1 + num2
#     print(sum)
    
# shekreba(200, 190)
# def calculate_max(scores):
#     max = scores[0]
#     for max_nam in scores:
#         if max < max_nam:
#             max = max_nam
#     print(max)
# calculate_max([20,40,50,80])
# calculate_max([20,40,50,80,50,899,780])

def pair_sum(arr1,arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    print(arr1, arr2, arr3)
pair_sum([20,40,50,80],[20,10,50,80])