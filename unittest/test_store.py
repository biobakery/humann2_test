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

    def test_Read_print_fasta(self):
        """
        Read class: Test the loading of a full fasta file
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # Check that the total number of expected reads are loaded
        self.assertEqual(len(reads_store.id_list()), cfg.small_fasta_file_total_sequences)
        
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
        
    def test_Read_delete_id(self):
        """
        Read class: Test the deleting of ids
        """
        
        reads_store=store.Reads(cfg.small_fasta_file)
        
        # delete all of the reads and check structure is empty
        for id in reads_store.id_list():
            reads_store.remove_id(id)
            
        self.assertEqual(len(reads_store.id_list()), 0)
        
    def test_PathwaysDatabase_read(self):
        """
        Pathways database class: Test the storing of a recursive set of pathways
        """
        
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file)
        
        # check for the same number of pathways
        pathway_list=pathways_database_store.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        self.assertEqual(len(pathway_list),len(pathway_list_flat))
        
        # check that the pathway ids are identical
        for pathway in pathway_list:
            self.assertTrue(pathway in pathway_list_flat)
            
        # check that the reactions list for each pathway is identical
        for pathway in pathway_list:
            self.assertEqual(pathways_database_store.find_reactions(pathway),
                pathways_database_flat_store.find_reactions(pathway))
        
        # check for the same number of reactions
        self.assertEqual(len(pathways_database_store.reaction_list()), 
            len(pathways_database_flat_store.reaction_list()))
        
        # check that the reactions are identical
        reaction_list=pathways_database_store.reaction_list()
        reaction_list_flat=pathways_database_flat_store.reaction_list()
        for reaction in reaction_list:
            self.assertTrue(reaction in reaction_list_flat)
            
    def test_PathwaysDatabase_print_flat_file(self):
        """
        Pathways database class: Test the printing of a flat file from a recursive file
        """
 
        pathways_database_store=store.PathwaysDatabase(cfg.pathways_file)
        pathways_database_flat_store=store.PathwaysDatabase(cfg.pathways_flat_file)       
        
        # write the flat file created from a recursive file to a temp file
        file_out, new_file=tempfile.mkstemp()
        os.write(file_out, pathways_database_store.get_database())
        os.close(file_out)
        
        # load in the flat file and compare with the correct flat file
        pathways_database_flat_store_write=store.PathwaysDatabase(new_file)
        
        # remove the temp file
        utils.remove_temp_file(new_file)
        
        # check for the same number of pathways
        pathway_list=pathways_database_flat_store_write.pathway_list()
        pathway_list_flat=pathways_database_flat_store.pathway_list()
        self.assertEqual(len(pathway_list),len(pathway_list_flat))
        
        # check that the pathway ids are identical
        for pathway in pathway_list:
            self.assertTrue(pathway in pathway_list_flat)
        
        # check that the reactions list for each pathway is identical
        for pathway in pathway_list:
            self.assertEqual(pathways_database_flat_store_write.find_reactions(pathway),
                pathways_database_flat_store.find_reactions(pathway))
        

