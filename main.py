#a= int(input("Введите значене в переменнную А: "))
#b= int(input("Введите значене в переменнную В: "))

#print("А =", a, "Б =", b)


#for x in range(a + a % 2, b + 1, 2):
 #   print(x, end=" ")

# a = int(input("Введите значене в переменнную А: "))
# b = int(input("Введите значене в переменнную В: "))
# c = int(input("Введите значене в переменнную C: "))
# d = int(input("Введите значене в переменнную D: "))

# for x in range(a + a % d, b + 1, d):
#     #if x % d == c:
#         print(x, end=", ")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for number in range(a + (c - a % d), b + 1, d):
#     print(number, end=' ')

# sum =0
# for i in range(5):

#     a=int(input())

#     sum=sum+a

# print(sum, end=" ")
# Вариант через файл
# with open("input_data.txt", "r") as file:
#     numbers = [
#         int(item) 
#         for item in file.read().strip().split('\n')
#     ]
#     # numbers = list(map(int, file.read().strip().split('\n')))

# print(sum(numbers))

# N = int(input())
# sum = 0
# for i in range(N):

#      a = int(input())

#      sum = sum + a

# print(sum, end=" ")

# N = int(input())
# sum = 0

# for i in range(N):

#      a = int(input())

#      if a == 0:

#         sum = sum + 1

# print(sum, end=" ")

N = int(input())
sum = 0
sum_pol = 0
sum_otr = 0

for i in range(N):

    a = int(input())

    if a == 0:
        sum = sum + 1
    if a > 0:
        sum_pol = sum_pol +1
    else:
        sum_otr = sum_otr +1

print(sum, sum_pol, sum_otr)


# mas = [1, 98, 345, 567]

# for index in range(len(mas)):
#     item = mas[index]
#     code ...
#     if x > 0:
#         code...

# for item in mas:
#     code...


# while (...){
    
# }

# while x > 0:
#     code.