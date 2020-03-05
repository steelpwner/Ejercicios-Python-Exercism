def to_rna(dna_strand):
    comp = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return ''.join([comp[x] for x in dna_strand])
