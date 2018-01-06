from pymetamap import Concept


def extract_concepts(sents):
    concepts = []
    with open('concepts_mock.txt') as f:
        lines = f.readlines()
        for line in lines:
            concepts.append(Concept.ConceptMMI.from_mmi(line))
    return concepts
