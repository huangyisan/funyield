import futu as ft
import time
quote_ctx = ft.OpenQuoteContext(host="127.0.0.1", port=11111)


code = 'SH.600000'
code_list = ['SH.600000', 'SH.600519']

def get_now_price():
    quote_ctx.subscribe(code_list, [ft.SubType.QUOTE])
    data = quote_ctx.get_stock_quote(code_list)
    title = list(data[-1])
    print(title)
    print(list(data[-1].iloc[:, 8]))
    # print([i for i in list(data)])
    print(data)

def get_max_volume():
    quote_ctx.subscribe(code_list, [ft.SubType.RT_DATA])
    for i in code_list:
        data = quote_ctx.get_rt_data(i)
        index = list(data)
        print(max(list(quote_ctx.get_rt_data(i)[-1].iloc[:, 7])))
        print(index)

# 上下文控制
quote_ctx.start()  # 开启异步数据接收
quote_ctx.set_handler(ft.TickerHandlerBase())  # 设置用于异步处理数据的回调对象(可派生支持自定义)

n=10
while n:
    get_now_price()
    n-=1
    time.sleep(10)

# 停止异步数据接收
quote_ctx.stop()

# 关闭对象
quote_ctx.close()