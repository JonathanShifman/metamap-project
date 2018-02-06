from pymetamap import MetaMap
import configparser


class MetaMapWrapper(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        # Read path to the MetaMap binary release from configuration
        meta_map_path = config.get('general', 'meta_map_path')
        self.meta_map = MetaMap.get_instance(meta_map_path)

        # Get relevant field names, i.e. score, cui, preferred_name...
        self.relevant_field_names = config.get('general', 'relevant_field_names').split(',')

    '''
        :param str sentence: The sentence that is being analyzed
        :param str pos_info: Concept pos_info value as returned from MetaMap
        :return: The original concept and mappings to the original indices in the sentence (could be
            more than one if the concept is made of multiple non consecutive parts).
    '''
    def extract_data_from_pos_infos(self, sentence, pos_infos):
        pos_info_list = pos_infos.split(',')
        original_name_components = []
        mappings = []
        for pos_info in pos_info_list:
            split_pos_info = pos_info.split('/')
            starting_index = int(split_pos_info[0]) - 1
            length = int(split_pos_info[1])
            mappings.append([starting_index, length])
            component = sentence[starting_index:starting_index+length]
            original_name_components.append(component)
        return " ".join(original_name_components), mappings

    '''
        :param str sentence: The sentence to analyze
        :return: A list of concept dictionaries
    '''
    def analyze_texts(self, texts):
        concepts, error = self.meta_map.extract_concepts(texts, [1])
        output_list = []

        for concept in concepts:
            concept_dict = dict()

            # Store relevant field values in concept dict
            for field_name in self.relevant_field_names:
                concept_dict[field_name] = getattr(concept, field_name)

            # Store original name, starting index and sentence_index in concept dict
            concept_dict['text_index'] = int(concept.index) - 1
            original_name, mappings = self.extract_data_from_pos_infos(texts[concept_dict['text_index']], concept.pos_info)
            concept_dict['original_name'] = original_name
            concept_dict['mappings'] = mappings

            output_list.append(concept_dict)

        return output_list

    '''
        :param str sentences: A list of sentences to analyze
        :return: A list of concept dictionaries. Each dictionary specifies the appropriate sentence index.
    '''
    def analyze_sentences(self, sentences):
        output_list = []
        current_sentence_index = 0
        for sentence in sentences:
            sentence_output_list = self.analyze_sentence(sentence, current_sentence_index)
            output_list.extend(sentence_output_list)
        return output_list
