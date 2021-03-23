# Module Imports
import mariadb
import sys
import time

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="airbox",
        password="password",
        host="127.0.0.1",
        port=3306,
        database="db_airbox"
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

#insert information
try: 
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S", localtime)
    print(result)
    cur.execute("INSERT INTO `Data` (`time`, `pm10`, `formaldehyde`, `vocs`, `co2`, `temp`, `humidity`, `battery`, `runtime`, `air3um`, `air5um`, `air10um`, `air25um`, `air50um`, `air100um`) VALUES ('?', '?', '?', '?', '?', '?','?','?','?','?','?','?','?','?','?');",(str(result),20,30,40,50,60,70,80,90,100,110,111,112,113,114))
except mariadb.Error as e: 
    print(f"Error: {e}") 
conn.commit() 
conn.close()
#Adding Data
#ex.INSERT INTO `Data` (`time`, `pm10`, `formaldehyde`, `vocs`, `co2`, `temp`, `humidity`, `battery`, `runtime`, `air3um`, `air5um`, `air10um`, `air25um`, `air50um`, `air100um`) VALUES ('2021-03-22 00:00:00', '10', '30', '55', '55', '66', '77', '88', '99', '10', '11', '12', '13', '14', '15');

   

