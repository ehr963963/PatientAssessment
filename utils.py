def extract_concepts(data):
    from pymetamap import MetaMap
    MetaMapPath = '/Users/radhachitta/pehr/PatientAssessment/public_mm/bin/metamap'
    mm = MetaMap.get_instance(MetaMapPath)
    data = data.encode("ascii","ignore").decode()
    concepts,error = mm.extract_concepts([data],ids=None,
        restrict_to_sts = ['sosy','fndg','acty','bhvr','biof','bpoc','clna',
        'clnd','cnce','diap','dora','drdd','dsyn','food','hlca','inbe','inpo','lbpr','lbtr','mobd',
        'virs','vita'])

    return concepts

def process_concept(concept):
    if concept.__class__.__name__ == 'ConceptMMI':
            preferred_name = concept.preferred_name
            return(preferred_name.split('(')[0].rstrip() + " (" + preferred_name + "->" +  concept.cui + "->" + concept.semtypes + ")")
    if concept.__class__.__name__ == 'ConceptAA':
            return(concept.long_form + " (" + concept.short_form + ")")

def pp_concepts(data):
    concepts = extract_concepts(data)
    results = []
    for concept in concepts:
        results.append(process_concept(concept) + "\n")
    return results
