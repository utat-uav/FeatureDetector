import blob_detection
import os


#def calculating_gps_location(gps_coordinate, elevation, pitch_degree, orientation):
#	center_pixel


def main():
	cwd = os.getcwd()
	path = "..\\data\\frame11.jpg"
	print(path)
	blob_detection.detection(path)




if __name__ == "__main__":
	main()