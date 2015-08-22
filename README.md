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
