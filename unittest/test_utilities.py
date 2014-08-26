import unittest, importlib, os

import config

class TestHumann2UtilitiesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/utilities.py
    """

    def setUp(self):
        self.utilities=importlib.import_module('utilities')

    def test_file_exists_readable(self):
        self.utilities.file_exists_readable(os.path.basename(__file__))

    def test_count_reads(self):
	fasta_seqs=self.utilities.count_reads(config.small_fasta_file)
	self.assertEqual(fasta_seqs, config.small_fasta_file_total_sequences)                

	fastq_seqs=self.utilities.count_reads(config.small_fastq_file)
	self.assertEqual(fastq_seqs, config.small_fastq_file_total_sequences)     

    def test_estimate_unaligned_reads(self):
        percent_unaligned=self.utilities.estimate_unaligned_reads(
            config.small_fasta_file, config.small_fastq_file)

        percent_expected=int(config.small_fastq_file_total_sequences / 
            float(config.small_fasta_file_total_sequences)*100)

        self.assertEqual(percent_unaligned, str(percent_expected))   

        percent_unaligned=self.utilities.estimate_unaligned_reads(
            config.small_fastq_file, config.small_fastq_file)

        percent_expected=int(config.small_fastq_file_total_sequences / 
            float(config.small_fastq_file_total_sequences)*100)

        self.assertEqual(percent_unaligned, str(percent_expected))   
               
