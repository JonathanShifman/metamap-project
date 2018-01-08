from MetaMapWrapper import *
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
meta_map_path = config.get('general', 'meta_map_path')
wrapper = MetaMapWrapper(meta_map_path)


sentence = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
           'and cardiovascular systems. '

output_dict = wrapper.f(sentence)
for key in output_dict:
    print key
    concept_dict = output_dict[key]
    for concept_key in concept_dict:
        print concept_key + ': ' + concept_dict[concept_key]