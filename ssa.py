#!/usr/bin/env python

class SSA():
	'''Class that encodes and decodes messages embeded in images.'''

	def __init__(self):
		'''Initializes lists with options and operations.'''
		self.operations = ['encode', 'decode']
		self.options = {
			'encode': ['-s', '-f'],
			'decode': ['-f']
		}

	def is_fit(self, string):
		'''Checks if string ca fit in the image.'''

		# each character have 1 byte (8 bits)
		# string_lenght = len(string) * 8

		# each pixel can have 3 bits of the message (RGB, 1 one bit each)
		# fits_in_image = pixels * 3

		# return string_lenght < fits_in_image
		return True

	def to_binary(self, c):
		'''Takes a character and converts it to a string of 8 bits.'''

		value = ord(c)
		bin = str(value % 2)
		result = value / 2
		while result > 0:
			bin = bin + str(result % 2)
			result = result / 2

		while len(bin) < 8:
			bin = bin + '0'

		return bin

	def to_character(self, b):
		'''Takes a string of 8 bits and converts it to a character.'''

		multiplyer = 1
		value = 0
		for i in range(7):
			value = value + int(b[i]) * multiplyer
			multiplyer = multiplyer * 2
		return chr(value)

	def encode_to_string(self, string):
		encoded = []
		for c in string:
			encoded.append(self.to_binary(c))
		return encoded

	def decode_from_string(self, bin):
		decoded = []
		for b in bin:
			decoded.append(self.to_character(b))
		return decoded

	def encode(self):
		'''Encode a string in an image.'''

		return True

	def decode(self):
		'''Decodes a string from an image.'''

		return True