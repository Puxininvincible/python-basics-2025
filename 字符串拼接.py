from pyexpat.errors import messages

print("学IT来黑马"+"月薪过万")

name ="黑马程序员"
address="江西交通职业技术学院"
print(name,address)
#通过占位完成拼接
messages="学IT来:%s" %name
print(messages)
#通过占位完成数字和字符串拼接
class_num=57
avg_salary=16781
messages="Python大数据学科，北京%s期，毕业平均工资：%s" %(class_num,avg_salary)
print(messages)

name="传智播客"
setup_year=2006
stock_price=19.99
message="%s,成立于：%d,我今天的股价是：%f" %(name,setup_year,stock_price)
print(message)