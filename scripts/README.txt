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

