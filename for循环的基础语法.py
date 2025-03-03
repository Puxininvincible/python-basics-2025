# name="itheima"
# for x in name:
#     #将name的内容，挨个取出赋予x临时变量
#     print(x)
name="itheima is a brand of itcast"
#用来统计有多少个a
count=0
for x in name:
    if x=="a":
        count+=1
print(f"itheima is a brand of itcast中含有：{count}个字母a")