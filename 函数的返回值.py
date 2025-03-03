# def add(a,b):
#     result= a+b
#     return result#return后的代码不会执行
#
# r=add(5,6)
# print(r)

#None类型 空
def say_hi():
    print("hello")

result=say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

def say_hi2():
    print("hello")
    return None

result=say_hi2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")
#None用于if判断
def check_age(age):
    if age>18:
        return "SUCCESS"
    else:
        return  None
result=check_age(17)
if not result:
    #进入if表示result是None值 也就是false
    print("未成年，不可以进入")

#None用于声明无初始内容的变量
name=None