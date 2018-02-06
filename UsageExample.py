from MetaMapWrapper import *

wrapper = MetaMapWrapper()
text = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
           'and cardiovascular systems. '
output_list = wrapper.analyze_sentence([text])

running_index = 1
for concept_dict in output_list:
    print running_index
    for concept_key in concept_dict:
        print concept_key + ': ' + str(concept_dict[concept_key])
    running_index += 1
