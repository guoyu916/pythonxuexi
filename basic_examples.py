# Python基础语法示例

# 1. 变量和数据类型
print("=== 变量和数据类型 ===")
# 整数
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数
height = 1.75
print(f"身高: {height}, 类型: {type(height)}")

# 字符串
name = "张三"
print(f"姓名: {name}, 类型: {type(name)}")

# 布尔值
is_student = True
print(f"是否学生: {is_student}, 类型: {type(is_student)}")

# 2. 列表
print("\n=== 列表 ===")
fruits = ["苹果", "香蕉", "橙子"]
print(f"水果列表: {fruits}")
print(f"第一个水果: {fruits[0]}")
print(f"水果数量: {len(fruits)}")

# 添加元素
fruits.append("草莓")
print(f"添加草莓后: {fruits}")

# 3. 字典
print("\n=== 字典 ===")
person = {
    "name": "李四",
    "age": 30,
    "city": "北京"
}
print(f"个人信息: {person}")
print(f"姓名: {person['name']}")
print(f"年龄: {person['age']}")

# 4. 条件语句
print("\n=== 条件语句 ===")
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 5. 循环
print("\n=== 循环 ===")
# for循环
print("for循环:")
for i in range(5):
    print(f"数字: {i}")

# while循环
print("\nwhile循环:")
count = 0
while count < 3:
    print(f"计数: {count}")
    count += 1

# 6. 函数
print("\n=== 函数 ===")
def greet(name):
    """打招呼函数"""
    return f"你好, {name}!"

print(greet("王五"))

# 7. 类
print("\n=== 类 ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我叫{self.name}, 今年{self.age}岁"

p = Person("赵六", 28)
print(p.introduce())

# 8. 异常处理
print("\n=== 异常处理 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误: 除数不能为零")
finally:
    print("异常处理结束")

print("\n基础语法示例结束！")