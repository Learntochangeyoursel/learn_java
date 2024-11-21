# 20241121 锻炼循环使用能力
# 判断两个数的最小公倍数数和最大公约数，首先得了解最小公倍数和最大公约数的定义
# 首先需要判断得到的两数是否为整数
# 其次需要得到两数所有的质因数
# 然后将最小公质数相乘为最小公倍数，将两数相乘除以最小公倍数则得到最大公约数

'''解决思路'''
from src.Homework import test03


# 1. 将参数设置为整形
# 2. 判断两数是否为素数,若为素数，
# 3.

def judgeTwoNumbers(num1:int ,num2 : int ):
    bool1= test03.judgePrimeNumber02(num1)
    bool2= test03.judgePrimeNumber02(num2)
    if  bool1 and bool2 == True :
        min = 1
        max = num1 * num2
        print(min,max)
    else:
        for i in range(2,num1+1):
            print(i)
            if num2 % i == 0 and num1 % i == 0 :
                min = i
                max = int(num1 * num2 / i)
                print(min,max)
                break
    return min,max

print(judgeTwoNumbers(3,9))


