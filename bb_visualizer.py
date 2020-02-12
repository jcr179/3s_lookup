import cv2
import sys

# View a frame and its corresponding bounding box

image_dir = sys.argv[1]
label_dir = sys.argv[2]
green = (0, 255, 0)

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
