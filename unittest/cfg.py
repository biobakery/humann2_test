
import os

verbose=False

data_folder="data"

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

