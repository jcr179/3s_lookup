import sys
import os

def label_generator(input_file, label_output_file_dir):
	# WARNING: Currently only handles 1 object type per frame!!!
		
	"""
	with open(input_file, 'r') as reader:
		line = reader.readline()
		frame = line.split()[-1]
		print(line, 'frame:',frame)
		
		with open(os.path.join(label_output_file_dir, frame), 'w') as writer:
			tmp = line.split()[:-1]
			print('tmp is ', tmp)
			print('will write ', ''.join([x + ' ' for x in tmp])[:-1])
			writer.write(''.join([x + ' ' for x in tmp])[:-1] + '\n')
	"""
	read = open(input_file, 'r')
	
	for i, line in enumerate(read):
		frame = line.split()[-1]
		tmp = line.split()[:-1]
		
		output_file_name = os.path.join(label_output_file_dir, frame)
		writer = open(output_file_name + '.txt', 'w')
		writer.write(''.join([x + ' ' for x in tmp])[:-1] + '\n')
		writer.close()

input_file = sys.argv[1]
label_output_file_dir = sys.argv[2]

label_generator(input_file, label_output_file_dir)
