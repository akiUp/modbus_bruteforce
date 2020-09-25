#Function to read all the registers based on the parameter received
from pyModbusTCP.client import ModbusClient
from time import sleep
import sys
import argparse
port = "502"

def read_valid_registers(target_ip,port,reg):
	result = False
	print (f'\n=====Polling remote server for {reg}:=====')
	for i in range(start_reg, end_reg):
		client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=10)
		if reg == "hold":
			data=client.read_holding_registers(i,1)
		if reg == "input":
			data=client.read_input_registers(i,1)
		if reg == "discrete":
			data=client.read_discrete_inputs(i,1)
		if reg == "coil":
			data=client.read_coils(i,1)
		if data:
				result = True
				print(f'\nValid Registers {reg} detected at {i} with value {data}')
		client.close()
		print ('/', end='')
		sleep(0.1)
#	return valid_list,data_list,permission_list
	if result != True: 
		print(f'\n No Valid Registers detected in specified range')

my_parser = argparse.ArgumentParser(description='Pass the input IP Address')
my_parser.add_argument('-i','--ip', action='store', type=str,required=True, help='Target IP Address')
my_parser.add_argument('-s','--sreg', action='store', type=int,required=True, help='Specify register address to start search' )
my_parser.add_argument('-e','--ereg', action='store', type=int,required=True, help='Specify register address to end search' )
args = my_parser.parse_args()

target_ip = args.ip
start_reg = args.sreg
end_reg = args.ereg


print (f'\n#### Modbus Scan of {target_ip} started with range from {start_reg} till {end_reg} #########')
read_valid_registers(target_ip,port,reg="coil") #run function
read_valid_registers(target_ip,port,reg="hold") #run function
read_valid_registers(target_ip,port,reg="discrete") #run function
read_valid_registers(target_ip,port,reg="input") #run function
print (f'\n#### Modbus Scan of {target_ip} completed #########')
print ()


