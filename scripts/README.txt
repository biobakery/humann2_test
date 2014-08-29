HUMAnN2 Test Scripts

To create the HUMAnN2 data files from the MetaCyc database:

1. Download the meta.tar.gz of flat-files from MetaCyc.
A description of the files along with download instructions 
can be found at http://bioinformatics.ai.sri.com/ptools/flatfile-format.html

2. Decompress the download.
$ tar zxvf meta.tar.gz

3. Create the humann2/data/mcc data file.
$ ./metacyc2mcc.py < 17.0/data/reactions.dat > humann2/data/mcc

4. Create the humann2/data/mcpc data file.
$ ./metacyc2mcpc.py < 17.0/data/pathways.dat > humann2/data/mcpc

 ***************************************************************************
 *    UPDATE:  We have downloaded version 18.1  of the metacyc files       *
 *    into a new directory called                                          *
 *    /n/huttenhower_lab_nobackup/downloads/metacyc/18.1                   *
 *    August 21, 2014                                                      *
 *    In order to use the updated files please modify the commands         *
 *    in 2. and 3. above to reflect the new directory as follows:          *
 *                                                                         *
 *  
$./metacyc2mcc.py <
/n/huttenhower_lab_nobackup/downloads/metacyc/18.1/data/reactions.dat >
humann2/data/mcc

$./metacyc2mcpc.py <
/n/huttenhower_lab_nobackup/downloads/metacyc/18.1/data/pathways.dat >
humann2/data/mcpc
 *                                                                         *
 ***************************************************************************
 
#********************************************************************************************
#    Read Uniref Program                                                                    *
#    This program reads the mappings uniprot --> Uniref50                                   *
#    and uniprot --> Uniref90                                                               *
#    that currently reside in: /n/huttenhower_lab/data/idmapping/map_uniprot_UniRef50.dat.gz*
#    and /n/huttenhower_lab/data/idmapping/map_uniprot_UniRef90.dat.gz                      *
#  -----------------------------------------------------------------------------------------*
#  Invoking the program:                                                                    *
#  ---------------------                                                                    *
#   python ReadUniref.py  map_uniprot_UniRef50.dat.gz map_uniprot_UniRef90.dat.gz  mcc outx *
#   Where:                                                                                  *
#   The first two files are the input mappings                                              *
#   The third file is the input mcc                                                         *
#   The fourth file is the output converted mcc file                                        *
#                                                                                           *
#                                                                                           *
#    Map to Uniref50 looks as follows:                                                      *
#   A0A008IWE9      UniRef50_I0C253                                                         *
#   A0A008IWF0      UniRef50_B0FFT6                                                         *
#   A0A008IWF1      UniRef50_Q5HRF6                                                         *
#   A0A008IWF2      UniRef50_O30875                                                         *
#                                                                                           * 
#    Map to Uniref90    looks as follows:                                                   *
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
#                                                                                           *
#   Written by George Weingart - george.weingart@gmail.com   8/28/2014                      *  
#********************************************************************************************