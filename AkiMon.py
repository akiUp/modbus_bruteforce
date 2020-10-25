
from pyModbusTCP.client import ModbusClient
from time import sleep
import sys
import argparse
port = "502"
#Function to continiously reads given register
def monitor_register(target_ip,port,address,delay,reg):
	while True:
		client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=1)
		if reg == "Holding":
			data=client.read_holding_registers(address,1)
		if reg == "Input":
			data=client.read_input_registers(address,1)
		if reg == "Discrete":
			data=client.read_discrete_inputs(address,1)
		if reg == "Coil":
			data=client.read_coils(address,1)
		if data:
			print(f'{reg} register at address {address} has value {data}')
		#print ('.', end='')
		client.close()
		sleep(delay)
#need to implement timeout
#Parsing CLI arguments
my_parser = argparse.ArgumentParser(description='Pass the input IP Address')
my_parser.add_argument('-i','--ip', action='store', type=str,required=True, help='Target IP Address')
my_parser.add_argument('-r','--reg', action='store', type=str,required=True, help='Specify register type - C Coil, - H Holding, -I Input, -D Discrete' )
my_parser.add_argument('-a','--addr', action='store', type=int,required=True, help='Specify register address to end search' )
my_parser.add_argument('-d','--delay', action='store', type=int,required=True, help='Specify delay in seconds' )
args = my_parser.parse_args()

target_ip = args.ip
function = args.reg
address = args.addr
delay = args.delay

print (f'You about to run continious probe of {function} register on adress {address} of host {target_ip} each {delay} second')
input("Press enter to continue")
if function =="C":
	monitor_register(target_ip,port,address,float(delay),reg="Coil") #run function
if function =="H":
	monitor_register(target_ip,port,address,float(delay),reg="Holding") #run function
if function =="D":
	monitor_register(target_ip,port,address,float(delay),reg="Discrete") #run function
if function =="I":
	monitor_register(target_ip,port,address,float(delay),reg="Input") #run function
print ()


