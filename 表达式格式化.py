print("1*1 的结果是：%d" %(1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))
#练习
name = "传智播客"
stock_code='003032'
stock_price=19.99
stock_price_daily_growth_factor=1.2
growth_day=7
stock_now=stock_price * stock_price_daily_growth_factor ** growth_day
print(f"公司：{name},股票代码：{stock_code}，当前股价：{stock_price}")
print( "每日增长系数是:%.1f，经过%d天增长后，股票达到了：%.2f" %(stock_price_daily_growth_factor,growth_day,stock_now))
