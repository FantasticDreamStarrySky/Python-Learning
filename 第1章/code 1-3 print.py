# 年
year = 2024
# 月
month = 2
# 日
day = 2
# 星期
week = "一"
# 天气
weather = "晴"
# 气温
temperature = 15.4

print("我是FDSS")

"""
sep：设置多个内容之间的分隔符，默认分隔符空格。
end：设置结束符，默认结束符'\n'
"""
print(year, "年，我要减肥", sep="", end="\n\n")
print(year, "年，我要读100本书", sep="", end="\n\n")
print(year, "年，我要去10个城市旅游", sep="", end="\n\n")

print("今天是 %d 年 %02d 月 %02d 日，星期 %s ，今天的天气 %s ，气温 %.1f 度" % (
    year, month, day, week, weather, temperature))
