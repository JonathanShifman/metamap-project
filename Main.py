from MetaMapWrapper import *

sentence = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
           'and cardiovascular systems. '
wrapper = MetaMapWrapper('/home/jonathans/meta-map-project/public_mm/bin/metamap16')

output_dict = wrapper.f(sentence)
for key in output_dict:
    print key
    concept_dict = output_dict[key]
    for concept_key in concept_dict:
        print concept_key + ': ' + concept_dict[concept_key]
a = 1