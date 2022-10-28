# Patient Assessment
Python library for patient assessment

### Concept extraction using UMLS Metathesaurus
Given a piece of text that the patient enters as the reason for the appointment, the concept extraction code identifies important concepts in the text. These concepts could be symptoms (positive and negative), drugs used, pre-existing conditions etc.

***Installation***
Download and install  `MetaMap` in the `public_mm` directory. Download is available at https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/run-locally/MainDownload.html and instructions for installation are at https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/documentation/Installation.html

Download and setup `pymetamap`, a Python wrapper around MetaMap. Details here: https://github.com/AnthonyMRios/pymetamap

***Usage***
Set the value of `MetaMapPath` appropriately in `utils.py`
Run the concept extraction tool using
```
python extract_concept_test.py  <text_file>
```

Example usage and output:
```
python extract_concept_test.py sample.txt

Symptoms:

I have been feeling really tired lately.
Sometimes I find myself crying in my car for no reason.
There is nothing really going on I’m my life right now - and I and upset for no reason.
I just have no energy.

Concepts:

Crying (Crying->C0010399->[inbe])

Finding (Finding->C0243095->[fndg])

Tired (Tired->C0557875->[sosy])

Vitality (Vitality->C0424589->[fndg])

NI+ (NI+->C3869926->[fndg])

NI- (NI-->C3869927->[fndg])
```
