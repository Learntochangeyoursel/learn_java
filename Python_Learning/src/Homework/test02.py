# 为了熟悉分支语句的一次作业

# 完成英寸和厘米之间的转换
def inchesCentimetersInterchange(length):
    # 判断单位时，防止不合法的字符串混入其中
    if len(length) == 3 :
        #查看长度的单位
        unit = length[-2:]
        #截取单位，将长度有字符串转换为float类型
        new_length = float(length.rstrip(length[-2:]))
        # 返回字符串，在拼接时需要将数据进行转换才可以
        if unit == "厘米" : return str(new_length / 2.45) + "英寸"
        elif unit == "英寸" : return  str(new_length * 2.45) + "厘米"
        else : return "输入格式有误"
    else: return "输入格式有误"

# 这是一个判断成绩等级的小函数
def gradeLevel(grade):
    if grade >= 90 : return "A"
    elif grade >= 80 : return "B"
    elif grade >= 70 : return "C"
    elif grade >= 60 : return "D"
    else: return "E"




# 调用inchesCentimetersInterchange()函数并将返回值打印出来，python在定义函数时默认有返回值None
if __name__ == '__main__':
    print(inchesCentimetersInterchange(input("请输入长度")))
    print (gradeLevel(30))



