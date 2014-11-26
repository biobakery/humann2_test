import unittest
import logging
import re
import math

import cfg
import utils

import translated_search
import store
import config

class TestAdvancedHumann2TranslatedSearchFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/translated_search.py
    """
    
    def setUp(self):
        config.unnamed_temp_dir="/tmp/"
        
        # set up nullhandler for logger
        logging.getLogger('translated_search').addHandler(logging.NullHandler())

    def test_translated_search_unaligned_reads_blastm8(self):
        """
        Test the unaligned reads and the store alignments
        Test with a blastm8-like output file
        Test with empty reads structure
        Test that log of evalue is not taken
        Test that function does not require gene lengths in reference id
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # load the blastm8-like output
        file_handle=open(cfg.rapsearch2_output_file_without_header)
        
        for line in file_handle:
            if not re.search("^#",line):
                data=line.strip().split(config.blast_delimiter)
                
                referenceid=data[config.blast_reference_index]
                queryid=data[config.blast_query_index]
                evalue=float(data[config.blast_evalue_index])
            
                alignments.add(referenceid, 1, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the blastm8-like output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_without_header, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are unchanged
        self.assertEqual(sorted(alignments.all_hits()), sorted(alignments_test.all_hits()))
        
    def test_translated_search_unaligned_reads_rapsearch_log(self):
        """
        Test the unaligned reads function
        Test with a rapsearch output file
        Test that log of evalue is taken
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # load the rapsearch output
        file_handle=open(cfg.rapsearch2_output_file_with_header)
        
        for line in file_handle:
            if not re.search("^#",line):
                data=line.strip().split(config.blast_delimiter)
                
                referenceid=data[config.blast_reference_index]
                queryid=data[config.blast_query_index]
                evalue=float(data[config.blast_evalue_index])
            
                alignments.add(referenceid, 1, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_with_header, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are changed
        hit1_evalue=sorted(alignments.all_hits())[0][-1]
        hit1_evalue_test=sorted(alignments_test.all_hits())[0][-1]
        self.assertEqual(math.pow(10.0,hit1_evalue),hit1_evalue_test)

    def test_translated_search_unaligned_reads_rapsearch2_no_log(self):
        """
        Test the unaligned reads function
        Test with a rapsearch2 output file with out the log
        Test that log of evalue is not taken
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # load the rapsearch2 output
        file_handle=open(cfg.rapsearch2_output_file_with_header_no_log)
        
        for line in file_handle:
            if not re.search("^#",line):
                data=line.strip().split(config.blast_delimiter)
                
                referenceid=data[config.blast_reference_index]
                queryid=data[config.blast_query_index]
                evalue=float(data[config.blast_evalue_index])
            
                alignments.add(referenceid, 1, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch2 output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_with_header_no_log, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are unchanged
        self.assertEqual(sorted(alignments.all_hits()), sorted(alignments_test.all_hits()))


