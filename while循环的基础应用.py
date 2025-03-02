from itertools import count

from 判断语句综合案例 import guess_num

i=0
while i<100:
    print("小美，我喜欢你")
    i+=1


#练习:求1—100累加的和
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(f"1-100累加的和是:{sum}")


#案例：无限次猜数字
import random
num=random.randint(1,100)
#记录猜测多少次
count=0
#通过一个布尔类型的变量，做循环是否继续的标记
falg=True
while falg:
    guess_num=int(input("请输入你猜测的数字："))
    count+=1
    if guess_num==num:
        print("猜中了")
        #终止循环条件
        falg=False
    else:
        if guess_num>num:
            print("你猜的大了")
        else:
            print("你猜的小了")
print(f"你总共猜测了{count}次")