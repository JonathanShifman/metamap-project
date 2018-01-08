from pymetamap import MetaMap


class MetaMapWrapper(object):

    def __init__(self, meta_map_path):
        self.meta_map = MetaMap.get_instance(meta_map_path)

    def f(self, sentence):
        concepts, error = self.meta_map.extract_concepts([sentence], [1])
        output_dict = dict()

        current_index = 1
        for concept in concepts:
            concept_dict = dict()
            concept_dict['pos_info'] = concept.pos_info
            concept_dict['preferred_name'] = concept.preferred_name
            concept_dict['cui'] = concept.cui
            output_dict[current_index] = concept_dict
            current_index += 1

        return output_dict



