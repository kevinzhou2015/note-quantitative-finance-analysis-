from tudata.tu_handler import *

def action():
    df = ts.pro_bar(ts_code='000156.SZ', adj='qfq', 
    start_date='20180101', end_date='20181201')
    print(df)
    df.to_csv('tudata/daily_000156.csv')