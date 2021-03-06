import blob_detection
import os
import math


def determiningViability():
	#Constants
	#We can find the value of the angle of view from an online calculator
	#this is one way
	lengthline = 500
	distancetoline = 100
	angleofview = math.atan((lengthline/2)/distancetoline)

	#this is another
	#measured in millimeters
	sensorwidth = .033
	focallength = .050
	calculatedFocal = 2*math.atan((sensorwidth)/(2*focallength))
	print("Calculated Focal Length: " + str(calculatedFocal))



	pitch_angle = 10
	#negative_angle
	marginOfError = 1.5
	numberOfPixels = 5120
	smallestPixels = 6
	metersPerPixel = 0.008333


	#Areas
	print("The focal length: " + str(calculatedFocal*(180/math.pi)))
	#Altitude requirement calculation
	altitude = (metersPerPixel*numberOfPixels) / (2*math.tan(calculatedFocal/2))*2
	print(altitude)
	totalArea = 500000

	totalAreaCovered = 2*math.tan(calculatedFocal/2)*altitude/1.3333
	#meters per second
	speed = 14

	print("Total area covered: " + str(totalAreaCovered))
	areaPerSecond = speed*totalAreaCovered
	print(areaPerSecond)
	totalTime = totalArea/areaPerSecond
	print("Total time: " + str(totalTime))
	print("Time in minutes: " + str(totalTime/60))

	print(calculatedFocal)



def  calculateFocal():
	#measured in millimeters
	sensorwidth = .033
	focallength = .050
	calculatedFocal = 2*math.atan((sensorwidth)/(2*focallength))
	return calculatedFocal


def calculate_distance(elevation):

	focal = calculateFocal()

	widthpicture = 1920
	heightpicture = 1080
	pixelpointx = 1567
	pixelpointy = 952
	pixelangle = (calculatedFocal/2)

	xcomp = (pixelpointx - (widthpicture/2))/(widthpicture/2)
	ycomp = (pixelpointy - (heightpicture/2))/(heightpicture/2)
	xdistance = xcomp*elevation*math.tan((calculatedFocal/2))
	ydistance = ycomp*elevation*math.tan((calculatedFocal/2))

	print("Distance from x coordinates is: " + str(xdistance))
	print("Distance from y coordinates is: " + str(ydistance))


def calculate_distance_pitch(elevation):
	widthpicture = 1920
	heightpicture = 1080

	elevation = 1000
	pixelpointx = 1567
	pixelpointy = 952
	pixelangle = (calculatedFocal/2)

	xcomp = (pixelpointx - (widthpicture/2))/(widthpicture/2)
	ycomp = (pixelpointy - (heightpicture/2))/(heightpicture/2)

	xdistance = elevation*math.tan(math.atan(((xcomp*math.tan(calculatedFocal/2))/5000))+15*(math.pi/180))
	print("Distance from x coordinates is: " + str(xdistance))






def demoDetection():
	directory = "/test/"
	save_directory = "/saved/"
	path = os.getcwd()
	print(path)
	for item in os.listdir(path + directory):
		print(item)
		test_path = path + directory + item
		save_path = path + save_directory + item
		image = blob_detection.detection_return(test_path, save_path, item)





#def calculating_gps_location(gps_coordinate, elevation, pitch_degree, orientation):
#	center_pixel


#def distancefromcenter():


def main():
	demoDetection()


	# cwd = os.getcwd()
	# path = "try/im0346.jpg"
	# print(path)
	# blob_detection.detection(path)




if __name__ == "__main__":
	main()