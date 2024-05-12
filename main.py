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
