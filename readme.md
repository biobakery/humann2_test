# HUMAnN2 Test #

The HUMAnN2 Test repository contains software to test HUMAnN2. 

## Requirements ##

### Software ###

Download and Install [HUMAnN2](https://github.com/biobakery/humann)

All HUMAnN2 software requirements are also required for HUMAnN2 Test:

1. [MetaPhlAn](https://github.com/biobakery/MetaPhlAn)
1. [bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/) (version >= 2.1)
1. [rapsearch2](http://omics.informatics.indiana.edu/mg/RAPSearch2/)
1. [Python](http://www.python.org/) (version >= 2.7)

All of these requirements should be installed in a location in your $PATH.

### Other ###
1. Operating system (Linux or Mac)

## Installation ##
HUMAnN2 Test can be downloaded in two ways:

* [Download](https://github.com/biobakery/humann2_test/archive/master.zip) a compressed set of files.
* Create a clone of the repository on your computer with the command: 
	
	``git clone https://github.com/biobakery/humann2_test.git ``

Note: Creating a clone of the repository requires [Git](https://git-scm.com/) to be installed. Once the repository has been cloned upgrading to the latest release of HUMAnN2 Test is simple. Just type ``hg -u pull`` from within the repository which will download the latest release.

There are no additional steps to install HUMAnN2 Test.

## How to Run ##

### Basic usage ###

From in the HUMAnN2_Test folder, type the command:

`` ./humann2_test.py ``

Running with the optional "--verbose" flag will produce the following output.

```
$ ./humann2_test.py --verbose
test_break_up_fasta_file (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_count_reads_fasta (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_count_reads_fastq (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_fasta (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_fastq (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_rapsearch2_with_header (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_rapsearch2_without_header (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_sam_with_header (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_sam_without_header (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_determine_file_format_sam_without_header_with_tags (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_double_sort (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_double_sort_float (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_estimate_unaligned_reads_fasta_and_fastq_files (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_estimate_unaligned_reads_identical_files (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_fastq_to_fasta (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_file_exists_readable (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_file_exists_readable_raise (basic_tests_utilities.TestHumann2UtilitiesFunctions) ... ok
test_Alignments_add_bug_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_add_bug_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_add_gene_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_add_gene_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_bug_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_bug_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_gene_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_hits_by_gene (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_hits_for_bug (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Alignments_delete_total_genes (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_GeneScores_add (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_GeneScores_add_second_set (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_GeneScores_get_score (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_GeneScores_get_score_second_set (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_GeneScores_scores_for_bug (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysAndReactions_median_score_even_number_vary_pathways (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysAndReactions_median_score_even_number_vary_reactions (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysAndReactions_median_score_odd_number_vary_pathways (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysAndReactions_median_score_odd_number_vary_reactions (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_print_flat_file_pathways_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_print_flat_file_pathways_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_print_flat_file_reactions_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read_pathways_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read_pathways_ids (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read_reactions_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read_reactions_ids (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_PathwaysDatabase_read_reactions_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_ReactionsDatabase_read_gene_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_ReactionsDatabase_read_reactions_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_delete_id (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_print_fasta_id_count (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_print_fasta_id_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_Read_print_fasta_sequence_list (basic_tests_store.TestHumann2StoreFunctions) ... ok
test_compute_gene_scores_double_gene_double_query (basic_tests_quantify_families.TestHumann2QuantifyFamiliesFunctions) ... ok
test_compute_gene_scores_single_gene_double_query (basic_tests_quantify_families.TestHumann2QuantifyFamiliesFunctions) ... ok
test_compute_gene_scores_single_gene_single_query (basic_tests_quantify_families.TestHumann2QuantifyFamiliesFunctions) ... ok
test_Alignments_filter_hits_bug_count (advanced_tests_store.TestAdvancedHumann2UtilitiesFunctions) ... ok
test_Alignments_filter_hits_bug_list (advanced_tests_store.TestAdvancedHumann2UtilitiesFunctions) ... ok
test_Alignments_filter_hits_gene_count (advanced_tests_store.TestAdvancedHumann2UtilitiesFunctions) ... ok
test_gene_families_bug_list (advanced_tests_quantify_families.TestAdvancedHumann2QuantifyFamiliesFunctions) ... ok
test_gene_families_gene_list (advanced_tests_quantify_families.TestAdvancedHumann2QuantifyFamiliesFunctions) ... ok
test_gene_families_tsv_output (advanced_tests_quantify_families.TestAdvancedHumann2QuantifyFamiliesFunctions) ... ok

----------------------------------------------------------------------
Ran 59 tests in 0.035s

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
