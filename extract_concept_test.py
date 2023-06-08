import sys
from utils import *
import openai
openai.api_key = "open-api-key"
# Read the file containing the text
if len(sys.argv) <  2:
    print ("Need an input filename containing the notes.")
    sys.exit()
input_file = sys.argv[1]
#input_file="sample3.txt"

with open (input_file, 'r') as file:
    data  = file.read().rstrip()
print ("Symptoms:\n")
print(data)
# metamap_results = pp_concepts(data)
# print ("Conditions from Metmap:\n")
# for result in metamap_results:
#     print (result)

prompt1 = "Read the following text containing the symptoms I am experiencing delimited by backticks:\n```"
prompt2 = "\n```\nIn the form of an unnumbered list, tell me what diagnoses the symptoms could indicate " \
         "starting from the most likely to the least likely?  Also list  the percentage " \
         "of chance for each diagnosis. Do not provide explanation of the diagnoses."

request = prompt1 + data + prompt2

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

print ("Conditions from OPENAI:")

for diag in prelim_diagnosis:
    print (diag + ":" + prelim_diagnosis_perc[diag])

#print ("Combining the results from the different sources")

