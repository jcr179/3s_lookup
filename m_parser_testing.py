from xml.etree import ElementTree as et

mytree = et.parse('test_meta3.xml')

"""
myroot = mytree.getroot()

queue = [myroot]
while queue:
	current = queue.pop(0)
	print(current.tag, '...', current.attrib)
	
	for child in current:
		queue.append(child)
"""	

""" For all elements.
for elem in mytree.iter():
	print(elem.tag, '...', elem.attrib)
"""

"""
tags = ['{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint', '{urn:mpeg:mpeg7:schema:2001}Box', '{urn:mpeg:mpeg7:schema:2001}Keyword']

for t in tags:
	for elem in mytree.iter(tag=t):
		if elem.text == 'ken 1':
			print(elem.tag, '...', elem.attrib, '...', elem.text)
		
"""

"""
# Great help in visualizing complicated XML structures with indenting!
import xml.dom.minidom

dom = xml.dom.minidom.parse('test_meta3.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)
"""

# Bounding box dimensions are minx miny maxx maxy 


# This gets all the manually placed bounding boxes but none of the interpolated ones.
"""
label_token = '{urn:mpeg:mpeg7:schema:2001}StillRegion'

data_point = {'{urn:mpeg:mpeg7:schema:2001}Keyword': 'label', '{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint': 'frame', \
'{urn:mpeg:mpeg7:schema:2001}Box': 'box'}

layer2 = {'{urn:mpeg:mpeg7:schema:2001}SpatialDecomposition': None}

for elem in mytree.iter(tag=label_token):
	point = {'label': None, 'frame': None, 'box': None}
	for e in elem:
		if e.tag == '{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint':
			#print(e.tag, e.text)
			point['frame'] = int(e.text)
		if e.tag in layer2:
			for dp in data_point:
				for child in e.iter(tag=dp):
					#print(child.tag, child.text)
					if data_point[child.tag] == 'label':
						#print(child.text.split(' '))
						label = child.text.split(' ')[0]
						point[data_point[child.tag]] = label
					else: # Box
						box = [int(x) for x in child.text.split(' ')]
						point[data_point[child.tag]] = box
						
	if all(point.values()): # If all values are non-None
		print(point)
"""

label_token = '{urn:mpeg:mpeg7:schema:2001}StillRegion'

data_point = {'{urn:mpeg:mpeg7:schema:2001}Keyword': 'label', '{urn:mpeg:mpeg7:schema:2001}MediaRelIncrTimePoint': 'frame', \
'{urn:mpeg:mpeg7:schema:2001}Box': 'box'}

layer2 = {'{urn:mpeg:mpeg7:schema:2001}SpatialDecomposition': None}

last_seen_label = None

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
							box = [int(x) for x in child.text.split(' ')]
							point[data_point[child.tag]] = box
					else: # Interpolated frame
						point['label'] = last_seen_label
						
	if all(point.values()): # If all values are non-None
		print(point)		
					
print('test one'.split())
print('test     one'.split())
