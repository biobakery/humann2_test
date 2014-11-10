import unittest
import math

import quantify_families

class TestHumann2QuantifyFamiliesFunctions(unittest.TestCase):
    """
    Test the functions found in humann2/src/quantify_families.py
    """

    def test_compute_gene_scores_single_gene_single_query(self):
        """
        Test the compute_gene_scores function
        Test one hit for gene with one hit for query
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
        
        hits=[]
        hits.append(["bug1","gene1",gene1_length,"query1",eval1])
        hits.append(["bug1","gene2",gene2_length,"query1",eval2])
        hits.append(["bug1","gene2",gene2_length,"query2",eval3])
        hits.append(["bug1","gene3",gene3_length,"query3",eval4])
        
        gene_scores=quantify_families.compute_gene_scores(hits)
        
        # gene3
        hit4_score=math.exp(-eval4)
        query3_sum=hit4_score
        gene_score=hit4_score/query3_sum/gene3_length

        self.assertEqual(gene_scores["gene3"],gene_score)

    def test_compute_gene_scores_single_gene_double_query(self):
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
        
        hits=[]
        hits.append(["bug1","gene1",gene1_length,"query1",eval1])
        hits.append(["bug1","gene2",gene2_length,"query1",eval2])
        hits.append(["bug1","gene2",gene2_length,"query2",eval3])
        hits.append(["bug1","gene3",gene3_length,"query3",eval4])
        
        gene_scores=quantify_families.compute_gene_scores(hits)
        
        # gene1
        hit1_score=math.exp(-eval1)
        hit2_score=math.exp(-eval2)
        query1_sum=hit1_score+hit2_score
        gene_score=hit1_score/query1_sum/gene1_length

        self.assertEqual(gene_scores["gene1"],gene_score)

    def test_compute_gene_scores_double_gene_double_query(self):
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
        
        hits=[]
        hits.append(["bug1","gene1",gene1_length,"query1",eval1])
        hits.append(["bug1","gene2",gene2_length,"query1",eval2])
        hits.append(["bug1","gene2",gene2_length,"query2",eval3])
        hits.append(["bug1","gene3",gene3_length,"query3",eval4])
        
        gene_scores=quantify_families.compute_gene_scores(hits)
        
        # gene1
        hit1_score=math.exp(-eval1)
        hit2_score=math.exp(-eval2)
        query1_sum=hit1_score+hit2_score
        
        # gene2
        hit3_score=math.exp(-eval3)
        query2_sum=hit3_score
        gene_score=hit3_score/query2_sum/gene2_length + hit2_score/query1_sum/gene2_length

        self.assertEqual(gene_scores["gene2"],gene_score)

