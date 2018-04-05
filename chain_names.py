# the script outputs a txt file with a list of all the chains
# in a molecule, to compare the chain's name on the pdb file
# and the "real" name of the chain

from lxml import html
import requests
import sys, os, time, subprocess
from subprocess import call
import UserString

class ChainNames:
	
	# displays the usage of the program if run without parameters
	def help(self):
		print ''
		print 'Usage:'
		print 'python chain_names.py molecule_code_on_pdb'
		print 'example: python chain_names.py 2WSS'
		print ''
		
	def scrape_data(self, chain):
		self.structure_id = chain

		# requests.get retrieves the web page with the data, parses 
		# it using the html module and saves the results in tree
		print 'requesting...'
		page = requests.get('https://www.rcsb.org/pdb/explore/remediatedSequence.do?structureId=' + self.structure_id + '&params.chainsPerPage=100')
		print '...done'
		tree = html.fromstring(page.content)

		name = tree.xpath('//div[@class="panel-heading"]/text()')
	
		# prints in a txt file
		output_file = open(''+ self.structure_id + '_chains.txt', 'w')
		for i in name:
			output_file.write(i +'\n')
		output_file.close()

cn = ChainNames()

if len(sys.argv) == 1:
	cn.help()
	sys.exit(0)

try:
	cn.scrape_data(sys.argv[1])
# need to better handle errors
except IOError:
	print ''
	print 'PDB CODE ERROR! Insert a valid pdb code'
	print ''
