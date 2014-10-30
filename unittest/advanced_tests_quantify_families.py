import unittest
import re
import tempfile
import os
import filecmp

import cfg
import utils

import quantify_families
import store
import config

class TestHumann2QuantifyFamiliesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/quantify_families.py
    """

    def test_gene_families(self):
        """
        Test the gene families function and the blast config indexes
        """
        
        # create a set of alignments
        alignments=store.Alignments()
        
        # load the usearch output
        file_handle=open(cfg.usearch_file)
        
        for line in file_handle:
            if not re.search("^#",line):
                data=line.strip().split(config.blast_delimiter)
                
                referenceids=data[config.blast_reference_index].split("|")
                queryid=data[config.blast_query_index]
                evalue=float(data[config.blast_evalue_index])
            
                alignments.add(referenceids[1], 1, queryid, evalue,referenceids[0])
            
        file_handle.close()
        
        # check the bugs and genes were loaded correctly
        self.assertEqual(sorted(cfg.usearch_file_bug_list),sorted(alignments.bug_list()))
        
        self.assertEqual(sorted(cfg.usearch_file_gene_list),sorted(alignments.gene_list()))
        
        # set the output format
        config.output_format="tsv"
        
        # set the location of the file to write to as a temp file
        file_out, gene_families_file=tempfile.mkstemp()
        os.close(file_out)
        config.genefamilies_file=gene_families_file
        
        # obtain the gene families
        gene_scores=store.GeneScores()
        gene_families_file=quantify_families.gene_families(alignments, gene_scores)
        
        # check the gene families output is as expected
        self.assertTrue(filecmp.cmp(gene_families_file,
            cfg.gene_familes_file, shallow=False))
        
        # delete the temp file
        utils.remove_temp_file(gene_families_file)
        
