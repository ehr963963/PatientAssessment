def extract_concepts(data):
    from pymetamap import MetaMap
    MetaMapPath = '/Users/radhachitta/pehr/PatientAssessment/public_mm/bin/metamap16'
    mm = MetaMap.get_instance(MetaMapPath)
    data = data.encode("ascii","ignore").decode()
    concepts,error = mm.extract_concepts([data],[1,2],
        restrict_to_sts = ['sosy','fndg','acty','bhvr','biof','bpoc','clna',
        'clnd','cnce','diap','dora','drdd','dsyn','food','hlca','inbe','inpo','lbpr','lbtr','mobd',
        'virs','vita'])

    return concepts

def pp_concepts(data):
    concepts = extract_concepts(data)
    results = []
    for concept in concepts:
        results.append(concept.preferred_name.split('(')[0].rstrip() + " (" + concept.preferred_name + "->" +  concept.cui + "->" + concept.semtypes + ")\n")
    return results
