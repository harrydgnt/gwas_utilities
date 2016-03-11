import argparse 
import sys


"""
argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("gwas_file", help="output from pylmm")
parser.add_argument("map_file", help="map file (plink format)")
praser.add_argument("outfile", help="the name of output text file for manhattan plot")

args = parser.parse_args()
gwas_file = args.gwas_file
mapfile = args.map_file
outfile = open(args.outfile, 'w')
print study_list, outfile



snpfile=open(gwas_file,'r')
snp_list={}
for item in snpfile:
        snp_list[item.split()[0]]=item.split()[4]
searchfile=open(mapfile,'r')
counter=0
map_list={}
for line in searchfile:
        map_list[line.split()[1]]=str(line.split()[0] + "\t" + line.split()[3])
for key, value in snp_list.iteritems():
        counter=counter+1
        if counter%100==0:
                print "Processed ", counter, "SNPS"
        answer = str(map_list[key] + "\t" + key + "\t" + value + "\n")
        outfile.write(answer)
searchfile.close()
snpfile.close()
outfile.close()
