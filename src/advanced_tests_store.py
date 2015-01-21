import unittest
import logging
import os
import sys
import math

import cfg

import store


class TestAdvancedHumann2UtilitiesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/store.py
    """
    
    def setUp(self):
        # set up nullhandler for logger
        logging.getLogger('store').addHandler(logging.NullHandler())
        
    def test_Alignments_compute_gene_scores_single_gene_single_query(self):
        """
        Test the compute_gene_scores function
        Test one hit for gene with one hit for query
        """
        
        # create a set of hits
        eval1=1e-4
        eval2=3e-7
        eval3=2e-10
        eval4=2e-10
        
        gene1_length=2
        gene2_length=3
        gene3_length=4
        
        # Create a set of alignments
        alignments_store=store.Alignments()
        alignments_store.add("gene1",gene1_length,"query1",eval1,"bug1")
        alignments_store.add("gene2",gene2_length,"query1",eval2,"bug1")
        alignments_store.add("gene2",gene2_length,"query2",eval3,"bug1")
        alignments_store.add("gene3",gene3_length,"query3",eval4,"bug1")
        
        gene_scores_store=store.GeneScores()
        
        # compute gene scores
        alignments_store.convert_alignments_to_gene_scores(gene_scores_store)
        
        # convert lengths to per kb
        gene3_length=gene3_length/1000.0
        
        # gene3
        hit4_score=math.exp(-eval4)
        query3_sum=hit4_score
        gene_score=hit4_score/query3_sum/gene3_length

        self.assertEqual(gene_scores_store.get_score("bug1","gene3"),gene_score)

    def test_Alignments_compute_gene_scores_single_gene_double_query(self):
        """
        Test the compute_gene_scores function
        Test one hit for gene with more than one hit per query
        """
        
        # create a set of hits
        # bug, reference, reference_length, query, evalue = hit
        
        eval1=1e-4
        eval2=3e-7
        eval3=2e-10
        eval4=2e-10
        
        gene1_length=2
        gene2_length=3
        gene3_length=4
        
        # Create a set of alignments
        alignments_store=store.Alignments()
        alignments_store.add("gene1",gene1_length,"query1",eval1,"bug1")
        alignments_store.add("gene2",gene2_length,"query1",eval2,"bug1")
        alignments_store.add("gene2",gene2_length,"query2",eval3,"bug1")
        alignments_store.add("gene3",gene3_length,"query3",eval4,"bug1")
        
        gene_scores_store=store.GeneScores()
        
        # compute gene scores
        alignments_store.convert_alignments_to_gene_scores(gene_scores_store)
        
        # convert lengths to per kb
        gene1_length=gene1_length/1000.0
        
        # gene1
        hit1_score=math.exp(-eval1)
        hit2_score=math.exp(-eval2)
        query1_sum=hit1_score+hit2_score
        gene_score=hit1_score/query1_sum/gene1_length

        self.assertEqual(gene_scores_store.get_score("bug1","gene1"),gene_score)

    def test_Alignments_compute_gene_scores_double_gene_double_query(self):
        """
        Test the compute_gene_scores function
        Test two hits to gene with more than one hit per query
        """
        
        # create a set of hits
        # bug, reference, reference_length, query, evalue = hit
        
        eval1=1e-4
        eval2=3e-7
        eval3=2e-10
        eval4=2e-10
        
        gene1_length=2
        gene2_length=3
        gene3_length=4
        
        # Create a set of alignments
        alignments_store=store.Alignments()
        alignments_store.add("gene1",gene1_length,"query1",eval1,"bug1")
        alignments_store.add("gene2",gene2_length,"query1",eval2,"bug1")
        alignments_store.add("gene2",gene2_length,"query2",eval3,"bug1")
        alignments_store.add("gene3",gene3_length,"query3",eval4,"bug1")
        
        gene_scores_store=store.GeneScores()
        
        # compute gene scores
        alignments_store.convert_alignments_to_gene_scores(gene_scores_store)
        
        # gene1
        hit1_score=math.exp(-eval1)
        hit2_score=math.exp(-eval2)
        query1_sum=hit1_score+hit2_score
        
        # convert lengths to per kb
        gene2_length=gene2_length/1000.0
        
        # gene2
        hit3_score=math.exp(-eval3)
        query2_sum=hit3_score
        gene_score=hit3_score/query2_sum/gene2_length + hit2_score/query1_sum/gene2_length

        self.assertEqual(gene_scores_store.get_score("bug1","gene2"),gene_score)
        
    def test_Alignments_id_mapping_all_gene_list(self):
        """
        Test the store_id_mapping function
        Test the add_annotated and process_reference_annotation with id mapping
        Test the genes are mapped correctly
        """
        
        alignments_store=store.Alignments()
        
        # load in the id_mapping file
        alignments_store.store_id_mapping(cfg.id_mapping_file)
        
        # store some alignments
        alignments_store.add_annotated("query1",1,"ref1")
        alignments_store.add_annotated("query2",1,"ref2")
        alignments_store.add_annotated("query3",1,"ref3")
        
        # test the genes are correct
        self.assertEqual(sorted(alignments_store.gene_list()),sorted(["gene1","gene2","gene3"]))
        
    def test_Alignments_id_mapping_all_bug_list(self):
        """
        Test the store_id_mapping function
        Test the add_annotated and process_reference_annotation with id mapping
        Test the bugs are mapped correctly
        """
        
        alignments_store=store.Alignments()
        
        # load in the id_mapping file
        alignments_store.store_id_mapping(cfg.id_mapping_file)
        
        # store some alignments
        alignments_store.add_annotated("query1",1,"ref1")
        alignments_store.add_annotated("query2",1,"ref2")
        alignments_store.add_annotated("query3",1,"ref3")
        
        # test the bugs are correct
        self.assertEqual(sorted(alignments_store.bug_list()),sorted(["bug3","unclassified"]))
        
    def test_Alignments_id_mapping_all_hits(self):
        """
        Test the store_id_mapping function
        Test the add_annotated and process_reference_annotation with id mapping
        Test the lengths are mapped correctly
        """
        
        alignments_store=store.Alignments()
        
        # load in the id_mapping file
        alignments_store.store_id_mapping(cfg.id_mapping_file)
        
        # store some alignments
        alignments_store.add_annotated("query1",1,"ref1")
        alignments_store.add_annotated("query2",1,"ref2")
        alignments_store.add_annotated("query3",1,"ref3")
        
        # test the lengths are correct
        stored_lengths=[item[-1] for item in alignments_store.get_hit_list()]
        self.assertEqual(sorted(stored_lengths),sorted([1.0/1000,10.0/1000,1.0]))
        
    def test_Alignments_id_mapping_half_hits(self):
        """
        Test the store_id_mapping function
        Test the add_annotated and process_reference_annotation with id mapping
        Test the lengths are mapped correctly with only some references included
        in those provided for id mapping
        """
        
        alignments_store=store.Alignments()
        
        # load in the id_mapping file
        alignments_store.store_id_mapping(cfg.id_mapping_file)
        
        # store some alignments
        alignments_store.add_annotated("query1",1,"ref1")
        alignments_store.add_annotated("query2",1,"ref2")
        alignments_store.add_annotated("query3",1,"ref1|100")
        alignments_store.add_annotated("query3",1,"200|ref2")
        
        # test the lengths are correct
        stored_lengths=[item[-1] for item in alignments_store.get_hit_list()]
        self.assertEqual(sorted(stored_lengths),sorted([1.0/1000,100.0/1000,
            200.0/1000.0,1.0]))
        
