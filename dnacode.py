mapping = {
        
'AAA':'a',
'AAC':'b',
'AAG':'c',
'AAT':'d',
'ACA':'e',
'ACC':'f', 
'ACG':'g',
'ACT':'h',
'AGA':'i',
'AGC':'j',
'AGG':'k',
'AGT':'l',
'ATA':'m',
'ATC':'n',
'ATG':'o',
'ATT':'p',
'CAA':'q',
'CAC':'r',
'CAG':'s',
'CAT':'t',
'CCA':'u',
'CCC':'v',
'CCG':'w',
'CCT':'x',
'CGA':'y',
'CGC':'z',
'CGG':'A',
'CGT':'B',
'CTA':'C',
'CTC':'D',
'CTG':'E',
'CTT':'F',
'GAA':'G',
'GAC':'H',
'GAG':'I',
'GAT':'J',
'GCA':'K',
'GCC':'L',
'GCG':'M',
'GCT':'N',
'GGA':'O',
'GGC':'P',
'GGG':'Q',
'GGT':'R',
'GTA':'S',
'GTC':'T',
'GTG':'U',
'GTT':'V',
'TAA':'W',
'TAC':'X',
'TAG':'Y',
'TAT':'Z',
'TCA':'1',
'TCC':'2',
'TCG':'3',
'TCT':'4',
'TGA':'5',
'TGC':'6',
'TGG':'7',
'TGT':'8',
'TTA':'9',
'TTC':'0',
'TTG':' ',
'TTT':'.'

	
}


encode_string = 'OME'

decode_string = 'GGAGCGCTG' 

inverted_mapping = dict(zip(mapping.values(), mapping.keys()))

def decode_dna( decode_string ):

    pieces = []
    for i in range( 0, len(decode_string), 3 ):
        piece =  decode_string[i:i+3]
        # pieces.append()
        pieces.append( mapping[piece] )

    return "".join(pieces)

def encode_dna(encode_string):
    pieces = []
    for i in encode_string:
        piece =  inverted_mapping[i]
        pieces.append(piece)
    return "".join(pieces)
  
print 'Decoded String is:- '+ decode_dna(decode_string)
print 'Encoded DNA String is:- '+ encode_dna(encode_string)

