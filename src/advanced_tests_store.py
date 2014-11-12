import unittest
import logging
import os
import sys

import cfg

import store


class TestAdvancedHumann2UtilitiesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/store.py
    """
    
    def setUp(self):
        # set up nullhandler for logger
        logging.getLogger('store').addHandler(logging.NullHandler())
        
    def test_Alignments_filter_hits_bug_count(self):
        """
        Test the filter hits function in the Alignments class with
        a reactions database
        
        Test total number of bugs
        """
    
        # Create a reactions database
        reactions_database=store.ReactionsDatabase(cfg.reactions_file)
    
        # Create a set of alignments
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # Add some genes to the alignments set that are in the reactions database
        # Associate these with 2 more bugs
        genes=reactions_database.gene_list()
        alignments_store.add(genes[0], 1, "Q3", 0.01, "bug1")
        alignments_store.add(genes[1], 1, "Q1", 0.01, "bug4")
        alignments_store.add(genes[2], 1, "Q2", 0.01, "bug5")
        alignments_store.add(genes[3], 1, "Q1", 0.01, "bug1")       
        
        # Redirect stdout
        sys.stdout=open(os.devnull,"w")
        
        # Filter hits not associated with genes in the reactions database
        alignments_store.filter_hits(reactions_database)
        
        # Undo stdout redirect
        sys.stdout=sys.__stdout__
        
        # Check the total bugs
        self.assertEqual(alignments_store.count_bugs(),3)
        
    def test_Alignments_filter_hits_gene_count(self):
        """
        Test the filter hits function in the Alignments class with
        a reactions database
        
        Test total number of genes
        """
    
        # Create a reactions database
        reactions_database=store.ReactionsDatabase(cfg.reactions_file)
    
        # Create a set of alignments
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # Add some genes to the alignments set that are in the reactions database
        genes=reactions_database.gene_list()
        alignments_store.add(genes[0], 1, "Q3", 0.01, "bug1")
        alignments_store.add(genes[1], 1, "Q1", 0.01, "bug1")
        alignments_store.add(genes[2], 1, "Q2", 0.01, "bug1")
        alignments_store.add(genes[3], 1, "Q1", 0.01, "bug1")       
        
        # Redirect stdout
        sys.stdout=open(os.devnull,"w")
        
        # Filter hits not associated with genes in the reactions database
        alignments_store.filter_hits(reactions_database)
        
        # Undo stdout redirect
        sys.stdout=sys.__stdout__
        
        # Check the total genes
        self.assertEqual(alignments_store.count_genes(),4)
        
    def test_Alignments_filter_hits_bug_list(self):
        """
        Test the filter hits function in the Alignments class with
        a reactions database
        
        Test the bugs list
        """
    
        # Create a reactions database
        reactions_database=store.ReactionsDatabase(cfg.reactions_file)
    
        # Create a set of alignments
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # Add some genes to the alignments set that are in the reactions database
        # Associate these with 2 more bugs
        genes=reactions_database.gene_list()
        alignments_store.add(genes[0], 1, "Q3", 0.01, "bug1")
        alignments_store.add(genes[1], 1, "Q1", 0.01, "bug4")
        alignments_store.add(genes[2], 1, "Q2", 0.01, "bug5")
        alignments_store.add(genes[3], 1, "Q1", 0.01, "bug1")       
        
        # Redirect stdout
        sys.stdout=open(os.devnull,"w")
        
        # Filter hits not associated with genes in the reactions database
        alignments_store.filter_hits(reactions_database)
        
        # Undo stdout redirect
        sys.stdout=sys.__stdout__
        
        # Check the bugs list
        self.assertEqual(sorted(alignments_store.bug_list()),["bug1","bug4","bug5"])
        
    def test_Alignments_filter_hits_gene_count(self):
        """
        Test the filter hits function in the Alignments class with
        a reactions database
        
        Test the gene list
        """
    
        # Create a reactions database
        reactions_database=store.ReactionsDatabase(cfg.reactions_file)
    
        # Create a set of alignments
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # Add some genes to the alignments set that are in the reactions database
        genes=reactions_database.gene_list()
        alignments_store.add(genes[0], 1, "Q3", 0.01, "bug1")
        alignments_store.add(genes[1], 1, "Q1", 0.01, "bug1")
        alignments_store.add(genes[2], 1, "Q2", 0.01, "bug1")
        alignments_store.add(genes[3], 1, "Q1", 0.01, "bug1")       
        
        # Redirect stdout
        sys.stdout=open(os.devnull,"w")
        
        # Filter hits not associated with genes in the reactions database
        alignments_store.filter_hits(reactions_database)
        
        # Undo stdout redirect
        sys.stdout=sys.__stdout__
        
        # Check the gene list
        self.assertEqual(sorted(alignments_store.gene_list()),sorted(genes[0:4])) 