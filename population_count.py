import csv
import time
import glob


start_time = time.time()
# popcount takes a glob of files, iterates through them, and sums PWGTP fields
def popcount(files, count):
	for csvfile in files:
		reader = csv.DictReader(open(csvfile))
		for row in reader:
			count += int(row['PWGTP'])
	return count

files = glob.glob('full_us/*.csv')
population = 0
print(popcount(files, population))
print(time.time() - start_time)