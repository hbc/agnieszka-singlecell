## overview
This project is with Agnieszka Czechowitz as part of the Rossi lab, they are
looking at two types of cells, MPP (multipotent progenitors) and hematopoetic
stem cells (HSCs). They did single-cell RNA-seq using SMART-seq2.  They had
four lanes of a single plate, with 48 MPPs and 48 HSCs. They want to look at
differences between the two types of cells and also to see if there are some
smaller subpopulations of cells within the HSC/MPP populations.

## setup

Steps to get the data:

1) run the script run.sh which downloads the data from the Broad. This is the contents of the script, it just logs in and grabs everything.
wget --tries=10 --continue --mirror --user {user} --password {password} --no-check-certificate ftp://ftp.broadinstitute.org

2) copy the aligned.bam files to the data directory:
mkdir data
python scripts/setup_files.py ftp.broadinstitute.org/ *aligned*.bam

3) create a CSV file to merge together the files
cd data
python ../scripts/create_csv.py > agnieszka-singlecell.csv

4) merge the samples together
bcbio_prepare_samples.py --out merged --csv agnieszka-singlecell.csv

5) get the appropriate bcbio template
wget https://raw.githubusercontent.com/chapmanb/bcbio-nextgen/master/config/templates/illumina-rnaseq.yaml

6) edit to map to mm10 and just trim polyA

7) create template
bcbio_nextgen.py -w template illumina-rnaseq.yaml agnieszka-singlecell-merged.csv data/merged/

8) run the analysis
cp scripts/run-analysis.sh agnieszka-singlecell-merged/work/.
cd !$
sbatch < run-analysis.sh

9) final directory has the counts, final alignment files and other QC information

10) run bcbio.rnaseq (http://www.github.com/roryk/bcbio.rnaseq) to generate a report.
