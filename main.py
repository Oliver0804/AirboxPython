import mariadb
import sys
import time
conn= mariadb.connect(user="airbox",password="password",host="127.0.0.1",port=3306,database="db_airbox")
cur=conn.cursor()
cur.execute("select version()")
data =cur.fetchone()
print (data)

localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S", localtime)
print(result)
sql_cmd="INSERT INTO `Data` (`time`, `pm10`, `formaldehyde`, `vocs`, `co2`, `temp`, `humidity`, `battery`, `runtime`, `air3um`, `air5um`, `air10um`, `air25um`, `air50um`, `air100um`) VALUES ('2020-04-12 12:34:45', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14')"
cur.execute(sql_cmd)
conn.autocommit=True
