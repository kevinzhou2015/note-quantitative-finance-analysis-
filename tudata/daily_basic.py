from tudata.tu_handler import *

def action():
    df = pro.daily_basic(ts_code='000156.SZ', start_date='20180101', end_date='20181201', 
    fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
    print(df)
    df.to_csv('tudata/daily_basic_000156.csv')