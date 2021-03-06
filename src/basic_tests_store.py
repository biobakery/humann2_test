import unittest
import importlib
import re
import tempfile
import os

import cfg
import utils

import store

class TestHumann2StoreFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/store.py
    """

    def test_Read_print_fasta_id_count(self):
        """
        Read class: Test the loading of a full fasta file
        Test the total number of expected ids are loaded
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # Check that the total number of expected reads are loaded
        self.assertEqual(len(reads_store.id_list()), cfg.small_fasta_file_total_sequences)
            
    def test_Read_print_fasta_id_list(self):
        """
        Read class: Test the loading of a full fasta file
        Test the expected ids are loaded
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # Check the reads are printed correctly
        printed_stored_fasta=reads_store.get_fasta()
        
        compare_fasta={}
        # organize the fasta from the read class and the 
        # file of correct fasta output
        file_handle=open(cfg.small_fasta_file_single_line_sequences)
        for input in [printed_stored_fasta.split("\n"), file_handle]:
            id=""
            seq=""
            for line in input:
                if re.search(">",line):
                    # store prior id
                    if id and seq:
                        compare_fasta[id]=compare_fasta.get(id,[])+[seq]
                    id=line.strip()
                    seq=""
                else:
                    seq=line.strip()
                    
            # store the last sequence found
            if id and seq:
                compare_fasta[id]=compare_fasta.get(id,[])+[seq]
        
        file_handle.close()
        
        # check there are still the same number of ids
        self.assertEqual(len(compare_fasta.keys()),cfg.small_fasta_file_total_sequences)
        
        # check the sequences match
        for id, sequences in compare_fasta.items():
            self.assertTrue(len(sequences)==2)
            self.assertEqual(sequences[0], sequences[1])
            
    def test_Read_print_fasta_sequence_list(self):
        """
        Read class: Test the loading of a full fasta file
        Test the sequences are loaded
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # Check the reads are printed correctly
        printed_stored_fasta=reads_store.get_fasta()
        
        compare_fasta={}
        # organize the fasta from the read class and the 
        # file of correct fasta output
        file_handle=open(cfg.small_fasta_file_single_line_sequences)
        for input in [printed_stored_fasta.split("\n"), file_handle]:
            id=""
            seq=""
            for line in input:
                if re.search(">",line):
                    # store prior id
                    if id and seq:
                        compare_fasta[id]=compare_fasta.get(id,[])+[seq]
                    id=line.strip()
                    seq=""
                else:
                    seq=line.strip()
                    
            # store the last sequence found
            if id and seq:
                compare_fasta[id]=compare_fasta.get(id,[])+[seq]
        
        file_handle.close()
        
        # check the sequences match
        for id, sequences in compare_fasta.items():
            self.assertTrue(len(sequences)==2)
            self.assertEqual(sequences[0], sequences[1])
        
    def test_Read_delete_id(self):
        """
        Read class: Test the deleting of ids
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # delete all of the reads and check structure is empty
        for id in reads_store.id_list():
            reads_store.remove_id(id)
            
        self.assertEqual(len(reads_store.id_list()), 0)
        
    def test_PathwaysDatabase_read_pathways_count(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        Test for the number of pathways
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        self.assertEqual(len(pathway_list),len(pathway_list_flat))
            
    def test_PathwaysDatabase_read_pathways_ids(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        Test for the pathways ids
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        # check that the pathway ids are identical
        for pathway in pathway_list:
            self.assertTrue(pathway in pathway_list_flat)

    def test_PathwaysDatabase_read_reactions_list(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        Test for the reactions list
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
            
        # check that the reactions list for each pathway is identical
        for pathway in pathway_list:
            self.assertEqual(sorted(pathways_database_store.find_reactions(pathway)),
                sorted(pathways_database_flat_store.find_reactions(pathway)))
            
    def test_PathwaysDatabase_read_reactions_count(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        Test for the number of reactions 
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        # check for the same number of reactions
        self.assertEqual(len(pathways_database_store.reaction_list()), 
            len(pathways_database_flat_store.reaction_list()))
        
        # check that the reactions are identical
        reaction_list=pathways_database_store.reaction_list()
        reaction_list_flat=pathways_database_flat_store.reaction_list()
        for reaction in reaction_list:
            self.assertTrue(reaction in reaction_list_flat)

    def test_PathwaysDatabase_read_reactions_ids(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        Test for the reactions ids 
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        # check that the reactions are identical
        reaction_list=pathways_database_store.reaction_list()
        reaction_list_flat=pathways_database_flat_store.reaction_list()
        for reaction in reaction_list:
            self.assertTrue(reaction in reaction_list_flat)
            
    def test_PathwaysDatabase_print_flat_file_pathways_count(self):
        """
        Pathways database class: Test the printing of a flat file from a recursive file
        Test for the total number of pathways
        """
 
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)       
        
        # write the flat file created from a recursive file to a temp file
        file_out, new_file=tempfile.mkstemp()
        os.write(file_out, pathways_database_store.get_database())
        os.close(file_out)
        
        # load in the flat file and compare with the correct flat file
        pathways_database_flat_store_write=store.PathwaysDatabase(new_file, True)
        
        # remove the temp file
        utils.remove_temp_file(new_file)
        
        # check for the same number of pathways
        pathway_list=pathways_database_flat_store_write.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        self.assertEqual(len(pathway_list),len(pathway_list_flat))
            
    def test_PathwaysDatabase_print_flat_file_pathways_list(self):
        """
        Pathways database class: Test the printing of a flat file from a recursive file
        Test for the pathways list
        """
 
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)       
        
        # write the flat file created from a recursive file to a temp file
        file_out, new_file=tempfile.mkstemp()
        os.write(file_out, pathways_database_store.get_database())
        os.close(file_out)
        
        # load in the flat file and compare with the correct flat file
        pathways_database_flat_store_write=store.PathwaysDatabase(new_file, True)
        
        # remove the temp file
        utils.remove_temp_file(new_file)
        
        # check for the same number of pathways
        pathway_list=pathways_database_flat_store_write.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        # check that the pathway ids are identical
        for pathway in pathway_list:
            self.assertTrue(pathway in pathway_list_flat)
            
    def test_PathwaysDatabase_print_flat_file_reactions_list(self):
        """
        Pathways database class: Test the printing of a flat file from a recursive file
        Test the reactions list
        """
 
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file, True)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file, True)       
        
        # write the flat file created from a recursive file to a temp file
        file_out, new_file=tempfile.mkstemp()
        os.write(file_out, pathways_database_store.get_database())
        os.close(file_out)
        
        # load in the flat file and compare with the correct flat file
        pathways_database_flat_store_write=store.PathwaysDatabase(new_file, True)
        
        # remove the temp file
        utils.remove_temp_file(new_file)
        
        # check for the same number of pathways
        pathway_list=pathways_database_flat_store_write.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        
        # check that the reactions list for each pathway is identical
        for pathway in pathway_list:
            self.assertEqual(sorted(pathways_database_flat_store_write.find_reactions(pathway)),
                sorted(pathways_database_flat_store.find_reactions(pathway)))
            
    def test_ReactionsDatabase_read_reactions_count(self):
        """
        Reactions Database class: Test the storing of reactions
        Test the total number of reactions
        """
        
        reactions_database_store=store.ReactionsDatabase(cfg.reactions_file)
        
        # read in the reactions directly from the file
        file_handle=open(cfg.reactions_file)
        
        reactions={}
        for line in file_handle:
            data=line.strip().split("\t")
            reactions[data[0]]=data[2:]
        file_handle.close()
        
        # test for the same number of reactions
        self.assertEqual(len(reactions.keys()), len(reactions_database_store.reaction_list()))
            
    def test_ReactionsDatabase_read_gene_list(self):
        """
        Reactions Database class: Test the storing of reactions
        Test for the gene list
        """
        
        reactions_database_store=store.ReactionsDatabase(cfg.reactions_file)
        
        # read in the reactions directly from the file
        file_handle=open(cfg.reactions_file)
        
        reactions={}
        for line in file_handle:
            data=line.strip().split("\t")
            reactions[data[0]]=data[2:]
        file_handle.close()
        
        # test for the same reactions and genes
        for rxn in reactions:
            self.assertEqual(reactions[rxn],reactions_database_store.find_genes(rxn))
            
    def test_PathwaysAndReactions_median_score_odd_number_vary_reactions(self):
        """
        Pathways and Reactions class: Test add and median score
        Test and odd number of values and different reactions
        """
        
        pathways_and_reactions=store.PathwaysAndReactions()
        
        # add scores all for same pathway and different reaction
        pathways_and_reactions.add("bug","P1","R1",1)
        pathways_and_reactions.add("bug","P1","R2",2)        
        pathways_and_reactions.add("bug","P1","R3",3)
        pathways_and_reactions.add("bug","P1","R4",4)
        pathways_and_reactions.add("bug","P1","R5",5)  
        
        # test median score for odd number of values
        self.assertEqual(pathways_and_reactions.median_score("bug"),3)
        
    def test_PathwaysAndReactions_median_score_even_number_vary_reactions(self):
        """
        Pathways and Reactions class: Test add and median score
        Test an even number of values and different reactions
        """
        
        pathways_and_reactions=store.PathwaysAndReactions()
        
        # add scores all for same pathway and  different reaction
        pathways_and_reactions.add("bug","P1","R1",1)
        pathways_and_reactions.add("bug","P1","R2",2)        
        pathways_and_reactions.add("bug","P1","R3",3)
        pathways_and_reactions.add("bug","P1","R4",4) 
        
        # test median score for an even number of values
        self.assertEqual(pathways_and_reactions.median_score("bug"),2.5)    
        
    def test_PathwaysAndReactions_median_score_odd_number_vary_pathways(self):
        """
        Pathways and Reactions class: Test add and median score
        Test an odd number of values and different pathways
        """
        
        pathways_and_reactions=store.PathwaysAndReactions()        
        
        # add scores all for same pathway and reaction
        pathways_and_reactions.add("bug","P1","R1",1)
        pathways_and_reactions.add("bug","P2","R1",2)        
        pathways_and_reactions.add("bug","P3","R1",3)
        pathways_and_reactions.add("bug","P4","R1",4)
        pathways_and_reactions.add("bug","P5","R1",5)  
        
        # test median score for odd number of values
        self.assertEqual(pathways_and_reactions.median_score("bug"),3)
        
    def test_PathwaysAndReactions_median_score_even_number_vary_pathways(self):
        """
        Pathways and Reactions class: Test add and median score
        Test an even number of values and different pathways
        """
        
        pathways_and_reactions=store.PathwaysAndReactions()
        
        # add scores all for same pathway and reaction
        pathways_and_reactions.add("bug","P1","R1",1)
        pathways_and_reactions.add("bug","P2","R2",2)        
        pathways_and_reactions.add("bug","P3","R3",3)
        pathways_and_reactions.add("bug","P4","R4",4) 
        
        # test median score for an even number of values
        self.assertEqual(pathways_and_reactions.median_score("bug"),2.5)         
        
    def test_Alignments_add_bug_count(self):
        """
        Alignments class: Test add function
        Test the total bugs
        """             
        
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # check the total bugs
        self.assertEqual(alignments_store.count_bugs(),3)
        
    def test_Alignments_add_gene_count(self):
        """
        Alignments class: Test add function
        Test the total genes
        """             
        
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # check the total genes
        self.assertEqual(alignments_store.count_genes(),3)
        
    def test_Alignments_add_bug_list(self):
        """
        Alignments class: Test add function
        Test the bug list
        """             
        
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # check bug list
        self.assertEqual(sorted(alignments_store.bug_list()),["bug1","bug2","bug3"])
        
    def test_Alignments_add_gene_list(self):
        """
        Alignments class: Test add function
        Test the gene list
        """             
        
        alignments_store=store.Alignments()
        
        alignments_store.add("gene2", 1, "Q3", 0.01, "bug1")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug2")
        alignments_store.add("gene3", 1, "Q2", 0.01, "bug3")
        alignments_store.add("gene1", 1, "Q1", 0.01, "bug1")
        
        # check gene list
        self.assertEqual(sorted(alignments_store.gene_list()),["gene1","gene2","gene3"])        
        
    def test_Alignments_process_chocophlan_length(self):
        """
        Test the process_chocophlan_length with standard length format
        """
        
        alignments_store=store.Alignments()
        
        length=alignments_store.process_chocophlan_length("1-100","gene")
        
        self.assertEqual(length, 100)
        
    def test_Alignments_process_chocophlan_length_multiple(self):
        """
        Test the process_chocophlan_length with multiple lengths
        Test with one length on the reverse strand
        """
        
        alignments_store=store.Alignments()
        
        length=alignments_store.process_chocophlan_length("c:100-1,1-100","gene")
        
        self.assertEqual(length, 200) 

    def test_GeneScores_add(self):
        """
        GeneScores class: Test add function
        """
        
        gene_scores=store.GeneScores()
        
        bug1_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug1_scores,"bug1")
        
        bug2_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug2_scores,"bug2")
        
        self.assertEqual(gene_scores.count_genes_for_bug("bug1"),2)
        
    def test_GeneScores_add_second_set(self):
        """
        GeneScores class: Test add function
        Test adding a second set of scores to bug set
        """
        
        gene_scores=store.GeneScores()
        
        bug1_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug1_scores,"bug1")
        
        bug1_scores_2={"gene3":1,"gene4":2, "gene2":22}
        gene_scores.add(bug1_scores_2,"bug1")
        
        self.assertEqual(gene_scores.count_genes_for_bug("bug1"),4)
        
    def test_GeneScores_get_score(self):
        """
        GeneScores class: Test get_score function
        """
        
        gene_scores=store.GeneScores()
        
        bug1_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug1_scores,"bug1")
        
        bug2_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug2_scores,"bug2")
        
        self.assertEqual(gene_scores.get_score("bug1","gene2"),2)
        
    def test_GeneScores_get_score_second_set(self):
        """
        GeneScores class: Test get_score function
        Test getting the score for a second set of scores added to bug set
        """
        
        gene_scores=store.GeneScores()
        
        bug1_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug1_scores,"bug1")
        
        bug1_scores_2={"gene3":1,"gene4":2, "gene2":22}
        gene_scores.add(bug1_scores_2,"bug1")
        
        # Test that the most recent score for gene2 is returned
        self.assertEqual(gene_scores.get_score("bug1","gene2"),22)
        
    def test_GeneScores_scores_for_bug(self):
        """
        GeneScores class: Test scores_for_bug
        """
  
        gene_scores=store.GeneScores()
        
        bug1_scores={"gene1":1,"gene2":2}
        gene_scores.add(bug1_scores,"bug1")
        
        bug1_scores_2={"gene3":1,"gene4":2, "gene2":22}
        gene_scores.add(bug1_scores_2,"bug1")
        
        # Test that the most recent score for gene2 is returned
        self.assertDictEqual(gene_scores.scores_for_bug("bug1"),
            {"gene1":1,"gene2":22,"gene3":1,"gene4":2})      
    
    def test_GeneScores_add_from_file_bug_list(self):
        """
        GeneScores class: Test add_from_file bug list
        """
        
        gene_scores=store.GeneScores()
        
        gene_scores.add_from_file(cfg.genetable_file)
        
        # Test the bug list is as expected
        self.assertEqual(sorted(cfg.genetable_file_bug_scores.keys()),sorted(gene_scores.bug_list()))
        
    def test_GeneScores_add_from_file_gene_list(self):
        """
        GeneScores class: Test add_from_file gene list
        """
        
        gene_scores=store.GeneScores()
        
        gene_scores.add_from_file(cfg.genetable_file)
        
        # Create a list of all of the genes in the table
        genes={}
        for bug in cfg.genetable_file_bug_scores:
            for gene in cfg.genetable_file_bug_scores[bug]:
                genes[gene]=1
        
        # Test the gene list is as expected
        self.assertEqual(sorted(genes.keys()),sorted(gene_scores.gene_list()))
        
    def test_GeneScores_add_from_file_scores(self):
        """
        GeneScores class: Test add_from_file scores
        """
        
        gene_scores=store.GeneScores()
        
        gene_scores.add_from_file(cfg.genetable_file)
        
        # Test the scores for all bugs and genes
        for bug in cfg.genetable_file_bug_scores:
            self.assertDictEqual(cfg.genetable_file_bug_scores[bug],gene_scores.scores_for_bug(bug))
            
        