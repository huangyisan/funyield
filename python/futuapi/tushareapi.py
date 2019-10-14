import tushare as ts

df = ts.get_realtime_quotes('600000') #Single stock symbol
# df = ts.get_tick_data('600000',date='2019-10-14',src='tt')
# print(df.tail(100))
print(df[['code','name','price','bid','ask','volume','amount','time']])

# ts.set_token('daddc1dafa8c960707c5d9322901cddc1e42cebb978a8c58c86d30c3')
# pro = ts.pro_api()
# df = pro.daily(ts_code='600000.SH', start_date='20191014', end_date='20191014')
# print(df)
#
