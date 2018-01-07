import MetaMapMock
from Phrase import Phrase
from pymetamap import MetaMap


def f(sentence):
    mm = MetaMap.get_instance('/home/jonathans/meta-map-project/public_mm/bin/metamap16')
    concepts, error = mm.extract_concepts([sentence], [1])
    output_dict = dict()

    current_index = 1
    for concept in concepts:
        concept_dict = dict()
        concept_dict['pos_info'] = concept.pos_info
        concept_dict['preferred_nane'] = concept.preferred_nane
        concept_dict['cui'] = concept.cui
        output_dict[current_index] = concept_dict
        current_index += 1


sentence = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
       'and cardiovascular systems. '
output_dict = f(sentence)
for key in output_dict:
    print key
    concept_dict = output_dict[key]
    for concept_key in concept_dict:
        print concept_key + ': ' + concept_dict[concept_key]
a = 1
