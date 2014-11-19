
import os

verbose=False

data_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)),"data")

small_fasta_file=os.path.join(data_folder,"file.fasta")
small_fasta_file_total_sequences=3
small_fastq_file=os.path.join(data_folder,"file.fastq")
small_fastq_file_total_sequences=2

convert_fastq_file=os.path.join(data_folder,"convert_file.fastq")
convert_fasta_file=os.path.join(data_folder,"convert_file.fasta")

small_fasta_file_single_line_sequences=os.path.join(data_folder,"file_single_line_sequences.fasta")

pathways_file=os.path.join(data_folder, "pathways.tsv")
pathways_flat_file=os.path.join(data_folder, "pathways_flat.tsv")

reactions_file=os.path.join(data_folder, "reactions.tsv")

usearch_file=os.path.join(data_folder, "usearch_output.tsv")
usearch_file_bug_list=["bug1","bug2","bug3","unclassified"]
usearch_file_gene_list=["UniRef50_unknown","gene1","gene2","gene3","gene4","gene5"]

gene_familes_file=os.path.join(data_folder, "gene_families.tsv")

sam_file_with_header=os.path.join(data_folder, "file_with_header.sam")
sam_file_without_header=os.path.join(data_folder, "file_without_header.sam")
sam_file_without_header_with_tags=os.path.join(data_folder, "file_without_header_with_tags.sam")
rapsearch2_output_file_with_header=os.path.join(data_folder, "rapsearch2_output_with_header.m8")
rapsearch2_output_file_without_header=os.path.join(data_folder, "rapsearch2_output_without_header.m8")

