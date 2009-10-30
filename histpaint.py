#!/usr/bin/python

import random
from optparse import OptionParser

class RouletteWheel(object):
	def __init__(self, wheelType=None):
		if type(wheelType) is str:
			# Allow string literals 'French' and 'American'
			wheelType = wheelType.capitalize()
			
		if wheelType in [1, "0", "French"]:
			# These are the 37 numbers on a single-zero French wheel, in order 
			# of appearance followed by the corresponding colors.
			self.pool = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 
				6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 
				24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 
				29, 7, 28, 12, 35, 3, 26]
			self.pColor = ['G', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 
				'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 
				'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 
				'B', 'R', 'B', 'R', 'B', 'R', 'B', ]
				
		elif wheelType in [2, "00", "American"]:
			# Double-zero American wheel and corresponding colors
			# TODO: Should check to make sure '0' and '00' are working properly
			#  Maybe a -0 could be used instead of 00 or some other magic number
			self.pool = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 
				5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 
				27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 
				21, 33, 16, 4, 23, 35, 14, 2]
			self.pColor = ['G', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 
				'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'G', 
				'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 
				'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B']
				
		else:
			print "Error: bad wheel type, quitting"
			exit()
		
	def spin(self, n=1):
		spins = []
		for i in range(n):
			index = random.randint(0, len(self.pool) - 1)
			num = self.pool[index]
			numColor = self.pColor[index]
			spin = (num, numColor)
			spins.append(spin)
		return spins
		
if __name__ == "__main__":

	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename", 
		help="write report to FILE", metavar="FILE")
	parser.add_option("-n", "--number", dest="num", type="int", 
		help="write report to FILE", default="1")
	(options, args) = parser.parse_args()


	num = 5
	frames = []	for f in range(1,num+1):
		file = ''
		frame = []
		for c in ['red', 'green', 'black']:
			file = 'histpaintf_%02d.' % (f)
			file = file + c +  '.dat'			frame.append(file)
		frames.append(frame)	print frames 
	
	raw_input("done")

	r=open('./red.dat',   'w')
	g=open('./green.dat', 'w')
	b=open('./black.dat', 'w')

	rw = RouletteWheel(wheelType=1)
	spins = rw.spin(n=38)

	for (i, spin) in enumerate(spins):
		spinNumber = spin[0]
		spinColor  = spin[1]
		if spinColor == "G":
			g.write(str(i) + " 1\n")
		elif spinColor == "R":
			r.write(str(i) + " 1\n")
		elif spinColor == "B":
			b.write(str(i) + " 1\n")
		else:
			print "Error: Bad color, quitting"
			exit()
	
	r.close()
	g.close()
	b.close()
	