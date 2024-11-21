
def is_palindrome(num):
    # 将数字转换为字符串
    str_num = str(num)
    # 检查字符串与其反转是否相同
    return str_num == str_num[::-1]

# 测试函数
numbers = [121, -121, 10, 12321]
for number in numbers:
    print(f"{number} is a palindrome: {is_palindrome(number)}")