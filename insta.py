#
# numbers = []
# target = 0
# while target < 5:
#     numbers.append(target * 8)
#     target += 1
# print(numbers)
#

# numbers = [100,200,400,500,600,450,650,750]
# i = 0
# while i < len(numbers) :
#     print(numbers[i])
#     if numbers[i] == 300:
#         break
#         print("Break from loop")
#
#     numbers[i] += 1
# print(numbers[i])

numbers = [100, 200, 300, 400, 450, 650, 550, 750, 700]
i = 0

while i < len(numbers):
    
    print(numbers[i])
    if numbers[i] >= 300:
        print("Break from loop")
        break
    i += 1
