from WindPy import w

w.start() # 默认命令超时时间为120秒，如需设置超时时间可以加入waitTime参数，例如waitTime=60,即设置命令超时时间为60秒  

w.isconnected() # 判断WindPy是否已经登录成功

w.stop() # 当需要停止WindPy时，可以使用该命令
          # 注： w.start不重复启动，若需要改变参数，如超时时间，用户可以使用w.stop命令先停止后再启动。
          # 退出时，会自动执行w.stop()，一般用户并不需要执行w.stop  

    # 获取日时间序列函数WSD
history_data=w.wsd("010107.SH",
                   "sec_name,ytm_b,volume,duration,convexity,open,high,low,close,vwap", 
                   "2018-06-01", "2018-06-11", "returnType=1;PriceAdj=CP", usedf=True) 
# returnType表示到期收益率计算方法，PriceAdj表示债券价格类型‘
history_data[1].head()

