# Python初学者练习

# 练习1: 计算两个数的和
def exercise1(a, b):
    """计算两个数的和"""
    # 请在此处编写代码
    return a + b

# 练习2: 判断一个数是否为偶数
def exercise2(num):
    """判断一个数是否为偶数"""
    # 请在此处编写代码
    return num % 2 == 0

# 练习3: 计算列表中所有元素的和
def exercise3(numbers):
    """计算列表中所有元素的和"""
    # 请在此处编写代码
    total = 0
    for num in numbers:
        total += num
    return total

# 练习4: 找出列表中的最大值
def exercise4(numbers):
    """找出列表中的最大值"""
    # 请在此处编写代码
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 练习5: 反转字符串
def exercise5(s):
    """反转字符串"""
    # 请在此处编写代码
    return s[::-1]

# 练习6: 统计字符串中字母的个数
def exercise6(s):
    """统计字符串中字母的个数"""
    # 请在此处编写代码
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count

# 练习7: 生成斐波那契数列
def exercise7(n):
    """生成前n个斐波那契数列"""
    # 请在此处编写代码
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 练习8: 判断一个数是否为质数
def exercise8(num):
    """判断一个数是否为质数"""
    # 请在此处编写代码
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 练习9: 合并两个有序列表
def exercise9(list1, list2):
    """合并两个有序列表"""
    # 请在此处编写代码
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

# 练习10: 计算阶乘
def exercise10(n):
    """计算n的阶乘"""
    # 请在此处编写代码
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 测试练习
print("=== 测试练习 ===")
print(f"练习1: 1 + 2 = {exercise1(1, 2)}")
print(f"练习2: 4是否为偶数? {exercise2(4)}")
print(f"练习3: [1, 2, 3, 4, 5]的和 = {exercise3([1, 2, 3, 4, 5])}")
print(f"练习4: [1, 5, 3, 9, 2]的最大值 = {exercise4([1, 5, 3, 9, 2])}")
print(f"练习5: 'hello'反转 = {exercise5('hello')}")
print(f"练习6: 'Hello123'中字母个数 = {exercise6('Hello123')}")
print(f"练习7: 前5个斐波那契数 = {exercise7(5)}")
print(f"练习8: 7是否为质数? {exercise8(7)}")
print(f"练习9: 合并[1, 3, 5]和[2, 4, 6] = {exercise9([1, 3, 5], [2, 4, 6])}")
print(f"练习10: 5的阶乘 = {exercise10(5)}")