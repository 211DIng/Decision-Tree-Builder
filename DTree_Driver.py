from D_Tree import *
import sys
import csv

# Use processed version of dataset - golf_processed.csv, car_processed.csv

def main():

	if (len(sys.argv) < 3):
		print("\nError - Not enough arguments supplied")
		print("\nUsage: > DTree_Driver.py <input_processed_csv_file> <output_txt_file>")
		print("\nExample: > DTree_Driver.py golf_processed.csv golf_output.txt")
		sys.exit()
	
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	records = []
	
	with open(input_file, 'r') as f:
		f = csv.reader(f, delimiter = ',')
		for line in f:
			r = [int(i) for i in line]
			records.append(r)
			
	n_records = len(records)
	n_attributes = len(records[0]) - 1
	print("\n")
	print("------Input Configuration------")
	print("\nNumber of records: ", n_records)
	print("\nNumber of attributes: ", n_attributes)
	print("\nCheck output in ", output_file)
	print("\n")
	print("-------------------------------\n")
	att = [0 for i in range(n_attributes)]
	tree = build_tree(records, att)
	outfile = open(output_file, 'w')
	print(tree, file = outfile, flush = True)
	outfile.close()
	


if __name__ == '__main__':
	main()


