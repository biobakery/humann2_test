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
            
                alignments.add(referenceid, 0, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the blastm8-like output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_without_header, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are unchanged
        self.assertEqual(sorted(alignments.get_hit_list()), sorted(alignments_test.get_hit_list()))
        
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
            
                alignments.add(referenceid, 0, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_with_header, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are changed
        hit1_evalue=sorted(alignments.get_hit_list())[0][-2]
        hit1_evalue_test=sorted(alignments_test.get_hit_list())[0][-2]
        self.assertAlmostEqual(math.pow(10.0,math.log(hit1_evalue)*-1),
            math.log(hit1_evalue_test)*-1,places=7)

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
            
                alignments.add(referenceid, 0, queryid, evalue,"unclassified")
            
        file_handle.close()
        
        alignments_test=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch2 output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch2_output_file_with_header_no_log, alignments_test)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # check the evalues are unchanged
        self.assertEqual(sorted(alignments.get_hit_list()), sorted(alignments_test.get_hit_list()))
        
        
    def test_translated_search_unaligned_reads_annotations_reference(self):
        """
        Test the unaligned reads and the store alignments
        Test with a rapsearch2 output file
        Test the different annotation formats are recognized for reference
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch2 output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch_file_annotations, alignments)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # three of the hits should be for gene "UniRef50"
        hits=alignments.hits_for_gene("UniRef50")
        self.assertEqual(len(hits),3)
        
                
    def test_translated_search_unaligned_reads_annotations_bug(self):
        """
        Test the unaligned reads and the store alignments
        Test with a rapsearch2 output file
        Test the different annotation formats are recognized for bug
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch2 output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch_file_annotations, alignments)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)
        
        # there should be one bug name and the other should be unclassified
        self.assertEqual(sorted(alignments.bug_list()),sorted(["s__Bacteroides_xylanisolvens","unclassified"]))
        
                
    def test_translated_search_unaligned_reads_annotations_gene_length(self):
        """
        Test the unaligned reads and the store alignments
        Test with a rapsearch2 output file
        Test the different annotation formats are recognized for gene length
        """
 
         # create a set of alignments
        alignments=store.Alignments()
        unaligned_reads_store=store.Reads()
        
        # load the rapsearch2 output with the unaligned reads function
        unaligned_file_fasta=translated_search.unaligned_reads(unaligned_reads_store, 
            cfg.rapsearch_file_annotations, alignments)
        
        # remove temp file
        utils.remove_temp_file(unaligned_file_fasta)       

        # there should be 4 hits identified
        all_hits=alignments.get_hit_list()
        self.assertEqual(len(all_hits),4)
        
        # check for set and default gene lengths
        for hit in all_hits:
            bug, reference, query, evalue, length_normalization = hit
            if reference == "UniRef50":
                self.assertEqual(length_normalization,1/(2000/1000.0))
            else:
                self.assertEqual(length_normalization,1/(1000/1000.0))


