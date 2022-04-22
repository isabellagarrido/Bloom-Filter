import csv
import sys
import mmh3
import math
from bitarray import bitarray

inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
outputFile = 'results.csv'
falsePositiveProbability = 0.0000001

# Array to be filled with all emails in first input file.
emailsList = []

#Array to be filled with results after checking the Bloom Filter.
resultsList = []

#Array to be filled with emails to be looked for in the Bloom Filter.
emailsCheckList = []

class BloomFilter:

    # Bloom Filter constructor
    def __init__(self, filterSize, hashCount):
        self.filterSize = filterSize
        self.hashCount = hashCount
        self.bitArray = bitarray(filterSize)
        # Start with an array full of 0s
        self.bitArray.setall(0)

    def addDataToFilter(self, data):
        for seeds in range(self.hashCount):
            # Make sure the index is within the size of the filter.
            index = mmh3.hash(data, seeds) % self.filterSize
            # Sets position to 1
            self.bitArray[index] = 1

    # Check if the string is most likely present in the filter.
    def present(self, data):
        for seeds in range(self.hashCount):
            index = mmh3.hash (data, seeds) % self.filterSize
            # If the bit is off, element is not in the DB
            if self.bitArray[index] == 0:
                return "Not in the DB"
        return "Probably in the DB"

# --------- Reading first input file ---------
# Reads input file and creates the bloom filter.
# Returns the bloom filter.
def read_input(input):
    with open(input, 'r') as i:
        lines = i.readlines()
        for line in lines[1:]: # Skip title
            emails = line.strip()  # Remove trailing newline characters
            emailsList.append(emails) # Adds all emails to a list.

    numberOfInputs = len(emailsList)

    # Formula to calulate the size of the bit array.
    bitArraySize = math.floor(- (numberOfInputs * math.log(falsePositiveProbability)) / (math.log(2) ** 2))

    #Formula to calculate the amount of hashes to use.
    numberOfHashes = math.floor((bitArraySize / numberOfInputs) * math.log(2))

    bf = BloomFilter(bitArraySize, numberOfHashes)
    for emailData in emailsList:
        bf.addDataToFilter(emailData)

    return bf

# --------- Checking the Bloom Filter ---------
def checkBloomFilter(input2, bf):
        with open(input2, 'r') as i:
            lines = i.readlines()
            for line in lines[1:]: # Skip title
                emails = line.strip()
                # Adds all emails from second csv file to a list.
                emailsCheckList.append(emails)
                # Adds results for each email from second csv file to a list.
                resultsList.append(bf.present(emails))


# --------- Generating the output file ---------
def write_output(output):
    with open(output, 'w', newline="") as file:
        header = ['email', 'result']
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        length = len(emailsCheckList)
        i = 0
        while length > 0:
            data = [emailsCheckList[i], resultsList[i]]
            csvwriter.writerow(data)
            length -= 1
            i += 1
def main():
    bf = read_input(inputFile1)
    checkBloomFilter(inputFile2, bf)
    write_output(outputFile)

if __name__ == '__main__':
    main()