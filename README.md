# XYZ bulk uploader

This Python3 script uploads files in a directory to an XYZ Space using the HERE CLI. 

It assumes you have the [HERE CLI](https://github.com/heremaps/here-cli) installed. (Yes, a Python script controlling a Node app, I know.)

It looks in the directory (and subdirectories!) for GeoJSON, shapefiles, and CSVs. It will tell the CLI to stream GeoJSON and CSVs.

You can also add a list of words that will get turned into tags if they appear as a substring in the filename.

There is little to no error detection -- if there is a failure, it will move on to the next file, so you'd better check the CLI output.

arguments:

- `-s` the XYZ space you want to write to
- `-t` tags you want to add to all features
- `-p` property values you want to turn into a tag
- `-f` strings to search for in filenames to add as tags
