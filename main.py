import mariadb
import sys

conn= mariadb.connect(user="airbox",password="password",host="127.0.0.1",port=3306,database="db_airbox")
cur=conn.cursor()
cur.execute("select version()")
data =cur.fetchone()
print (data)

conn.autocommit=True
cur.execute("INSERT INTO `Data` (`time`, `pm10`, `formaldehyde`, `vocs`, `co2`, `temp`, `humidity`, `battery`, `runtime`, `air3um`, `air5um`, `air10um`, `air25um`, `air50um`, `air100um`) VALUES ('2021-03-31 00:00:00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14')")

