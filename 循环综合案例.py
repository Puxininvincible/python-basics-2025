money=10000
# for循环对员工发工资
for i in range(1,21):
    import random
    score=random.randint(1, 10)

    if score<5:
        print(f"员工{i}绩效分{score}，不满足，不发工资")
        # continue跳过发放
        continue
    # 要判断余额足不足
    if money>=1000:
        money-=1000
        print(f"员工{i}，满足条件发放工资1000，公司账户余额：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再来")
        # break结束发放
        break