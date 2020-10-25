## ModbusTCP bruteforce
>Set of simple Python scripts to locate valid ModbusTCP registers and modify them

>Based on original script by https://github.com/nallamuthu/ModBus

use nmap scan to locate ModbusTCP devices in your network
```shell
nmap -p 502 your_subnet
```
## AkiScan.py
Reckon script to run exhaustive scan on specified modbus registers range and find valid ones with current values.

> Important! The Modbus addressing has so-called 0-starting and 1-starting scheme. This script assume the use of 0-starting scheme. If you observe register addresses shifted by 1, it mean device uses 1-starting scheme.

Current version of script will scan only registers from device with unit ID 1.

<a href="https://github.com/akiUp/modbus_brutforce"><img src="https://github.com/akiUp/modbus_bruteforce/blob/master/AkiScan.PNG" title="Bruteforce script" alt="Read"></a>

## AkiMon.py
Continiously monitor selected register value

> Important! The Modbus addressing has so-called 0-starting and 1-starting scheme. This script assume the use of 0-starting scheme. If you observe register addresses shifted by 1, it mean device uses 1-starting scheme.

Current version of script will scan only registers from device with unit ID 1.

<a href="https://github.com/akiUp/modbus_brutforce"><img src="https://github.com/akiUp/modbus_bruteforce/blob/master/AkiMon.PNG" title="Monitor script" alt="Monitor"></a>

```shell
python3 AkiMon.py -h
usage: AkiMon.py [-h] -i IP -r REG -a ADDR -d DELAY

Pass the input IP Address

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Target IP Address
  -r REG, --reg REG     Specify register type - C Coil, - H Holding, -I Input, -D Discrete
  -a ADDR, --addr ADDR  Specify register address to end search
  -d DELAY, --delay DELAY Specify delay in seconds
```

## AkiWrite.py 
Will write specified value in selected register

> Important! The Modbus addressing has so-called 0-starting and 1-starting scheme. This script assume the use of 0-starting scheme. If you observe register addresses shifted by 1, it mean device uses 1-starting scheme.

Current version of script will write only registers to device with unit ID 1.
### The output of this script could be very INVASIVE to the controlled process!!!

### Please, do not use it on production equipment!!!
- Example of writing to coil

<a href="https://github.com/akiUp/modbus_brutforce"><img src="https://github.com/akiUp/modbus_bruteforce/blob/master/AkiWrite Coils.PNG" title="Bruteforce script" alt="writecoil"></a>
- Example of writing to Holding register

<a href="https://github.com/akiUp/modbus_brutforce"><img src="https://github.com/akiUp/modbus_bruteforce/blob/master/AkiWrite Holding.PNG" title="Bruteforce script" alt="writeHold"></a>
## Installation
Script uses pyModbusTCP and argaprse libraries

Python 3 example of lib installation
```shell
python3 -m pip install pyModbusTCP
python3 -m pip install argparse
```
