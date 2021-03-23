import serial

#ser = serial . Serial('/dev/tty.usbserial-14130', # Device name varies
ser = serial . Serial('/dev/ttyUSB0', # Device name varies
baudrate = 19200,
bytesize = 8,
parity = 'N',
stopbits = 1)

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
ser.write(packet)

print (packet)

ser.write(packet)
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


ser.close()
