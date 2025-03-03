# i=0
# for i in range(1,101):
#     print(f"今天是向小美表白的第{i}天，加油坚持")
#
#     for j in range(1,11):
#         print(f"给小美送的第{j}朵玫瑰花")
#
#     print("小美，我喜欢你")
# print(f"第{i}天，表白成功")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j * i}\t", end='')
    print()