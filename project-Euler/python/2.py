def fiboEvenSum(num):
    a = 1
    b = 2
    sum = b
    next = a+b
    while next<= num:
        if next % 2 == 0:
            sum+=next
            temp = next
            next+=b
            b = temp
        else:
            temp = next
            next+=b
            b = temp
    return sum
print(fiboEvenSum(34))
