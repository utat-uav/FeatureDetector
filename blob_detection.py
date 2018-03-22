# Standard imports
import cv2
import numpy as np;


def parameters():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 1
	params.maxThreshold = 10


	# Filter by Area.
	params.filterByArea = True
	params.minArea = 10

	# Filter by Circularity
	params.filterByCircularity = True
	params.minCircularity = 0.05

	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.10

	# Filter by Inertia 
	# Will investigate this feature later
	#params.filterByInertia = True
	#params.minInertiaRatio = 0.01
	return params


def detection(path):
	# Import image
	im = cv2.imread(path)

	#Loads parameters as defined in the parameters function
	params = parameters()

	# Create a detector with the parameters
	detector = cv2.SimpleBlobDetector_create(params)

	# Detect blobs.
	keypoints = detector.detect(im)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob

	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	# Show blobs
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey(0)


def detection_return(path, save_path, item):
	# Import image
	im = cv2.imread(path)

	#Loads parameters as defined in the parameters function
	params = parameters()

	# Create a detector with the parameters
	detector = cv2.SimpleBlobDetector_create(params)

	# Detect blobs.
	keypoints = detector.detect(im)

	print("Keypoints are located at: " + str(keypoints))

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob

	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	
	cv2.imwrite(save_path, im_with_keypoints)

	return im_with_keypoints


def debug_keyponts(path):
	# Import image
	im = cv2.imread(path)

	#Loads parameters as defined in the parameters function
	params = parameters()

	# Create a detector with the parameters
	detector = cv2.SimpleBlobDetector_create(params)

	# Detect blobs.
	keypoints = detector.detect(im)
	

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob

	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	return im_with_keypoints



#def main():
#	path = "C:/Users/Chris Dryden/Desktop/projects/UTAT UAV/FeatureDetector/frame11.jpg"
#	detection(path)
#
#
#if __name__ == "__main__":
#	main()