#语法1 range(num)
# for x in range(10):
#     print(x)

#语法2 range(num1,num2)
# for x in range(5,10):
#从5开始到10结束（不包含10本身）的数字序列，数字间隔是1
#     print(x)

#语法3 range（num1,num2,step）
# for x in range(5,10,2):
#     print(x)

# for x in range(10):
#     print("送玫瑰花")

count=0
for x in range(1,100):
    if x%2==0:
        count+=1
print(f"1到100（不含100本身）范围内，有{count}个偶数")

