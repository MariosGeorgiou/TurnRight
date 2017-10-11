from __future__ import print_function
import time
from time import gmtime, strftime
import mraa
import sys
import math
import pyupm_i2clcd as lcd

count = 0

blueled = mraa.Gpio(2)
blueled.dir(mraa.DIR_OUT)

greenled = mraa.Gpio(3)
greenled.dir(mraa.DIR_OUT)

redled = mraa.Gpio(4)
redled.dir(mraa.DIR_OUT)

button = mraa.Gpio(5)
button.dir(mraa.DIR_IN)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(255,100,0)

touch = mraa.Gpio(8)
touch.dir(mraa.DIR_IN)

rotary = mraa.Gpio(7)
rotary.dir(mraa.DIR_IN)

lightPin=0
lum = mraa.Aio(lightPin)
lumVal = 0

f = open('tableau.csv', 'a')

while 1:
	lumVal = float(lum.read())

	if lumVal < 100:
		if touch.read() == 1:
			blueled.write(1)
			time.sleep(2)
			blueled.write(0)
			if rotary.read() == 1:
				greenled.write(1)
				print(strftime("%d-%m-%y %H:%M:%S", gmtime()) + "    Turnstile 2  IN   " + "M0003453438")
				f.write(strftime("%d-%m-%y %H:%M:%S", gmtime()) +","+ " Turnstile 2 IN" +",1 "+", "+","+ "M0003453438" + "\n")
				f.close()
				f = open('tableau.csv', 'a')
				count = count + 1
				time.sleep(2)
				greenled.write(0)
			else :
				redled.write(1)
				time.sleep(1)
				redled.write(0)
		while button.read() == 1:
			blueled.write(1)
			if rotary.read() == 1:
				greenled.write(1)
				print(strftime("%d-%m-%y %H:%M:%S", gmtime()) + "    Turnstile 2  IN   " + "0")
				f.write(strftime("%d-%m-%y %H:%M:%S", gmtime()) +","+ " Turnstile 2 IN" +", 1"+", "+ ", 0" + "\n")
				f.close()
				f = open('tableau.csv', 'a')
				count = count + 1
				time.sleep(2)
				greenled.write(0)
				blueled.write(0)

	if lumVal >= 100:
		if touch.read() == 1:
			blueled.write(1)
			time.sleep(2)
			blueled.write(0)
			if rotary.read() == 1:
				greenled.write(1)
				print(strftime("%d-%m-%y %H:%M:%S", gmtime()) + "    Turnstile 4  OUT  " + "M0003453438")
				f.write(strftime("%d-%m-%y %H:%M:%S", gmtime()) +","+ " Turnstile 4 OUT" +", "+", 1" +","+ "M0003453438" + "\n")
				f.close()
				f = open('tableau.csv', 'a')
				count = count - 1
				time.sleep(2)
				greenled.write(0)
			else :
				redled.write(1)
				time.sleep(1)
				redled.write(0)
		while button.read() == 1:
			blueled.write(1)
			if rotary.read() == 1:
				greenled.write(1)
				print(strftime("%d-%m-%y %H:%M:%S", gmtime()) + "    Turnstile 4  OUT  " + "0")
				f.write(strftime("%d-%m-%y %H:%M:%S", gmtime()) +","+ " Turnstile 4 OUT" +","+ ""+", 1" +","+ "0" + "\n")
				f.close()
				f = open('tableau.csv', 'a')
				count = count - 1
				time.sleep(2)
				greenled.write(0)
				blueled.write(0)
				
	blueled.write(0)
	lcdDisplay.setCursor(0, 0)
	lcdDisplay.write("Total: " + str(count) +"     ")
