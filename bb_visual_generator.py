import cv2
import sys
import os
from tqdm import tqdm

# For a given video, draw bounding boxes on all its frames and save
# them to an output directory

training_dir = sys.argv[1] # path to directory with images, labels folders
output_dir = sys.argv[2] # path where imgs w boxes will be written
video_num = sys.argv[3] # vid ID number

green = (0, 255, 0)

img_path = os.path.join(training_dir, 'images', video_num)

for filename in tqdm(os.listdir(img_path)):
	#print(filename)
	
	img = cv2.imread(os.path.join(img_path, filename))
	#print('read from ', os.path.join(training_dir, 'images', video_num))
	
	file_num = filename.split('.')[0]
	
	try: 
		with open(os.path.join(training_dir, 'labels', video_num, file_num + '.txt')) as f:
			box = f.read().split(' ')
		

		label = box[0] 
		xmin, ymin, xmax, ymax = [int(x.replace('\n', '')) for x in box[1:]]

		img = cv2.rectangle(img,(xmin, ymax),(xmax, ymin), green,1)

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,label,(xmin , ymin-2), font, 0.6,green,1,cv2.LINE_AA)
		
		#cv2.imshow('image', img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		
		cv2.imwrite(os.path.join(output_dir, video_num, file_num + '.jpg'), img)
	except FileNotFoundError:
		print('No label file found:', file_num + '.txt')

"""
img = cv2.imread(image_dir)

with open(label_dir, 'r') as f:
	box = f.read().split(' ')
	
print(box)

label = box[0] 
xmin, ymin, xmax, ymax = [int(x.replace('\n', '')) for x in box[1:]]

print(label, xmin, ymin, xmax, ymax)

img = cv2.rectangle(img,(xmin, ymax),(xmax, ymin), green,1)
# arguments are: image handle, (top left corner), (bottom right corner), 
# color as 3-tuple, rectangle thickness

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,label,(xmin , ymin-2), font, 0.6,green,1,cv2.LINE_AA)
# args: img handel, text, 2-tuple of text position, font, size, 
# color as 3-tuple, thickness, ???

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
