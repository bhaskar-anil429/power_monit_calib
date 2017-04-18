# Distributed with a free-will license.
# https://www.controleverything.com
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)
####### change volt calib value over here

bus.write_byte_data(0x2A, 145, 38)
bus.write_byte_data(0x2A, 146,106)
bus.write_byte_data(0x2A, 147,38)
bus.write_byte_data(0x2A, 148,106)

##### change current calib value over here

#bus.write_byte_data(0x2A, 125, 71)
#bus.write_byte_data(0x2A, 126,43)
#bus.write_byte_data(0x2A, 127,71)
#bus.write_byte_data(0x2A, 128,43)


while True:


        data = bus.read_i2c_block_data(0x2A, 145, 4)

# Convert the data to 14-bits
        calibration_ch1 = (data[0] * 256 + data[1])

# Output data to screen
        print "Calibration On volt channel 1:%.3f" %calibration_ch1
# Convert the data to 14-bits
        calibration_ch2 = (data[2] * 256 + data[3])

# Output data to screen
        print "Calibration On Volt channel 2:%.3f" %calibration_ch2

############ current calibration read

        data = bus.read_i2c_block_data(0x2A, 125, 4)

# Convert the data to 14-bits
        calibration_ch1 = (data[0] * 256 + data[1])

# Output data to screen
        print "Calibration On current channel 1:%.3f" %calibration_ch1
# Convert the data to 14-bits
        calibration_ch2 = (data[2] * 256 + data[3])

# Output data to screen
        print "Calibration On current channel 2:%.3f" %calibration_ch2


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
        print"\n"
