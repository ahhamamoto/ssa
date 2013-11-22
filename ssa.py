#!/usr/bin/env python

class SSA():

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

	def encode(self, string):
		encoded = []
		for c in string:
			encoded.append(self.to_binary(c))
		return encoded

	def decode(self, bin):
		decoded = []
		for b in bin:
			decoded.append(self.to_character(b))
		return decoded