#!/usr/bin/env python
from pprint import pprint
import fileinput
import sys,os
from math import *
import tempfile 


#********************************************************************************************
#    Read Uniref Program                                                                    *
#    This program reads the mappings uniprot --> Uniref50                                   *
#    and uniprot --> Uniref90                                                               *
#    that currently reside in: /n/huttenhower_lab/data/idmapping/map_uniprot_UniRef50.dat.gz*
#    and /n/huttenhower_lab/data/idmapping/map_uniprot_UniRef90.dat.gz                      *
#    and look as follows                                                                    *
#                                                                                           *
#    Map to Uniref50                                                                        *
#   A0A008IWE9      UniRef50_I0C253                                                         *
#   A0A008IWF0      UniRef50_B0FFT6                                                         *
#   A0A008IWF1      UniRef50_Q5HRF6                                                         *
#   A0A008IWF2      UniRef50_O30875                                                         *
#                                                                                           * 
#    Map to Uniref90                                                                        *
#   A0A008IWE9      UniRef90_I0C253                                                         *
#   A0A008IWF0      UniRef90_X5E5F6                                                         *
#   A0A008IWF1      UniRef90_Q2G0I9                                                         *
#   A0A008IWF2      UniRef90_A5IQZ6                                                         * 
#                                                                                           *
#  The objective of the program is to translate the mcc file so that instead of             *
#  entries showing the uniprot id for a pathway,  we show the uniref50 and uniref90         *
#                                                                                           *
#  For example:   The following record                                                      *
#  BLASTICIDIN-S-DEAMINASE-RXN	EC-3.5.4.23	P33967	P78986                                  *      
#  will be converted to:                                                                    *
#  BLASTICIDIN-S-DEAMINASE-RXN EC-3.5.4.23 UniRef50_P33967 UniRef90_P33967                  *
#  Explanation:                                                                             *
#  P33967  maps in the translation files to UniRef50_P33967 P33967  UniRef90_P33967         *
#  and                                                                                      *
#  P78986 does not have a translation - thus no Uniref50 and Uniref90 entries were created  *
#  for P78986                                                                               *
#  LOGIC:                                                                                   *
#  The program uploads the Uniref translation files into a dictionary  and then reads       *
#  sequentially the mcc file and tries to convert each one of the Uniprot mappings to       *
#  the corresponding Uniref entry                                                           *
#  Logic of the Load of the table:                                                          *
#  The program creates a temporary directory and gunzips the input translation files        *
#  (sys.argv[1] and sys.argv[2])                                                            *
#  It then pastes the two of them together (In the temporary directory) and reads the       *
#  pasted file, uploading each of the Uniprot IDs as a key to the dictionary  with the      *
#  corresponding Uniref50 and 90 entries as a list in that dictionary entry                 *
#                                                                                           *
#  After the dictionary is built,  the temporary directory is deleted and we read the       *
#  mcc file looking for the uniprot id key in the dictionary and retrieving the             *
#  corresponding Uniref50 and 90 translations and posting that record into the output       *
#  -----------------------------------------------------------------------------------------*
#  Invoking the program:                                                                    *
#  ---------------------                                                                    *
#   python ReadUniref.py  map_uniprot_UniRef50.dat.gz map_uniprot_UniRef90.dat.gz  mcc outx *
#   Where:                                                                                  *
#   The first two files are the input mappings                                              *
#   The third file is the input mcc                                                         *
#   The fourth file is the output converted mcc file                                        *
#                                                                                           *
#   Written by George Weingart - george.weingart@gmail.com   8/28/2014                      *  
#********************************************************************************************



#********************************************************************************************
#*   Read Uniref 5090 file  and build translation table                                     *
#********************************************************************************************
def ReadUniref5090File(strInput5090):
	dUniprotUniref = dict()
	iTotalUniref5090RecsLoaded = 0							# Counter of Uniref5090 recs loaded
	iPrintAfter = 1000000										# Print status after multiple of these records
	File5090 = open(strInput5090)							# Open the file
	for strInputLine in File5090:   						# Read Input file
		lInputLineSplit = strInputLine.split() 				# Split the line using space as delimiter
		lEnt5090 = list()									# Initialize list
		lEnt5090.append(lInputLineSplit[1].split("_")[1])	# Entry is of the form UniRef50_Q2FWP1 - We need only the Q2FWP1
		lEnt5090.append(lInputLineSplit[3].split("_")[1])	# Entry is of the form UniRef50_Q2FWP1 - We need only the Q2FWP1
		dUniprotUniref[lInputLineSplit[0]] = lEnt5090		# Post it in the dictionary
		iTotalUniref5090RecsLoaded+=1						# Increase counter
		if  iTotalUniref5090RecsLoaded %  iPrintAfter == 0:	# If we need to print status
			print "Total of ", iTotalUniref5090RecsLoaded, " Uniref5090 records loaded into the table"
		#if  iTotalUniref5090RecsLoaded > 40000000:				#Just for debug......
			#print "Dummy Load Complete - Total of ", iTotalUniref5090RecsLoaded, " Uniref5090 records loaded into the table"
			#return dUniprotUniref
	print "Load Complete - Total of ", iTotalUniref5090RecsLoaded, " Uniref5090 records loaded into the table"
	File5090.close()										# CLose the file
	return dUniprotUniref
 
 
