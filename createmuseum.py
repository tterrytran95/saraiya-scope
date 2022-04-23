# Program To Read video
# and Extract Frames
# source code: https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
import cv2
FRAME_RATE = 2
# Function to extract frames

def FrameCapture(path):
	
	# Path to video file
    vidObj = cv2.VideoCapture(path)

	# Used as counter variable
    count = 0
	# checks whether frames were extracted 
    success = 1
    outframes = [] # list out outframes
    while success:
        success, image = vidObj.read() # vidObj object calls read # function extract frames

        if count % FRAME_RATE == 0 and success: # Saves the frames with frame-count
            cv2.imwrite("frames/frame%d.jpg" % count, image)
            outframes.append("frames/frame%d.jpg" % count) # just save the name of the image 
        count += 1
    return outframes

# Driver Code
if __name__ == '__main__':

	# Calling the functions
	FrameCapture("samples/theview.MOV")