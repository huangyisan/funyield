import futu as ft
quote_ctx = ft.OpenQuoteContext(host="127.0.0.1", port=11111)
# 上下文控制
quote_ctx.start()              # 开启异步数据接收
quote_ctx.set_handler(ft.TickerHandlerBase())  # 设置用于异步处理数据的回调对象(可派生支持自定义)

code = 'SH.600000'
quote_ctx.subscribe(code, [ft.SubType.RT_DATA])

# print(quote_ctx.get_stock_quote(code))  # 获取报价
# print(quote_ctx.get_rt_ticker(code))   # 获取逐笔
# print(quote_ctx.get_cur_kline(code, num=100, ktype=ft.KLType.K_DAY))   #获取当前K线
# print(quote_ctx.get_order_book(code))       # 获取摆盘
print(quote_ctx.get_rt_data(code)[-1])       # 获取分时数据
# print(quote_ctx.get_broker_queue(code))     # 获取经纪队列
# 停止异步数据接收
quote_ctx.stop()

# 关闭对象
quote_ctx.close()