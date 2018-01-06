class Phrase:

    def __init__(self, original_name, preferred_name, concept_types):
        self.original_name = original_name
        self.preferred_name = preferred_name
        self.concept_types = concept_types

    def __str__(self):
        return 'Original name: ' + self.original_name + \
               ', Preferred name: ' + self.preferred_name + \
               ', Concept_types: ' + str(self.concept_types)
