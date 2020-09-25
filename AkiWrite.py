from pyModbusTCP.client import ModbusClient
import sys
from time import sleep
import argparse
port = "502"

#Function to write single coil
def write_single_coil(target_ip,port,target_reg, value):
	client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=10)
	result=client.write_single_coil(int(target_reg),int(value)) # Writing to coil
	client.close()
	sleep(0.1)
	client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=10)
	data=client.read_coils(int(target_reg),1) # Reading the coil state
	if result==True:
		print(f'Write to coil {target_reg} successful! \nCurrent value:{data}')
	else: print ('Write operation failed')
	client.close()


#Function to write single Holding Register
def write_single_hold(target_ip,port,target_reg, value):
	client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=10)
	result=client.write_single_register(int(target_reg),int(value)) # Writing to holding reg
	client.close()
	sleep(0.1)
	client=ModbusClient(host=target_ip,port=port,auto_open=True,auto_close=True,timeout=10)
	data=client.read_holding_registers(int(target_reg),1) # reading holding reg 
	if result==True:
		print(f'Write to holding reg {target_reg} successful! \nCurrent value:{data}')
	else: print ('Write operation failed')
	client.close()


#Parse the input parameters
my_parser = argparse.ArgumentParser(description='Pass the input IP Address')
my_parser.add_argument('-i','--ip', action='store', type=str,required=True, help='Target IP Address')
my_parser.add_argument('-t','--tsel', action='store', type=str,required=True, help='Specify register type (H for Holding, C for Coil):' )
my_parser.add_argument('-r','--reg', action='store', type=int,required=True, help='Specify one target register:')
my_parser.add_argument('-v','--val', action='store', type=int,required=True, help='Value to write (integer):')
args = my_parser.parse_args()

target_ip = args.ip
target_select = args.tsel
target_reg = args.reg
value= args.val


# Disclaimer
print (f'################## WARNING!!! ################################ \n# The output of this script is very INVASIVE to the process! # \n######### DO NOT try it on production system! ################\n##############################################################')
input("Press enter to continue")
if target_select =="C":
	print (f'Executing write command with following parameters: \n Target IP :{target_ip} \n Register type {target_select} \n Address: {target_reg} \n Value: {value}')
	write_single_coil(target_ip,port,target_reg, value)
if target_select =="H":
	print (f'Executing write command with following parameters: \n Target IP :{target_ip} \n Register type {target_select} \n Address: {target_reg} \n Value: {value}')
	write_single_hold(target_ip,port,target_reg, value)

