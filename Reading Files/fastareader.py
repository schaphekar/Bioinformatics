#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Siddharth Chaphekar
# Created Date: 08/01/2023
# version ='1.0'
# ---------------------------------------------------------------------------

"""
PROBLEM STATEMENT: Create a FastaFile class that takes in filename as an argument.
It should then read the file and create a variable to holds the contents.

# File format: Each record starts with a header that looks like this:
# >DQ889687|exclusivity

# The accession is the first field (starts after the '>' character and ends before the '|').
# The sequence consists of all lines before the next record begins, and it should not have new line characters.

"""

import re
import sys
import typing

def main():
	sequence_file = FastaFile(sys.argv[1])

	sequences = FastaFile.read_fasta_file(sequence_file)

	print(sequences)
	print(len(sequences))

class FastaFile:
	def __init__(self, input_loc: str):
		"""Create a new fasta input file record.

		Args:
		input_loc: String path to the input file.
		"""
		self._input_loc = input_loc

	def get_input_loc(self) -> str:
		return self._input_loc

	def read_fasta_file(self):

		loc = self.get_input_loc()

		with open(loc, "r") as f:
			
			data = f.readlines()
			ids = []
			seqs = []

			cleaned_data = []

			# Remove all newline characters
			for line in data:
				cleaned_data.append(line.strip("\n"))

			# Initialize a string to append to the list of sequences
			sequence = ""

			for line in cleaned_data:

				# If line starts with ">" char, it is an ID
				if line[0] == ">":

					if len(ids) > len(seqs):
						seqs.append(sequence)
						sequence = ""

					# Parse out the accession ID without the extraneous characters
					bar_index = line.index("|")
					seq_id = line[1:bar_index]
					
					if seq_id not in ids:
						ids.append(seq_id)

				# Keep appending the next chunk of sequence
				else:
					sequence += line

			# Append the last sequence in the file
			seqs.append(sequence)
			sequence = ""

		# Construct a dictionary by pairing each id with the sequence
		sequences = dict(zip(ids, seqs))

		return sequences


if __name__ == '__main__':
	main()
