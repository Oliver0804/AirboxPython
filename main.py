import mariadb
import sys
import time
import serial



#serial 連線
ser = serial.Serial('/dev/ttyUSB0',baudrate = 19200,bytesize = 8,parity = 'N',stopbits = 1)
#準備發送資料
askcmd="\x55\xCD\x47\x00\x00\x00\x00\x00\x00\x01\x69\x0D\x0A"
packet = bytearray()
packet.append(0x55)
packet.append(0xCD)
packet.append(0x47)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x01)
packet.append(0x69)
packet.append(0x0D)
packet.append(0x0A)
print (packet)


#connect mariadb
conn= mariadb.connect(user="airbox",password="password",host="127.0.0.1",port=3306,database="db_airbox")
cur=conn.cursor()
cur.execute("select version()")
data =cur.fetchone()
#輸出DB版本
print (data)

while True:
    #發送詢問
    ser.write(packet)

    #接收資料解析
    feedback = ser.read(40)
    print('Data:', feedback)
    pm25=int(feedback[1])*255+int(feedback[2])
    pm10=int(feedback[3])*255+int(feedback[4])
    formaldehyde=int(feedback[5])*255+int(feedback[6])
    vocs=int(feedback[7])*255+int(feedback[8])
    co2=int(feedback[9])*255+int(feedback[10])
    temp=int(feedback[11])*255+int(feedback[12])
    humidity=int(feedback[13])*255+int(feedback[14])
    battery=int(feedback[15])*255+int(feedback[16])
    runtime=int(feedback[17])*255+int(feedback[18])
    air3um=int(feedback[19])*255+int(feedback[20])
    air5um=int(feedback[21])*255+int(feedback[22])
    air10um=int(feedback[23])*255+int(feedback[24])
    air25um=int(feedback[25])*255+int(feedback[26])
    air50um=int(feedback[27])*255+int(feedback[28])
    air100um=int(feedback[29])*255+int(feedback[30])
    print('pm2.5:',pm25)
    print('pm10:',pm10)
    print('formaldehyde:',formaldehyde/1000)
    print('vocs:',vocs/1000)
    print('co2:',co2)
    print('temp:',temp/100)
    print('humidity:',humidity/100)
    print('battery:',battery)
    print('runtime:',runtime)
    print('air3um:',air3um)
    print('air5um:',air5um)
    print('air10um:',air10um)
    print('air25um:',air25um)
    print('air50um:',air50um)
    print('air50um:',air50um)


    #獲取系統時間
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I:%M:%S", localtime)
    print(result)
    sql_cmd="INSERT INTO `Data` (`time`, `pm25`,`pm10`, `formaldehyde`, `vocs`, `co2`, `temp`, `humidity`, `battery`, `runtime`, `air3um`, `air5um`, `air10um`, `air25um`, `air50um`, `air100um`) VALUES ('%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d','%d')" % (result,pm25,pm10,formaldehyde,vocs,co2,temp,humidity,battery,runtime,air3um,air5um,air10um,air25um,air50um,air100um)
    print(sql_cmd)
    cur.execute(sql_cmd)
    conn.autocommit=True
    time.sleep(1)
