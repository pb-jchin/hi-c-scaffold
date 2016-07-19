from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

import re 


def main():
    RF = 'AAGCTT'
    for record in SeqIO.parse('../scaffold/chromosomes/NA19240_test_asm_p_ctg_2016-05-16.cleaned.fa', "fasta"):
        
        id,seq = record.id, str(record.seq)

        pos  = [m.start(0) for m in re.finditer(RF,seq)]
     
        length = len(seq)

        left_count = 0
        rigt_count = 0
        for each in pos:
        	if each < length/2:
        		left_count += 1
        	else:
        		rigt_count += 1

        print id, left_count, rigt_count

    

if __name__ == '__main__':
    main()