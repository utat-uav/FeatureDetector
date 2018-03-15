import blob_detection
import os
import math



#Constants
#We can find the value of the angle of view from an online calculator
#this is one way
lengthline = 500
distancetoline = 100
angleofview = math.atan((lengthline/2)/distancetoline)

#this is another
#measured in millimeters
sensorwidth = .033
focallength = .015
calculatedFocal = 2*math.atan((sensorwidth/2)/(2*focallength))
print("Calculated Focal Length: " + str(calculatedFocal))



def calculate_distance(elevation):

	widthpicture = 1920
	heightpicture = 1080

	elevation = 1000
	pixelpointx = 1567
	pixelpointy = 952
	

	xcomp = (pixelpointx - (widthpicture/2))/(widthpicture/2)
	ycomp = (pixelpointy - (heightpicture/2))/(heightpicture/2)
	xdistance = xcomp*elevation*math.tan((calculatedFocal/2))
	ydistance = ycomp*elevation*math.tan((calculatedFocal/2))

	print("Distance from x coordinates is: " + str(xdistance))
	print("Distance from y coordinates is: " + str(ydistance))



elevation_test = 500
calculate_distance(elevation_test)





#def calculating_gps_location(gps_coordinate, elevation, pitch_degree, orientation):
#	center_pixel


#def distancefromcenter():


def main():
	cwd = os.getcwd()
	path = "..\\data\\frame11.jpg"
	print(path)
	blob_detection.detection(path)




#if __name__ == "__main__":
#	main()