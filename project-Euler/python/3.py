import math
def largestPrimeFactor(num):
    lv = 0
    while num%2 == 0:
        lv = 2 
        num = num//2
    for i in range(3,math.floor(math.sqrt(num)),2):
        while num % i == 0:
            lv = i
            num = num//i
    if num>2:
        lv =num
    return lv

print(largestPrimeFactor(600851475143))