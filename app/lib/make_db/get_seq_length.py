import os,sys
import urllib2
import re
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


def seqlen(fastaf,fileo):
	fout=open(fileo,'w')
	for record in SeqIO.parse(fastaf,"fasta"):
		  fout.write("\t".join([record.id,str(len(record.seq)),"\n"]))
	fout.close()


#fastaf=sys.argv[1]
#fileo=sys.argv[2]

#seqlen(fastaf,fileo)
