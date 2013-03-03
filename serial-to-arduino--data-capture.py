#serialtoarduino2.py

import serial
ser = serial.Serial('/dev/tty.usbserial-A700dB2V', 115200, timeout = 2)


def main():
	outfile=open("STMdata.csv","w") 
	point = [] #initialize point as a blank array
	
	header = 0
	while(header < 32768):
		print "looking for header data..."
		temp_var = ser.read(2)
		if len(temp_var)>0:
			(header_bg, header_sm) = temp_var
			header_sm=ord(header_sm)
			header_bg=ord(header_bg)
			header=header_sm + (header_bg << 8)
			
	print "found header: " 
	print header
	outfile.write('header: ')
	outfile.write(str(header))
	outfile.write('\n')
	
	
	data = 0		
	while(data < 32768):
#		import pdb; pdb.set_trace()
		temp_var = ser.read(2)
		if len(temp_var)>1:
			(data_bg, data_sm) = temp_var
			data_sm=ord(data_sm)
			data_bg = ord(data_bg)
			data_bg = data_bg << 8
			data = data_sm + data_bg
		
	
			if len(point) == 3:
				outfile.write(','.join(point))
				outfile.write('\n')
				point = []
									
			point.append(str(data))

	outfile.write('footer: ')
	outfile.write(','.join(point))
	outfile.write('\n')
	point = []
			
	outfile.close() #closes the file

main()
