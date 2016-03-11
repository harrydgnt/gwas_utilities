

import argparse 
import sys


"""
argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("gwas_file", help="output from pylmm")
parser.add_argument("index_file", help="snp_index file - col 1 = chr:coord, col 2 = rsid")
praser.add_argument("outfile", help="the name of output text file for manhattan plot")

args = parser.parse_args()
gwas_file = args.gwas_file
index_file = args.index_file
outfile = open(args.outfile, 'w')
print study_list, outfile

index = open(index_file, 'r')
coord_list = {}
for line in index:
        coord_list[line.split()[0]] = str(line.split()[1])

gwas = open(gwas_file, 'r')
snp_list = {}
for line in gwas:
        snp_list[coord_list[line.split()[0]]] = line.split()[1:]


for key, value in snp_list.iteritems():
        try:
                counter=counter+1
                if counter%1000 == 0:
                        print counter
                answer=str(key + "\t" + value + "\n")
                outfile.write(answer)
        except KeyError:
                continue
gwas.close()
index.close()
outfile.close()
