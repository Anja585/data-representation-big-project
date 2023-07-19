import mysql.connector
import dbconfig as cfg
db = mysql.connector.connect(
    host = cfg.mysql['host'],
    user = cfg.mysql['user'],
    password = cfg.mysql['password'],
    database = cfg.mysql['database']
)

cursor = db.cursor()
sql = '''create table ea_assets(
        isin_code varchar(20), 
        issuance_date varchar(20), 
        maturity_date varchar(20), 
        coupon_rate int, 
        denomination varchar(100), 
        primary key(isin_code));'''

cursor.execute(sql)

db.commit()
db.close()
cursor.close()