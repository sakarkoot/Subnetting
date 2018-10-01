'''

Author : Sakar Koot.

Licences :

Date Created : 28 september 2018.

'''

from math import *

#### Methods ##################
def utility(binary_ip_int):
    temp =""
    index = 0
    _ip = ["", "", "", ""]
    for i in range(32):
        _ip[int(i/8)] = _ip[int(i/8)]+str(binary_ip_int[int(i)])

    _ip_decimal = []
    for i in range(4):
        _ip_decimal.append(int(_ip[i],2))

    for i in range(4):
        if (i != 3):
            print(str(_ip_decimal[i]) + ".", end="")

        else:
            print(str(_ip_decimal[i]))
###################################

print("******  SUBNETTING DEMO USING PYTHON  ********\n")
ip = input("Enter the ip : ")
n = input("\nEnter the total number of subnets : ")
ip_array = ip.split(".")
binary_ip = ""

### Binary Conversion ##########
for i in range(4):
    binary_ip = binary_ip + str(bin(int(ip_array[i]))[2:].zfill(8))
print("\nBinary format of the given IP : ")
print(binary_ip)

###### Host ID bits calculation and other stuff.. ####
network_bits = 0
if int(ip_array[0]) < 127:
    network_bits = 24
elif int(ip_array[0]) >127 & int(ip_array[0])<191:
    network_bits = 16
else:
    network_bits = 8

bits =  network_bits- (int(log(int(n), 2)))
print("\nHost ID Bits : " + str(bits))

############# FIRST ADDRESS ###############

binary_ip_int_first = []
for i in range(32):
    binary_ip_int_first.append(int(binary_ip[i]))
for i in range(31, 31 - bits, -1):
    binary_ip_int_first[i] = binary_ip_int_first[i] & 0

############# LAST ADDRESS  ###############

binary_ip_int_last = []
for i in range(32):
    binary_ip_int_last.append(int(binary_ip[i]))
for i in range(31, 31 - bits, -1):
    binary_ip_int_last[i] = binary_ip_int_last[i] | 1

########## IP ADDRESSES  ####################
print("\n############   Details of the Subnet in which the given IP ADDRESS is..  ############\n")

print("First IP of Subnet : ", end="")
first_ip_decimal = utility(binary_ip_int_first)

print("Last IP of subnet : ", end="")
last_ip_decimal = utility(binary_ip_int_last)

print("########################################################################################")
