#!/usr/bin/env python

import csv
import serial
import math
import sys

class Thermo:

	def reset(self):
		self.thermoData = []
		self.teensy = serial.Serial('/dev/ttyACM0', 9600)
		self.finalData = []

	def __init__(self):

		self.reset()

		print("Starting Temperature Measurements")
		print("Starting taking data")
		try:
			while True:
				lineStuff = self.teensy.readline().decode().split(",")
				print(lineStuff[0])
				self.thermoData.append( [ float(lineStuff[0]), float(lineStuff[1]), float(lineStuff[2]) ] )

		except KeyboardInterrupt:
			print("Termination of Datacollection")
			self.write_csv('thermo_0.csv', self.thermoData)
			print("Finished Writing CSV file, Terminating Program")
			# with open("thermo_0.csv", "r") as f:
			# 	for line in f:
					
			# 		cleanedLine = line.strip()
			# 		cleanedLine.replace("\"", "")
			# 		if cleanedLine: # is not empty
			# 			self.finalData.append(cleanedLine)
			# self.write_csv('thermo_0.csv', self.finalData)

			

		# r = rospy.Rate(100)
		# while( not (rospy.is_shutdown()) ):
		# 	rospy.sleep(0.1)	

		# self.write_csv('thermo_0.csv', self.thermoData)

		"""r = rospy.Rate(50)
        while not rospy.is_shutdown():
            # rospy.spinOnce()
            r.sleep() """ 


	def write_csv(self, filename, dictionary):
		with open(filename,'w', newline = '') as f:
			w = csv.writer(f)
			for row in dictionary:
				w.writerow(row)


if __name__ == '__main__':
	Thermo()