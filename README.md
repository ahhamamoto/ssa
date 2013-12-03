# Simple Steganography Application (SSA)


## Table of Contents

- [How to Use](#how-to-use)
- [Usage Example](#usage-example)

## How to Use ##

To use put the string in a command line:

	python ssa encode "image_name" -s "string"

To put the contents of the file in the image:

	python ssa encode "image_name" -f "file_name"

To get the images content:

	python ssa decode "image_name"

To dump the images content in another file:

	python ssa decode "image_name" -f "file_name"

## Usage Example ##

	python ssa encode "photo.png" -s "Hello, encoding image using SSA"
	python ssa decode "photo.png"
	python ssa encode "wallpaper.jpg" -f "ssa.py"
	python ssa decode "wallpaper.jpg" -f "ssa_copy.py"
