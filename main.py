import MetaMapMock
from Phrase import Phrase
from pymetamap import MetaMap


def f(sentence):
    mm = MetaMap.get_instance('/home/jonathans/meta-map-project/public_mm/bin/metamap16')
    concepts = mm.extract_concepts([sentence], [1])
    output_dict = {}

    for concept in concepts:
        print concept

'''
    for concept in concepts:
        concept_dict = dict()
        concept_dict['pos_info'] = concept.pos_info
        output_dict[concept.preferred_name] = concept_dict

    return output_dict
'''



sentence = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
       'and cardiovascular systems. '
output_dict = f(sentence)
a = 1
