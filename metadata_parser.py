from xml.etree import ElementTree as et
import sys

# Parse xml data from GTEditor into an output file for further processing.

input_file = sys.argv[1]
output_file = sys.argv[2]

mytree = et.parse(input_file) # input file

label_token = '{urn:mpeg:mpeg7:schema:2001}StillRegion'

data_point = {'{urn:mpeg:mpeg7:schema:2001}Keyword': 'label', '{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint': 'frame', \
'{urn:mpeg:mpeg7:schema:2001}Box': 'box'}

layer2 = {'{urn:mpeg:mpeg7:schema:2001}SpatialDecomposition': None}

last_seen_label = None

output = []

for elem in mytree.iter(tag=label_token):
	point = {'label': None, 'frame': None, 'box': None}
	for e in elem:
		if e.tag == '{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint':
			#print(e.tag, e.text)
			point['frame'] = int(e.text)
		if e.tag in layer2:
			for dp in data_point:
				for child in e.iter():
					#print(child.tag, child.text)
					if child.tag in data_point:
						if data_point[child.tag] == 'label':
							#print(child.text.split(' '))
							label = child.text.split(' ')[0]
							point[data_point[child.tag]] = label
							last_seen_label = label
						elif data_point[child.tag] == 'box': # Box
							box = [x + ' ' for x in child.text.split(' ')]
							point[data_point[child.tag]] = box
					else: # Interpolated frame
						point['label'] = last_seen_label
						
	if all(point.values()): # If all values are non-None
		#print(point)	
		output.append(point)
		
	
with open(output_file, 'w') as fp:
	for datapoint in output:
		tmp = str(datapoint['label']) + ' ' + ''.join(datapoint['box'])[:-1] + ' ' + str(datapoint['frame'])
		fp.write(tmp + '\n')	
		
