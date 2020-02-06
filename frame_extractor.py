import cv2
import sys
import os

def frame_extractor(path_to_video, output_dir):
	# Read in each frame from path_to_video and save the frame as a .jpg to 
	# output_dir. The output_dir should have some indication of what the
	# source video is.
	vidcap = cv2.VideoCapture(path_to_video)
	success,image = vidcap.read()
	count = 1
	while success:
		d = os.path.join(output_dir, str(count) + '.jpg')
		cv2.imwrite(d, image)     # save frame as JPEG file      
		success, image = vidcap.read()
		count += 1
		
path_to_video = sys.argv[1]
output_dir = sys.argv[2]

frame_extractor(path_to_video, output_dir)
