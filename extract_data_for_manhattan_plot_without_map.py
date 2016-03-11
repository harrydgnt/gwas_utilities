

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


gwas=open(gwas_file,'r')
snp_list={}
for item in gwas:
        snp_list[item.split()[0]]=item.split()[4]

index=open(index_file,'r')
coord_list={}
counter=0
for line in index:
        counter=counter+1
        if counter%1000 == 0:
                print counter
        coord_list[line.split()[1]]=str(line.split()[0].split(':')[0] + "\t" + line.split()[0].split(':')[1])
counter = 0
for key, value in snp_list.iteritems():
        try:
                counter=counter+1
                if counter%1000 == 0:
                        print counter
                answer=str(coord_list[key] + "\t" + key + "\t" + value + "\n")
                outfile.write(answer)
        except KeyError:
                continue
gwas.close()
index.close()
outfile.close()
