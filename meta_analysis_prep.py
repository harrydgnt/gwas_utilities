import argparse
import sys

"""
Written by Harry Yang - harry2416@gmail.com

"""
def dict_add(current_file,snp_list):
        snps={}
        used_snp=[]
        for read in current_file:
                string=str(read.split()[1])
                string=string+"\t"+str(read.split()[2]+"\t")
                #print string
                #if read.split()[0] not in snp_list:
                #       continue
                if read.split()[0] == "SNP_ID":
                        continue
                snps[read.split()[0]]=string
                used_snp.append(read.split()[0])

        #item in snp_list not in used_snp]

        unused_snps=list(set(snp_list)-set(used_snp))
        print len(unused_snps)
        #print unused_snps[0]
        for item in unused_snps:
                snps[item]="NA  NA      "
        return snps

def merge_dicts(dict_args):
        # keys = set().union(*dict_args)
        keys=list(dict_args[0])
        return {k: "".join(dic.get(k, '')for dic in dict_args) for k in keys}

def get_snps(current_file):
        snps=[]
        for read in current_file:
                snp=str(read.split()[0])
                snps.append(snp)
        return snps

"""
argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("study_list", help="text file that contains studies, on each line")
parser.add_argument("snp_list", help="list of snps across the studies") # FIX - THIS CAN BE INCORPORATED LATER

args = parser.parse_args()
study_list = args.study_list
snp_list = args.snp_list
print study_list, snp_list


#FIX - ADD OUT FILE OPTION 
outfile = 'test_out.txt'



# snps = open(snp_list, 'r')
# snp_list = []
# for s in snps:
#         snp_list.append(s[:-1])
# snps.close()
studies = open(study_list, 'r')
""" 
GET SNP LIST
"""
snp_list = []
for study in studies:
        opened_study = open(study[:-1], 'r')
        dummy_snps = get_snps(opened_study)
        snp_list = snp_list + dummy_snps
        opened_study.close()
print len(snp_list)
snp_list = list(set(snp_list))
snp_list = filter(None, snp_list)
try:
        snp_list.remove("SNP_ID")
        snp_list.remove('SNP_ID')
except ValueError:
        pass
print "SHORTENING"
print len(snp_list)
if "SNP_ID" in snp_list:
        print "WRONG ONE FOUND"
"""
dict merge
"""
studies = open(study_list, 'r')
dictlist = []
for study in studies:
        print "Current study is :", study
        current_study = open(study[:-1], 'r')
        current_snps = dict_add(current_study, snp_list)
        dictlist.append(current_snps)
        current_study.close()
print "DICT LEN : ", len(dictlist)
final_dict = merge_dicts(dictlist)
outfile = open(outfile, 'w' )

for key, value in final_dict.iteritems():
        outfile.write(str(key+"\t"+value+"\n"))
outfile.close()




# if __name__ == "__main__":
#         f=open('./snp_list_five.txt','r')
#         snp_list=[]
#         for a in f:
#                 snp_list.append(a[:-1])
#         print len(snp_list)
#         one_gwas=open('./AABC.gwas','r')
#         one_snps=dict_add(one_gwas,snp_list)
#         two_gwas=open('./latina_admix.gwas','r')
#         two_snps=dict_add(two_gwas,snp_list)
#         three_gwas=open('./MEC-copy.gwas','r')
#         three_snps=dict_add(three_gwas,snp_list)
#         four_gwas=open('./BPC3.gwas','r')
#         four_snps=dict_add(four_gwas,snp_list)
#         five_gwas=open('./CGEMS.gwas','r')
#         five_snps=dict_add(five_gwas,snp_list)
#         test_dict=merge_dicts(one_snps, two_snps, three_snps, four_snps, five_snps)
#         outfile=open('./new_metasoft_input.txt','w')
#         for key, value in test_dict.iteritems():
#                 outfile.write(str(key+"\t"+value+"\n"))
#         outfile.close
