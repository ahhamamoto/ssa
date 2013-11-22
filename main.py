#!/usr/bin/env python

import ssa

def main():
	a = ssa.SSA()
	print a.to_binary('A')
	print a.to_character(a.to_binary('A'))
	print a.encode('AAA')
	print a.decode(a.encode('AAA'))

if __name__ == '__main__':
	main()