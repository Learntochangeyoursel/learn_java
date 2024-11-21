# 20241121作业，锻炼循环使用能力

# 判断一个数是否为素数
def judgePrimeNumber(number):
    #设置区间，以最小的数2为中间值
    if number < 2 : return "不是"
    if number == 2 : return "是"
    for i in range (2,number):
        if number % i == 0 :
            return "不是"
    return "是"

# 判断一个数是否为素数 改进版，在上面的代码中间过多的考虑2的影响，导致自己做了过多的重复工作
def judgePrimeNumber02(number):
    #设置区间，以最小的数2为中间值，由素数的定义可知，素数是只能被1和本身整除的正整数，1不是素数
    if number < 2 : return False
    for i in range (2,number):
        if number % i == 0 :
            return False
    return True

if __name__ == '__main__':
    print(judgePrimeNumber02(2))