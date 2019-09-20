from tudata.tu_handler import *

#assets资产类别：E股票 I沪深指数 C数字货币 FT期货 FD基金 O期权 CB可转债（v1.2.39），默认E
#adj:复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
def action():
    df = ts.pro_bar(ts_code='000300.SH', asset='I',adj='qfq', 
    start_date='20180101', end_date='20181201')
    print(df)
    df.to_csv('tudata/HS300.csv')