import unittest
import importlib
import os
import filecmp

import cfg
import utils

import utilities
import config

class TestHumann2UtilitiesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/utilities.py
    """
    
    def setUp(self):
        config.unnamed_temp_dir="/tmp/"

    def test_file_exists_readable(self):
        """
        Test the file_exists_readable function
        """
        
        utilities.file_exists_readable(cfg.small_fasta_file)

    def test_count_reads(self):
        """
        Test the count_reads function
        """
        
        fasta_seqs=utilities.count_reads(cfg.small_fasta_file)
        self.assertEqual(fasta_seqs, cfg.small_fasta_file_total_sequences)                

        fastq_seqs=utilities.count_reads(cfg.small_fastq_file)
        self.assertEqual(fastq_seqs, cfg.small_fastq_file_total_sequences)     

    def test_estimate_unaligned_reads(self):
        """
        Test the estimate_unaligned_reads function
        """
        
        # Test with a fasta and a fastq file with a different number of reads
        percent_unaligned=utilities.estimate_unaligned_reads(
            cfg.small_fasta_file, cfg.small_fastq_file)

        percent_expected=int(cfg.small_fastq_file_total_sequences / 
            float(cfg.small_fasta_file_total_sequences)*100)

        self.assertEqual(percent_unaligned, str(percent_expected))   

        # Test with identical files
        percent_unaligned=utilities.estimate_unaligned_reads(
            cfg.small_fastq_file, cfg.small_fastq_file)

        percent_expected=int(cfg.small_fastq_file_total_sequences / 
            float(cfg.small_fastq_file_total_sequences)*100)

        self.assertEqual(percent_unaligned, str(percent_expected))   

    def test_break_up_fasta_file(self):
        """
        Test the break_up_fasta_file function
        """
        
        # Break up the file into smaller files each containing a single read
        new_fasta_files=utilities.break_up_fasta_file(
            cfg.small_fasta_file,1)

        for file in new_fasta_files:
            sequence_count=utilities.count_reads(file)
            self.assertEqual(sequence_count,1)
            utils.remove_temp_file(file) 

    def test_fastq_to_fasta(self):
        """
        Test the fastq_to_fasta function
        """
        
        new_fasta_file=utilities.fastq_to_fasta(
            cfg.convert_fastq_file)
        self.assertTrue(filecmp.cmp(new_fasta_file,
            cfg.convert_fasta_file, shallow=False))
        utils.remove_temp_file(new_fasta_file)                    

    def test_double_sort(self):
        """
        Test the double_sort function
        """
        
        pathways={}
        pathways["pathA"]=3
        pathways["pathB"]=3
        pathways["pathC"]=2
        pathways["pathD"]=1
        pathways["pathE"]=1
        
        double_sorted_pathways_keys_check=["pathA","pathB","pathC",
            "pathD","pathE"]
        
        double_sorted_pathways_keys=utilities.double_sort(pathways)
        
        self.assertEqual(double_sorted_pathways_keys,double_sorted_pathways_keys_check)
        
        pathways["pathA"]=0.1
        
        double_sorted_pathways_keys=utilities.double_sort(pathways)       
        
        double_sorted_pathways_keys_check=["pathB","pathC",
            "pathD","pathE","pathA"]      
        
        self.assertEqual(double_sorted_pathways_keys, double_sorted_pathways_keys_check)
        