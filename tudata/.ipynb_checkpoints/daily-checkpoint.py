from tudata.tu_handler import *

def action():
    df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181201')
    df.to_csv('tudata/daily_000001.csv')