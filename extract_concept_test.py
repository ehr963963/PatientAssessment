import sys
from utils import *

# Read the file containing the text
if len(sys.argv) <  2:
    print ("Need an input filename containing the notes.")
    sys.exit()
input_file = sys.argv[1]
#input_file="sample.txt"

with open (input_file, 'r') as file:
    data  = file.read().rstrip()
print ("Symptoms:\n")
print(data)
results = pp_concepts(data)
print ("Concepts:\n")
for result in results:
    print (result)