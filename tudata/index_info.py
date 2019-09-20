from tudata.tu_handler import *
def action():
    df = pro.index_basic(market='SW')
    print(df)
    df.to_csv('tudata/index_info.csv')