import fnmatch
import os
from argparse import ArgumentParser
import shutil
import sys

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--output", default="data", help="directory to output files")
    parser.add_argument("datadir", help="directory to walk to find files")
    parser.add_argument("searchstring", help="string to match filenames")

    args = parser.parse_args()
    matches = []

    for root, dirnames, filenames in os.walk(args.datadir):
     for filename in fnmatch.filter(filenames, args.searchstring):
        matches.append(os.path.join(root, filename))

    for file in matches:
        sample = os.path.basename(os.path.dirname(file))
        out_file = os.path.join(args.output, sample + "_" + os.path.basename(file))
        print "Copying %s to %s." % (file,  out_file)
        shutil.copyfile(file, out_file)
