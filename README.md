# Simple Steganography Application (SSA)

This application is a simple tool to hide a string
in an image.

It uses the images's RGB values to embed information within them.

## How to use

To use put the string in a command line:

	python ssa encode "image_name" -s "string"

To put the contents of the file in the image:

	python ssa encode "image_name" -f "file_name"

To get the images content:

	python ssa decode "image_name"

To dump the images content in another file:

	python ssa decode "image_name" -f "file_name"

## Usage example

	python ssa encode "photo.png" -s "Hello, encoding image using SSA"
	python ssa decode "photo.png"
	python ssa encode "wallpaper.jpg" -f "ssa.py"
	python ssa decode "wallpaper.jpg" -f "ssa_copy.py"
