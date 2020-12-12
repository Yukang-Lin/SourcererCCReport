# Compare two files to determine if there is overlap between them.
# Outputs the matches between the files as well as the non-matches.

# import the necessary packages
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--file1", required=True, help="File to match")
ap.add_argument("-b", "--file2", required=True, help="File to be matched on")
ap.add_argument("-x", "--match", required=True, help="Output filename for "
                                                       "matches")
ap.add_argument("-y", "--nomatch", required=True, help="Output filename "
                                                          "for non matches")
args = vars(ap.parse_args())

# open input files to read line by line
file1 = open(args["file1"], 'rt')
file2 = open(args["file2"], 'rt')

with file1:
    with file2:
        set1 = set(file1)
        set2 = set(file2)
        same = set2.intersection(set1)
        different = set2.difference(set1)

match = open(args["match"], 'wt')
matches = []
nomatch = open(args["nomatch"], 'wt')
nomatches = []
matchcount = 0
for line in same:
    matchcount+=1
    matches.append(line)
nomatchcount = 0
for line in different:
    nomatchcount+=1
    nomatches.append(line)

matches.sort()
nomatches.sort()
for line in matches:
    match.write(line)

for line in nomatches:
    nomatch.write(line)

print("FOUND " + str(matchcount) + " MATCHES AND " + str(nomatchcount) + " NON "
                                                                        "MATCHES")
