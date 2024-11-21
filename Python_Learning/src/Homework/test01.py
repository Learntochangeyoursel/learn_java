# 2021.11.21 上午作业

#这是一个简单的华氏温度转换为摄氏温度的函数
def temperature(Fahrenheit):
    return  (Fahrenheit - 32) / 1.8

#这是一个计算圆的面积的函数
def circleArea(radius):
    return 3.14 * (radius * radius)

# 这是一个判断输入年份是否为闰年的函数
def judgeLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 : return True
    elif year % 4 == 0 and year % 100 == 0:
            if year % 400 == 0:
                return True
if __name__ == '__main__':
    print('%.3f' % temperature(float(input("请输入温度"))))
    print('%.3f' % circleArea(float(input("请输入圆的半径"))))
    print(judgeLeapYear(int(input('请输入一个年份'))))
