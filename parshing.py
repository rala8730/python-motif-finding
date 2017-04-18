
import sys, getopt, math, os.path, string, collections
import numpy

def readInput(inFile):
    File = open(inFile, 'r')
    sequences = []
    output = []
    for line in File:
        if not line.startswith('>'):
             output.append(line.rstrip())
    return output


def usage():
    # print the usage of the application
    print 'python main.py -F <filename> -K <kmer>'


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "H:F:K:S:")
    except getopt.GetoptError:
        print "ERROR! An input file (-F) and a length of a kmer (-K) must be specified. Correct usage:"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        # process each input parameter
        if opt == '-H':
            print "Correct usage is:"
            usage()
            sys.exit()
        if opt == '-F':
            if os.path.isfile(arg):
                inputFile = arg
            # If the input file given does not exist, print an error message and exit the program
            else:
                print "ERROR! Input file must exist. Correct usage:"
                usage()
                sys.exit(2)
        if opt == '-K':
            kmerlen = int(arg)


    # store the array
    sequences= readInput(inputFile)
    if len(sequences) is not None:
        search_sq=search_seq(sequences)
    else:
        print "ERROR: length of sequence is None"


#this gives 1st sequence of the sequence and i made this to practice making kmer and kmer count function
def search_seq(sequences):

    for lines in sequences:
        print lines



if __name__ == '__main__':
    main(sys.argv[1:])

