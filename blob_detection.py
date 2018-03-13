# Standard imports
import cv2
import numpy as np;


def parameters():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 10
	params.maxThreshold = 200


	# Filter by Area.
	params.filterByArea = True
	params.minArea = 50

	# Filter by Circularity
	params.filterByCircularity = True
	params.minCircularity = 0.01

	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.57

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