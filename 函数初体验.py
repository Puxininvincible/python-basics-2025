str1="itheima"
str2="itcast"
str3="python"
count=0
for i in str1:
    count+=1
print(f"字符串{str1}的长度是：{count}")

count=0
for i in str2:
    count+=1
print(f"字符串{str2}的长度是：{count}")

count=0
for i in str3:
    count+=1
print(f"字符串{str3}的长度是：{count}")

#使用函数优化过程
def my_len(data):
    count=0
    for i in data:
        count+=1
    print(f"字符串{data}的长度是：{count}")
my_len(str1)
my_len(str2)
my_len(str3)
#函数：1已组织好的 2可重复使用 3针对特定功能