# print("hello",end='')
# print("hello",end='')
# print("hello\t world")
# print("itheima\t best")
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()#就是输出一个换行
