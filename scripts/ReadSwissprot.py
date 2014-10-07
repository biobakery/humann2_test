#!/usr/bin/env python
from cStringIO import StringIO
import sys,string
import sys, os
import argparse
from subprocess import call





#********************************************************************************************
#    Read Swissprot gram                                                                    *
#    This program reads the unprot.dat file and creates an                                  *
#    extract containing in each line                                                        *
#    The Protein AC and all the ECs related to it                                           *

#  -----------------------------------------------------------------------------------------*
#  Invoking the program:                                                                    *
#  ---------------------                                                                    *
#   python ReadSwissprot.py  --i  input_file  --o output_file                               *
#   Where:                                                                                  *
#                                                                                           *
#   Written by George Weingart - george.weingart@gmail.com   10/06/2014                     *  
#********************************************************************************************








#*************************************************************************************
#* Read Swissprot                                                                    *
#*************************************************************************************
def ReadSwissprot(i,o):
	iFile = i
	oFile = o
	strTab = "\t"
	strNewLine = "\n"
	InputFile = open(iFile)
	OutputFile = open(oFile,'w')
	LineCntr = 0
	OutputLineCntr = 0
	for iLine in InputFile:
			LineCntr = LineCntr +1
			if iLine.startswith("AC   "):
				lTemp = iLine.rstrip().split().pop().split(";")
				lACs = [var for var in lTemp if var]
  
			if iLine.startswith("DE   "):
 			    lTemp = iLine.rstrip().split().pop().split(";")
			    lECsTemp = [var for var in lTemp if var]
			    lECs = list()
			    bFlagEC = False
			    for strEC in lECsTemp:
					if strEC.startswith("EC="):
						bFlagEC = True
						strEC  =  strEC.replace("EC=","")
						strEC  =  strEC.replace(".-","")
						lECs.append(strEC)
			    if  bFlagEC == True:
					for ProtAC in lACs:
						OutputLine = ProtAC 
						for EC in  lECs:
							OutputLine =  OutputLine + strTab + EC  
					OutputLine = OutputLine + strNewLine
					OutputFile.write(OutputLine )
					OutputLineCntr = OutputLineCntr + 1
	print "Read " + str(LineCntr) + " Input Lines"
	print "Wrote " + str(OutputLineCntr) + " Output Lines"
	InputFile.close()
	OutputFile.close()
	return 0











#*************************************************************************************
#* Parse Input parms                                                                 *
#*************************************************************************************
def read_params(x):
	CommonArea = dict()	
	parser = argparse.ArgumentParser(description='Analysis of Short reads using k-mers search')
	parser.add_argument('--i', action="store", dest='i',nargs='?')
	parser.add_argument('--o', action="store", dest='o',nargs='?',  default='output_analysis')
	CommonArea['parser'] = parser
	return  CommonArea









#*************************************************************************************
#*  Main Program                                                                     *
#*************************************************************************************
print "Program started"
CommonArea = read_params( sys.argv )  # Parse command  
parser = CommonArea['parser'] 
results = parser.parse_args()

iFile = results.i
oFile = results.o
RC  = ReadSwissprot(iFile,oFile)



print "Program ended Successfully"
exit(0)
