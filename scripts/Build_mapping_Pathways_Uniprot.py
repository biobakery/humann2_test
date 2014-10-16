#!/usr/bin/env python
 
from cStringIO import StringIO
import sys,string
import os
from pprint import pprint
import sys, os
from pprint import *
import math
import pdb
import tempfile 
import argparse
from subprocess import call


#*************************************************************************************
#* Parse Input parms                                                                 *
#*************************************************************************************
def read_params(x):
	CommonArea = dict()	
	parser = argparse.ArgumentParser(description='Build mapping Pathways to Uniprot Ids')
	parser.add_argument('--o', action="store", dest='o',nargs='?',  default='summary_analysis')
	parser.add_argument('--i', action="store", dest='i',nargs='?')
	CommonArea['parser'] = parser
	return  CommonArea
 
 
#*************************************************************************************
#* Filter the records                                                                *
#*************************************************************************************
def FilterLine(iLine):
		if len(iLine) == 0\
		or iLine.startswith("----")\
		or iLine.find("UniProt - Swiss-Prot Protein Knowledgebase") > -1 \
		or iLine.find("SIB Swiss Institute of Bioinformatics; Geneva, Switzerland") > -1\
		or  iLine.find("European Bioinformatics Institute (EBI); Hinxton, United Kingdom") > -1\
		or iLine.find("Protein Information Resource (PIR); Washington DC, USA") > -1\
		or iLine.find("Description: PATHWAY comments: index") > -1\
		or iLine.find("Name:        pathway.txt") > -1\
		or  iLine.find("Release:") > -1\
		or iLine.find("Copyrighted by the UniProt Consortium") > -1\
		or iLine.find("Distributed under the Creative Commons Attribution-NoDerivs License") > -1:
			return -1
		return 0
 

#*************************************************************************************
#* Read the file                                                                     *
#*************************************************************************************
def Map_Pathways_toUniprotIDs(CommonArea):
	OutputFile = open(CommonArea['oFile'],'w')
	InputFile = open(CommonArea['iFile'])
	dPathwayUniprotAc = dict()
	lOutputLine = list()
	for iLine in InputFile: 
		iLine = iLine.rstrip('\n')
		RC = FilterLine(iLine)
		if RC < 0:
			continue

		if iLine[1] != " ":
			if len(lOutputLine) > 0:
				strBuiltRecord = "\t".join(lOutputLine) + 	"\n"
				OutputFile.write(strBuiltRecord )
			lOutputLine = [iLine]
		else:
			lEntries = iLine.split()
			for sEntry in lEntries:
				if sEntry.startswith("("):
					AC = sEntry.replace("(","").replace(")","")
					lOutputLine.append(AC)
  	else:
		if len(lOutputLine) > 0:
			strBuiltRecord = "\t".join(lOutputLine) + 	"\n"
			OutputFile.write(strBuiltRecord )
  
  
	InputFile.close()
	OutputFile.close()
	return CommonArea 









#*************************************************************************************
#*  Main Program                                                                     *
#*************************************************************************************
print "Program started"
CommonArea = read_params( sys.argv )  # Parse command  
parser = CommonArea['parser'] 
results = parser.parse_args()
CommonArea['oFile'] = results.o
CommonArea['iFile'] = results.i 


RC = Map_Pathways_toUniprotIDs(CommonArea)
print "Program ended Successfully"
exit(0)
