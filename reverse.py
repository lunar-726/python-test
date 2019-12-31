from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC
chr = SeqIO.read("/home/sjchen/assembly.fasta","fasta")
chr = chr[1012:36719].reverse_complement()+chr[36719:].reverse_complement()
chr.id="chr"
chr.description=""
final= SeqIO.write(chr, "ABP100_final.fasta", "fasta")
