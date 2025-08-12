from Bio import SeqIO

# List the files in the order you want to concatenate
region_files = [
    "CR_extracted.fasta",  
    "COI_extracted.fasta",
    "CytB_extracted.fasta", # <-- We'll use headers from here
    "ND2_extracted.fasta",
    "ND4L_extracted.fasta"
]

# Parse all files into lists (must be same order/sample count)
parsed = [list(SeqIO.parse(f, "fasta")) for f in region_files]

# Sanity check: All lists must have same number of records
num_records = len(parsed[0])
if not all(len(r) == num_records for r in parsed):
    raise ValueError("Mismatch in number of sequences between files!")

# Create concatenated records with COI headers
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

combined_records = []
for i in range(num_records):
    header = parsed[2][i].id  # From CytB_extracted
    concatenated_seq = "".join(str(parsed[j][i].seq) for j in range(5))
    record = SeqRecord(Seq(concatenated_seq), id=header, description="")
    combined_records.append(record)

# Write to output FASTA
output_file = "Spermophilus_mtDNA_supermatrix.fasta"
SeqIO.write(combined_records, output_file, "fasta")
print(f"✅ Saved concatenated sequences with CytB headers to: {output_file}")
