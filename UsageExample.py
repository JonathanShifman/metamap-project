from MetaMapWrapper import *

wrapper = MetaMapWrapper()

sentence = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
           'and cardiovascular systems. '

output_dict = wrapper.analyze_sentence(sentence)
for key in output_dict:
    print key
    concept_dict = output_dict[key]
    for concept_key in concept_dict:
        print concept_key + ': ' + concept_dict[concept_key]