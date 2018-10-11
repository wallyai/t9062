# MIT License
#
# Copyright (c) 2018 WallyAI
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#!/usr/bin/env python

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

def Read_Humid():

 
# T9062 Humidity & Temperature sensor,  address, 0x28 (40)
# Read data back from 0x28(40), with offset 0, 4 bytes)
# 4 bytes

    data = bus.read_i2c_block_data(0x28, 0, 4)

# humidity = (rH_High [5:0] x 256 + rH_Low [7:0]) / 16384 x 100
    humidity = (((data[0] & 0x3F ) << 8) + data[1]) / 16384.0 * 100.0
#  temperature = (Temp_High [7:0] x 64 + Temp_Low [7:2]/4 ) / 16384 x 165 - 40
    temperature = ((data[2]  * 64) +(data[3] >> 2 )) / 16384.0 * 165.0 - 40.0
    return [humidity, temperature]

try: 

    while True:
          list_result = Read_Humid()
          print "Humidity: %3.3f %%rH, Temperature: %3.2f C" %(list_result[0],list_result[1]) # Read 4 Byte DF
          time.sleep(0.5)

except:
    time.sleep(0.01)
