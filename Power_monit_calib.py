# Distributed with a free-will license.
# https://www.controleverything.com
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)
bus.write_byte(0x2A, 14)

while True:
        bus.write_byte(0x2A, 14)
        data = bus.read_i2c_block_data(0x2A, 14, 6)

# Convert the data to 24-bits
        current_ch1 = (data[0] * 65536 + data[1] * 256 + data[2])/1000.0

# Output data to screen
        print "Current On channel 1:%.3f" %current_ch1
# Convert the data to 24-bits
        current_ch2 = (data[3] * 65536 + data[4] * 256 + data[5])/1000.0

# Output data to screen
        print "Current On channel 2:%.3f" %current_ch2

        bus.write_byte(0x2A, 44)
        data = bus.read_i2c_block_data(0x2A, 44, 6)

# Convert the data to 24-bits
        voltage_ch1 = (data[0] * 65536 + data[1] * 256 + data[2])/1000.0

# Output data to screen
        print "Voltage On channel 1:%.3f" %voltage_ch1

# Convert the data to 24-bits
        voltage_ch2 = (data[3] * 65536 + data[4] * 256 + data[5])/1000.0

# Output data to screen
        print "Voltage On channel 2:%.3f" %voltage_ch2
        time.sleep(5)
