# the program displays the first and last residue numbers of a 
# structure along all the numbers of the missing residues by taking 
# in input a PDB file

from Bio.PDB import *
from itertools import imap, chain
from operator import sub
import sys, os, time, subprocess
from subprocess import call
import UserString


class MissingResidues:
	
	# displays the usage of the program if run without parameters
	def help(self):
		print ''
		print 'Usage:'
		print 'python missing_res.py filename_without_extension'
		print 'example: python missing_res.py 2wss'
		print ''
	
	# uses Bio.PDB's PDBParser class to extract all the structure's 
	# residues numbers from the PDB file and then gets all the 
	# missing numbers
	def find_res(self, name):
		self.structure_name = name
		self.a = []

		p=PDBParser()
		structure=p.get_structure(self.structure_name, self.structure_name+'.pdb')
		for residue in structure.get_residues():
			residue_id = residue.get_full_id()
			resseq = residue_id[3][1]
			self.a.append(resseq)

		self.miss_res = list(chain.from_iterable((self.a[i] + d for d in xrange(1, diff))
			for i, diff in enumerate(imap(sub, self.a[1:], self.a))
			if diff > 1))
	
	# prints the number of the first and last residue in the PDB file
	# and the numbers of its missing residues
	def results(self):
		print ''
		print '======= '+self.structure_name+' ======='
		print 'Starting residue: '+str(self.a[0])
		print 'Ending residue: '+str(self.a[-1])
		print 'Missing residues (if any): '+str(self.miss_res)
		print ''
		
		
mr = MissingResidues()

if len(sys.argv) == 1:
	mr.help()
	sys.exit(0)

try:
	mr.find_res(sys.argv[1])
	mr.results()
except IOError:
	print ''
	print 'NAMEFILE ERROR! There is no '+sys.argv[1]+'.pdb in folder'
	print ''
