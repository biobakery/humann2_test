[TOC]

# HUMAnN2 Test #

The HUMAnN2 Test repository contains software to test HUMAnN2. 

## Requirements ##

### Software ###

Download and Install [HUMAnN2](https://bitbucket.org/biobakery/humann2/)

All HUMAnN2 software requirements are also required for HUMAnN2 Test:

1. [MetaPhlAn](https://bitbucket.org/biobakery/metaphlan2/)
1. [bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/) (version >= 2.1)
1. [rapsearch2](http://omics.informatics.indiana.edu/mg/RAPSearch2/)
1. [Python](http://www.python.org/) (version >= 2.7)

All of these requirements should be installed in a location in your $PATH.

### Other ###
1. Operating system (Linux or Mac)

## Installing HUMAnN2 Test ##
HUMAnN2 Test can be downloaded in two ways:

* [Download](https://bitbucket.org/biobakery/humann2_test/downloads) a compressed set of files.
* Create a clone of the repository on your computer with the command: 
	
	``hg clone https://bitbucket.org/biobakery/humann2_test ``

Note: Creating a clone of the repository requires [Mercurial](http://mercurial.selenic.com/) to be installed. Once the repository has been cloned upgrading to the latest release of HUMAnN2 Test is simple. Just type ``hg -u pull`` from within the repository which will download the latest release.

There are no additional steps to install HUMAnN2 Test.

## How to Run ##

### Basic usage ###

From in the HUMAnN2_Test folder, type the command:

`` ./humann2_test.py ``

Running with the optional "--verbose" flag will produce output like the following.
```
$ ./humann2_test.py --verbose
test_break_up_fasta_file (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_count_reads (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_double_sort (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_estimate_unaligned_reads (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_fastq_to_fasta (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_file_exists_readable (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_Alignments_add (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysAndReactions_median_score (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_print_flat_file (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_ReactionsDatabase_read (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_delete_id (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_print_fasta (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_compute_gene_scores (basic_tests_quantify_families.TestHumann2QuantifyFamiliesFunctions) ... ok
test_gene_families (advanced_tests_quantify_families.TestHumann2QuantifyFamiliesFunctions) ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.013s

OK
```
The output describes each test which is run along with if it passes.
The total number of tests run will be printed at the end along with the time required
to run the tests. If any tests fail this will be indicated in the output.

### Complete option list ###
```
usage: humann2_test.py [-h] [-v] [--humann2 <humann2/>]

HUMAnN2 Unittest: Test cases for HUMAnN2

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         additional output is printed
  --humann2 <humann2/>  directory containing HUMAnN2
                        [DEFAULT: $PYTHONPATH]
```