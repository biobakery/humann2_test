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


