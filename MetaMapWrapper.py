from pymetamap import MetaMap
import configparser


class MetaMapWrapper(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        meta_map_path = config.get('general', 'meta_map_path')
        self.meta_map = MetaMap.get_instance(meta_map_path)
        self.relevant_field_names = config.get('general', 'relevant_field_names').split(',')

    def extract_data_from_pos_info(self, sentence, pos_info):
        split_pos_info = pos_info.split(':')
        starting_index = int(split_pos_info[0]) - 1
        length = int(split_pos_info[1])
        return sentence[starting_index:starting_index+length], str(starting_index)


    def analyze_sentence(self, sentence):
        concepts, error = self.meta_map.extract_concepts([sentence], [1])
        output_dict = dict()

        current_index = 1
        for concept in concepts:
            concept_dict = dict()
            for field_name in self.relevant_field_names:
                concept_dict[field_name] = getattr(concept, field_name)
            original_name, starting_index = self.extract_data_from_pos_info(sentence, concept.pos_info)
            concept_dict['original_name'] = original_name
            concept_dict['starting_index'] = starting_index

            output_dict[current_index] = concept_dict
            current_index += 1

        return output_dict
