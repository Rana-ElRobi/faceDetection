# Working !!!!!!!!!!!!!!!!!!!!
# This file loads all face images then detect faces from them
# needed packages
import cv2
# load images 
# Returns images loaded in stack and gray version of the image in stack too
def loadfaces():
	#Images main path 
	path= "/home/rana/Desktop/yelp/faceDetection/people/"
	#creat list with images names
	imgnames=[  "408830.jpg" ,"409268.jpg" ,"469954.jpg"  ,
				"470265.jpg" ,"470580.jpg" ,"470804.jpg" ,
				"470294.jpg" ,"470647.jpg" ,"470822.jpg" ,
				"470408.jpg" ,"470662.jpg" ,"470894.jpg" ,
				"470953.jpg" ,"471344.jpg" ,"471271.jpg" ,
				"471073.jpg" ,"471463.jpg" ,"471279.jpg" ,
				"471103.jpg" ,"471550.jpg" ,"471333.jpg" ,
				"471671.jpg" ,"471753.jpg" ,"471797.jpg" ,
				"471800.jpg" ]
	#create empty list for images loaded 
	imgstack =[]
	grayStack =[]
	# Loop to load the images in the path  
	for i in imgnames:
		# Read the image
		image = cv2.imread(path + i)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		imgstack.append(image)
		grayStack.append(gray)
		# display last element in the list
		#print (i)
		#cv2.imshow("Faces found" ,imgstack[-1])
		#cv2.waitKey(0)	
	return imgstack , grayStack
# face detection function
# input : 
#--------
# fi : target imges stack 
# gi : target images stack in gray scale
# =====================
# output:
# -------
# display imges with green fram in the detected imges
# Helper link :
# https://realpython.com/blog/python/face-recognition-with-python/
def findFacaes(fi,gi):
	cascPath = "/home/rana/Desktop/yelp/faceDetection/FaceDetect/haarcascade_frontalface_default.xml"
	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)
	# Loop on the images stack
	for i,item in enumerate (gi):
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
		    item,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(20, 20),
		    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		)
		print "Found {0} faces!".format(len(faces))
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
		    cv2.rectangle(fi[i], (x, y), (x+w, y+h), (0, 255, 0), 2)
		cv2.imshow("Faces found" ,fi[i])
		cv2.imwrite("face {0}.png".format(i),fi[i])
		cv2.waitKey(0)
		#break
# This function trie dto custmize the parameters of face detection to find all people in the image no 15
def image15(colorimg,grayimg):
	cascPath = "/home/rana/Desktop/yelp/faceDetection/FaceDetect/haarcascade_frontalface_default.xml"
	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)
	# Loop on the images stack
	#for i,item in enumerate (gi):
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
	    grayimg,
	    scaleFactor= 1.1,
	    minNeighbors= 3,
	    minSize=(15, 15),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	print "Found {0} faces!".format(len(faces))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		if (w < 53):
	    		cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    		print(" x :",x)
	    		print(" y :",y)
	    		print(" w :",w)
	    		print(" h :",h)
			cv2.imshow("Faces found" ,colorimg)
			cv2.imwrite("face 15.png",colorimg)
			cv2.waitKey(0)
# function that try to custmize the face detection on image 7
def image7(colorimg,grayimg):
	cascPath = "/home/rana/Desktop/yelp/faceDetection/FaceDetect/haarcascade_frontalface_default.xml"
	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)
	# Loop on the images stack
	#for i,item in enumerate (gi):
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
	    grayimg,
	    scaleFactor= 1.03,
	    minNeighbors= 3,
	    minSize=(25, 25)
	    ,
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	print "Found {0} faces!".format(len(faces))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
		print(" x :",x)
		print(" y :",y)
		print(" w :",w)
		print(" h :",h)
		cv2.imshow("Faces found" ,colorimg)
		cv2.imwrite("face 7.png",colorimg)
		cv2.waitKey(0)
# function that works on custmizing the face detection on image 2
def image2(colorimg,grayimg):
	cascPath = "/home/rana/Desktop/yelp/faceDetection/FaceDetect/haarcascade_frontalface_default.xml"
	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)
	# Loop on the images stack
	#for i,item in enumerate (gi):
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
	    grayimg,
	    scaleFactor= 1.02,
	    minNeighbors= 4,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	print "Found {0} faces!".format(len(faces))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
		print(" x :",x)
		print(" y :",y)
		print(" w :",w)
		print(" h :",h)
		cv2.imshow("Faces found" ,colorimg)
		cv2.imwrite("face 2.png",colorimg)
		cv2.waitKey(0)
# main function
def main():	
	# load face imgs
	faceImgs , grayfaces = loadfaces()
	# General face detection
	#findFacaes(faceImgs,grayfaces)
	# costumizations on image 15
	#image15(faceImgs[15],grayfaces[15])	
	# costumizations on image 7
	#image7(faceImgs[7],grayfaces[7])
	# costumizations on image 7
	image2(faceImgs[2],grayfaces[2])
main()