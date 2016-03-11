if [ $# -lt 3 ]
then
echo "Get sra files to bam"
echo "[1] list of SRA files from Accession"
echo "[2] dir where it would be saved"
echo "[3] the directory where SRA files would be saved"
exit 1
fi

cd $2

while read line
do
echo "/u/home/h/harryyan//sratoolkit.2.5.0-centos_linux64/bin/prefetch -v $line" >> download_files.sh
name=$(echo $line | awk -F '.sra' '{print $1}')
echo "/u/home/h/harryyan/sratoolkit.2.5.0-centos_linux64/bin/sam-dump $3/${line}.sra | samtools view -bS - > $2/${name}.bam " >> download_files.sh
echo "rm $3/$line.sra " >> download_files.sh
echo $name
done<$1