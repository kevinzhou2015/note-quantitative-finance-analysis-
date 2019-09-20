from tudata.tu_handler import *
def action():
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(data)
    data.to_csv('tudata/stock_info.csv')

