import sys
from utils import *
import openai
import argparse

#openai.api_key = "open-api-key"

# Read the file containing the text
parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input_file", help="File containing the symptoms", required=True)
parser.add_argument('-a', "--additional_file", help="File containing any addiotional conditions obtained from medical history or vitals information", default="")
args = vars(parser.parse_args())
input_file = args["input_file"]
additional_file = args["additional_file"]


with open (input_file, 'r') as file:
    data  = file.read().rstrip()
print ("Symptoms:\n")
print(data)
# metamap_results = pp_concepts(data)
# print ("Conditions from Metmap:\n")
# for result in metamap_results:
#     print (result)

request = "Read the following text containing the symptoms I am experiencing delimited by backticks:\n```\n" + data + "\n```\n" 

if additional_file != "":
	with open(additional_file, 'r') as f:
		health_conditions = f.readlines()
	request = request + "\nThe following text delimited by hashes contains my health status:\n###\n" 
	for i in range(len(health_conditions)):
		request = request + str(i+1) + ". " + health_conditions[i].rstrip() + "\n"
	request = request + "###\n"

request = request +  "\nIn the form of an unnumbered list, tell me what diagnoses the symptoms could indicate " \
         "starting from the most likely to the least likely?  Also list  the percentage " \
         "of chance for each diagnosis. Do not provide explanation of the diagnoses."


print (request)

model = "gpt-3.5-turbo"


response = openai.ChatCompletion.create(
    model = model,
    temperature=0,
    messages = [
        {"role": "user", "content": request}
    ]
)
prelim_diagnosis = list()
prelim_diagnosis_perc = dict()
if response['choices'][0]['finish_reason'] == "stop":
    output = response['choices'][0]['message']['content']
    results_openai = output.split("\n")
    for result in results_openai:
        diag = result.split("(")[0]
        prelim_diagnosis.append(diag)
        if diag not in prelim_diagnosis_perc.keys():
            prelim_diagnosis_perc[diag]=result.split("(")[1].split(")")[0]

else:
    print ("unable to determine the diagnosis")

#print ("Conditions from OPENAI:")
print ("Diagnoses")

for diag in prelim_diagnosis:
    print (diag + ":" + prelim_diagnosis_perc[diag])

#print ("Combining the results from the different sources")

