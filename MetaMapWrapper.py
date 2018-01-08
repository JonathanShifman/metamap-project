from pymetamap import MetaMap
import configparser


class MetaMapWrapper(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        meta_map_path = config.get('general', 'meta_map_path')
        self.meta_map = MetaMap.get_instance(meta_map_path)
        self.relevant_field_names = config.get('general', 'relevant_field_names').split(',')

    def f(self, sentence):
        concepts, error = self.meta_map.extract_concepts([sentence], [1])
        output_dict = dict()

        current_index = 1
        for concept in concepts:
            concept_dict = dict()
            for field_name in self.relevant_field_names:
                concept_dict[field_name] = getattr(concept, field_name)
            output_dict[current_index] = concept_dict
            current_index += 1

        return output_dict