#********************************************************************************************
#*   Process MCC file                                                                       *
#********************************************************************************************
def ProcessMCCFile(strInputmcc,  dUniprotUniref):
 
	iTotalMCCRecordsProcessed = 0							# Total MCC Records processed
	iTotalTranslationsFound = 0								# Total Translations 
	iPrintAfterMCCProcessed = 100   						# Print MCC processed only after 
	FileMCC =  open(strInputmcc)							# Open MCC file
	for strInputMCCLine in FileMCC:   						# Read Input MCC file
		lInputMCCLineSplit = strInputMCCLine.split() 				# Split the line using space as delimiter
		lRebuiltRecord = [lInputMCCLineSplit[0]]			#The rebuilt record consists of the ID, EC number (If there is one) plus any following translations
		iStartOfUniprotIds = 1								# In most cases it will be 2, but we initialize to 1 and if there is an EC we set to 2			
		if  lInputMCCLineSplit[1].startswith("EC-"):		# If there is an EC number
			lRebuiltRecord.append(lInputMCCLineSplit[1])	#  Add it
			iStartOfUniprotIds = 2							# The start of Uniprot IDs is 2
			lRebuiltRecord = [lInputMCCLineSplit[0], lInputMCCLineSplit[1]]		#The rebuilt record consists of the ID, EC number plus any following translations
		for  iIndx  in range(iStartOfUniprotIds,len(lInputMCCLineSplit)):
			lTranslations5090 = None
			try:
				lTranslations5090 = dUniprotUniref[ lInputMCCLineSplit[iIndx]] 	
			except:
				pass
			if lTranslations5090 is not None:
				iTotalTranslationsFound +=1								# Add to counter of translations
				lRebuiltRecord.append("UniRef50_" + lTranslations5090[0])	# Adding the translated entry for Uniref50
				lRebuiltRecord.append("UniRef90_" + lTranslations5090[1])	# Adding the translated entry for Uniref90
		lRebuiltRecord.append("\n")										# Add Line end delimiter
		strRebuiltRecord = " ".join(lRebuiltRecord)						# And after finished with all entries, rebuild the record
		OutputFile.write(strRebuiltRecord) 	 							#  write it
		iTotalMCCRecordsProcessed+=1									# Add to the counter of MCC records processed
		if  iTotalMCCRecordsProcessed %  iPrintAfterMCCProcessed == 0:	# If we need to print status
			print "Total of ", iTotalMCCRecordsProcessed, " MCC records processed and a total of ", iTotalTranslationsFound , " Successful Translations"
	FileMCC.close()														# Close MCC file
	return  
 
 
 
#********************************************************************************************
#*   Initialize the process                                                                 *
#********************************************************************************************
def InitializeProcess(strUniref50gz,  strUniref90gz):
	dInputFiles = dict()									# Initialize the dictionary
	dInputFiles["Uniref50gz"] = strUniref50gz				# Store 1st file name in dictionary
	dInputFiles["Uniref90gz"] = strUniref90gz				# Store 2nd file name in dictionary

	strTempDir = tempfile.mkdtemp()							# Make temporary folder to work in
	dInputFiles["TempDirName"] = strTempDir					# Store the name of the temp dir for future use
	cmd_chmod = "chmod 755 /" + strTempDir					# Change permissions to make usable 
	os.system(cmd_chmod)									# Invoke os
	
	print "Unzipping uniref50 file"
	cmd_gunzip = "gunzip -c " + strUniref50gz + ">" + strTempDir + "/" + strUniref50gz[:-3] # Build the gunzip command
	os.system(cmd_gunzip)									# Invoke os
	print "Unzipping uniref90 file"
 	cmd_gunzip = "gunzip -c " + strUniref90gz + ">" + strTempDir + "/" + strUniref90gz[:-3] # Build the gunzip command
	os.system(cmd_gunzip)									# Invoke os
	print "Pasting Uniref50 to Uniref90"
	cmd_paste =  "paste " +  strTempDir + "/" + strUniref50gz[:-3] + " " +\
						strTempDir + "/" + strUniref90gz[:-3] + ">" +\
						strTempDir + "/" + strUniref50gz[:-3] +  "90"    # Paste the two files together
	os.system(cmd_paste )									# Invoke os
	dInputFiles["File5090"] = strTempDir + "/" + strUniref50gz[:-3] +  "90"  #Post the file created into the Common Area
	return dInputFiles
 
 
 
#********************************************************************************************
#* Main                                                                                     *
#********************************************************************************************
print "Program Started"
strUniref50gz = sys.argv[1]					# The first file is the zipped version of the Uniref50 Translation file
strUniref90gz = sys.argv[2]					# The 2nd file is the zipped version of the Uniref90 Translation file
dInputFiles =  InitializeProcess(strUniref50gz,  strUniref90gz)  # Invoke initialization

strInput5090 =  dInputFiles["File5090"]		#Name of the Uniref5090 file
strInputmcc =  sys.argv[3]					#Name if mcc file
OutputFileName = sys.argv[4]				#Name of the output file
OutputFile = open(OutputFileName,'w')		#Open the Output file
print "Starting the load of the table\n"
dUniprotUniref = ReadUniref5090File(strInput5090)	#Invoke reading of the file
print "Completed the load of the table\n"
 
cmd_remove_tempdir = "rm -r /" + dInputFiles["TempDirName"]		# Remove the temporary directory
os.system(cmd_remove_tempdir)	
ProcessMCCFile(strInputmcc,  dUniprotUniref)		#Process MCC file records
OutputFile.close()							#Close the Output file
print "Program Ended Successfully"
