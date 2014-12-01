import unittest
import logging

import cfg
import utils

import nucleotide_search
import store
import config
import utilities

class TestAdvancedHumann2NucleotideSearchFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/nucleotide_search.py
    """
    
    def setUp(self):
        config.unnamed_temp_dir="/tmp/"
        
        # set up nullhandler for logger
        logging.getLogger('nucleotide_search').addHandler(logging.NullHandler())

    def test_nucleotide_search_unaligned_reads_output_fasta_format(self):
        """
        Test the unaligned reads and the store alignments
        Test with a bowtie2/sam output file
        Test output file is of fasta format
        Test sam file is not removed
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # read in the aligned and unaligned reads
        [unaligned_reads_file_fasta, unaligned_reads_store, 
            reduced_aligned_reads_file] = nucleotide_search.unaligned_reads(
            cfg.sam_file_unaligned_reads, alignments, keep_sam=True) 
        
        # check for fasta output file format
        file_format=utilities.determine_file_format(unaligned_reads_file_fasta)
        self.assertEqual("fasta",file_format)
        
        # remove temp files
        utils.remove_temp_file(unaligned_reads_file_fasta)
        utils.remove_temp_file(reduced_aligned_reads_file)


    def test_nucleotide_search_unaligned_reads_read_count_aligned(self):
        """
        Test the unaligned reads and the store alignments
        Test with a bowtie2/sam output file
        Test for aligned read counts
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # read in the aligned and unaligned reads
        [unaligned_reads_file_fasta, unaligned_reads_store, 
            reduced_aligned_reads_file] = nucleotide_search.unaligned_reads(
            cfg.sam_file_unaligned_reads, alignments, keep_sam=True) 
        
        # remove temp files
        utils.remove_temp_file(unaligned_reads_file_fasta)
        utils.remove_temp_file(reduced_aligned_reads_file)
        
        # check the aligned reads count
        self.assertEqual(len(alignments.all_hits()),cfg.sam_file_unaligned_reads_total_aligned)
        
        
    def test_nucleotide_search_unaligned_reads_read_count_unaligned(self):
        """
        Test the unaligned reads and the store alignments
        Test with a bowtie2/sam output file
        Test for unaligned read counts
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # read in the aligned and unaligned reads
        [unaligned_reads_file_fasta, unaligned_reads_store, 
            reduced_aligned_reads_file] = nucleotide_search.unaligned_reads(
            cfg.sam_file_unaligned_reads, alignments, keep_sam=True) 
        
        # remove temp files
        utils.remove_temp_file(unaligned_reads_file_fasta)
        utils.remove_temp_file(reduced_aligned_reads_file)
        
        # check the unaligned reads count
        self.assertEqual(unaligned_reads_store.count_reads(),cfg.sam_file_unaligned_reads_total_unaligned)


