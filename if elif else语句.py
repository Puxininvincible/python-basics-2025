'''if int(input("请输入你的身高："))<120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级（1-5）："))>3:
    print("VIP级别大于3，可以免费")
elif int(input("请告诉我今天几号："))==1:
    print("今天是1号免费日，可以免费")
else:
   print("不好意思，条件都不满足，需要买票10元")'''
#练习
num=5
if int(input("请输入第一次猜想的数字："))==num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次:"))==num:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次:")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry，全部猜错了，我想的是：5")
