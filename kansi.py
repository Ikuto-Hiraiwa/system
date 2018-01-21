
import sys
import os
import RPi.GPIO as GPIO
import subprocess
import datetime
from time import sleep
from time import time
import picamera

count = 0
count_i = 0

d = datetime.datetime.today()

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.HIGH)

os.chdir('/var/www/html/my-page/Movie_Data')

dir_name = str(d.year) + '.' + str(d.month) + '.' + str(d.day)

if os.path.isdir(dir_name):
	print ('Exist!')
	print (dir_name)
else:
	print ('No!')
	os.mkdir('/var/www/html/my-page/Movie_Data/'+ dir_name)

os.chdir('/var/www/html/my-page/Movie_Data/' + dir_name)

flag = 0

while(True):
	while(GPIO.input(21)):
		flag = 0
		print (GPIO.input(14))
		if GPIO.input(14) == GPIO.HIGH and count == 0:
				camera = picamera.PiCamera(resolution=(320,240),framerate=30)
				camera.start_recording('video.h264')
				camera.vflip = True
				count = 1
		sleep(1)	
		if GPIO.input(14) == GPIO.LOW and count == 1:
			count = 0
			
			filename = str(d.year) +'.' +  str(d.month) + '.' + str(d.day) + '.' + str(d.hour) + ':' + str(d.minute)
			if os.path.isfile(filename + '.mp4') == True:
				filename =  str(count_i) + '_' + filename
				count_i += 1
			else:
				count_i = 0
		
			cmd = "MP4Box -fps 30 -add video.h264 " + filename + ".mp4"
			subprocess.call(cmd,shell=True)
			camera.close()
			flag = 1
			break

	if count == 1:
		count = 0
		filename = str(d.year) +'.' +  str(d.month) + '.' + str(d.day) + '.' + str(d.hour) + ':' + str(d.minute)
		if os.path.isfile(filename + '.mp4') == True:
			filename =  str(count_i) + '_' + filename
			count_i += 1
		
		else:
			count_i = 0
		cmd = "MP4Box -fps 30 -add video.h264 " + filename + ".mp4"
		subprocess.call(cmd,shell=True)
		camera.close()
		

	sleep(0.5)
	if(flag==0):
		print ('Surveillance Camera OFF.')
		flag = 1
	



GPIO.cleanup()

