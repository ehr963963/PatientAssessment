# Patient Assessment
Python library for patient assessment

### Concept extraction using UMLS Metathesaurus
Given a piece of text that the patient enters as the reason for the appointment, the concept extraction code identifies important concepts in the text. These concepts could be symptoms (positive and negative), drugs used, pre-existing conditions etc.

***Installation***


***Pre-requisites***: Install python and java and python packages 
```
sudo apt install default-jre python python3-pip
pip install setuptools numpy scipy openai 
```


Download and install  `MetaMap` in the `public_mm` directory. Download is available at https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/run-locally/MainDownload.html and instructions for installation are at https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/documentation/Installation.html

Download and setup `pymetamap`, a Python wrapper around MetaMap. Details here: https://github.com/AnthonyMRios/pymetamap

***Usage***
Set the value of `MetaMapPath` appropriately in `utils.py`
Run the concept extraction tool using 
```
python extract_concept_test.py  -i <text_file> [-a <health_info_file] 
```

Example usage:
```
python extract_concept_test.py -i sample.txt

python extract_concept_test.py -i sample.txt -a conditions.txt 

```
Sample results are in the file `results.txt` 
