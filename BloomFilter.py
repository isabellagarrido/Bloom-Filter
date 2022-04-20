# NAME: Isabella S. Garrido Blanco
# STUDENT ID: 802199609
# COURSE: CIIC 4025-100
# PROFESSOR: Wilfredo E. Lugo
# Project 2: Bloom Filter

import csv
import sys

inputFile1 = sys.argv[1]
#inputFile2 = sys.argv[2]
outputFile = 'results.csv'

# Array to be filled with all emails in first input file.
emailsList = []

# Input Info
# The program must take 2 csv files as command-line inputs.
# The first CSV will be used to create the Bloom Filter,
# the second will be used to validate against the Bloom Filter.
# The input comma-separated files will contain 1 column: Email.
# Based on the email key, your program will
# build the Bloom Filter based on file 1 inputs.
# Then it will need to check file 2 entries
# against the bloom filter and provide its assessment

# Output info
# Code must output a "Results.csv" file that will contain all e-mails on the
# second CSV with a new field "Result" that will contain the result of the
# Bloom Filter for that e-mail.  The Result must be one of
# 2 possible values: "Probably in the DB" or "Not in the DB"

# Requirements and Specifications
# Create Bloom Filter based on parameters.  Bloom Filter
#  must be an object since in the future the code must be
# able to generate multiple bloom filters with different parameters.


# Inputs: 2 csv files
# Both files contain emails
#File 1 is used to create the bloom filter

def read_input(input):
    with open(input, 'r') as i:
        lines = i.readlines()
        for line in lines[1:]: # Skip title
            emails = line.strip()  # Remove trailing newline characters
            emailsList.append(emails)


# --------- Generating the output file ---------
def write_output(output):
    with open(output, 'w', newline="") as file:
        header = ['email', 'result']
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
def main():
    read_input(inputFile1)
    # write_output(outputFile)


if __name__ == '__main__':
    main()