# python-motif-finding

__Benchmarking Progress__

_How to Run BioProspector_

- Using a Linux machine, in the directory that contains the BioProspector files, run the command mv BioProspector.linux BioProspector
- You can generate the random datasets using the updated version of the Generated_Data.py (Rasmi edited Monte's to place it in FASTA format). Ex. python Generated_Data.py > small_seq_1.fasta (where it can be named anything and it will be used as the input into BioProspector)
- To run BioProspector and generate the results use this command: ./BioProspector -i small_seq_1.fasta -W 10 -o benchmark1
- -i is a flag that specifies the FASTA file name
- -W is a flag that specifies the length of the motif
- -o is a flag that specifies the output file name that it will write the results to
- _Note:_ There are more flags, and you don't have to include -o for instance. There are defaults too. Read the BioProspector README.md for examples and explanations.

So far, I have run a small input file (around 73 sequences), which is located in the Benchmark_Small folder, and I am currently running a big input file (over 5000 sequences and counting), which is located in the Benchmark_Medium folder. Each of the sequences are 160 nucleotides total, and are finding motif lengths of 10, 15, 18, 20, 25, 30, 40 or 45, and 50 (so about 10 benchmark result files each). 

_TO DO:_
- Need to compare the actual positions a motif was found through BioProspector with the positions that we identified in the sequences beforehand. (Note: Monte has code that prints out the locations, so we can just run the new FASTA file on there).
- Need to categorize into the following: positives, negatives, false positives, false negatives, etc. 
- Need to write the Word Document for Benchmarking containing our findings, and how accurate the application is.
