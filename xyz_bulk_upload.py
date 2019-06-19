import argparse
import os
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--space',
	help='xyz space')
parser.add_argument('-p', '--properties',
	help='properties to use as tags, comma separated')
parser.add_argument('-t', '--tags',
	help='tags to add to features, comma separated')
parser.add_argument('-f', '--filename_substring',
	help='tags to generate if a substring is in filename, comma separated')

results = parser.parse_args()

print("writing to",results.space,"\nproperties to tag",results.properties,"\ntags to add",results.tags,"\nextracting tags from filename",results.filename_substring)

count = 0

# convert substrings and tags into arrays
substrings = []
tags = []
if results.properties:
	properties = ' -p' + results.properties
else:
	properties = ''
if results.filename_substring:
	substrings = results.filename_substring.split(",") 
else: 
	substrings = ''
if results.tags:
	tags = results.tags.split(",")
else: 
	tags = ''
print ("substrings:",substrings)

# for fn in os.listdir('.'):  # walk through each file in the directory
path = os.getcwd()
# for subdir, dirs, files in os.walk('.'):
for path, subdirs, files in os.walk('.'):
	for fn in files:
		if "shp" in fn or "geojson" in fn or "csv" in fn: 
			if "shp" in fn:
				stream = false
			if "csv" in fn:
				stream = true
			if "geojson" in fn:
				stream = true
			full_path = os.path.join(path, fn)
			print ("processing",full_path)
			substrings_and_tags = tags.copy()
			for substring in substrings:  #check to see if substrings to tag are actually in this filename
		
				if substring.lower() in fn.lower():
					if substring.startswith('_'):
						_substring = substring[1:]
						substrings_and_tags.append(_substring)
						print("tagging substring, removed leading underscore:",_substring)
					else:
						substrings_and_tags.append(substring)
						print("tagging substring:",substring)
			substrings_and_tags = ','.join(substrings_and_tags)
			print("adding tags:",substrings_and_tags)
			streaming = ''
			if stream:
				streaming = ' -s'
			xyz = "here xyz upload " + results.space + " -f " + full_path + " -t " + substrings_and_tags +  properties + streaming
			print(xyz)
			os.system(xyz) #probably should use subprocess to parse and count errors
			count = count + 1
			print (count,"files processed")
		


