import subprocess


for i in range(1,21):
	cmd= "cat scaffolds_new_5.0_hg38.bed | grep -w chr{} | awk '$3-$2 > 1000000'".format(i)
	print cmd
	output = subprocess.check_output(cmd,shell=True)

	lines = output.strip().split('\n')
	scaffolds = set()
	for line in lines:
		attrs = line.split('\t')
		attrs[3] = attrs[3].split(':')
		if 'Reverse' in attrs[3][0]:
			attrs[3][0] = attrs[3][0][:-len('Reverse')-1]
		scaffolds.add(attrs[3][0])

	cmd = "samtools faidx scaffolds_new_5.0.fasta "
	for each in scaffolds:
		cmd += each+" "
	cmd += '> chromosomes_5.0/chr'+str(i)+'_predicted.fasta'
	print cmd
	op = subprocess.check_output(cmd,shell=True)


cmd= "cat scaffolds_new_5.0_hg38.bed | grep -w chrX | awk '$3-$2 > 1000000'".format(i)
output = subprocess.check_output(cmd,shell=True)

lines = output.strip().split('\n')
scaffolds = set()
for line in lines:
	attrs = line.split('\t')
	attrs[3] = attrs[3].split(':')
	if 'Reverse' in attrs[3][0]:
		attrs[3][0] = attrs[3][0][:-len('Reverse')-1]
	scaffolds.add(attrs[3][0])

cmd = "samtools faidx scaffolds_new_5.0.fasta "
for each in scaffolds:
	cmd += each+" "
cmd += '> chromosomes_5.0/chrX_predicted.fasta'
op = subprocess.check_output(cmd,shell=True)