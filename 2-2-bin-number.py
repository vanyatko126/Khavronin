import RPi.GPIO as GPIO
import time 
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
voltage = []
nums = [0, 5, 32, 64, 127, 255, 256]

def bin_translator(num, delay):
    number = [0 for i in range(8)]
    d_num = num % 256
    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])
        i -= 1

    print("{} --> {}".format(num, number))


    GPIO.output(dac, number)
    volt = float(input())
    voltage.append(volt)

    return 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in nums:
    bin_translator(i, 10)

x = [0, 5, 32, 64, 127, 255]
y = [0, 0.113, 0.458, 0.865, 1.669, 3.236]

plt.plot(x, y)
plt.show()
print(voltage)

GPIO.output(dac, 0)
GPIO.cleanup()