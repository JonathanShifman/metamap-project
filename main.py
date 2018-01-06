import MetaMapMock
from Phrase import Phrase


def extract_content_types(content_types_str):
    content_types_str = content_types_str.strip('[').strip(']')
    return content_types_str.split(':')


def f(sentences):
    concepts = MetaMapMock.extract_concepts(sentences)

    dict_by_concept_id = {}
    dict_by_preferred_name = {}
    dict_by_concept_type = {}
    updated_sentences = []
    updated_sentence = ''
    sentence_index = 0
    string_pointer = 0
    concept_id = 0

    for concept in concepts:
        while int(concept.index) > sentence_index + 1:
            updated_sentence = finish_sentence(updated_sentence, string_pointer, sentence_index, sentences)
            updated_sentences.append(updated_sentence)
            updated_sentence = ''
            sentence_index += 1
            string_pointer = 0
        concept_id += 1
        sentence = sentences[sentence_index]
        pos_info = concept.pos_info.split(':')
        starting_index = int(pos_info[0])
        length = int(pos_info[1])
        original_name = sentence[starting_index-1:starting_index-1+length]
        updated_sentence += sentence[string_pointer:starting_index-1] + \
            '<' + str(concept_id) + '>' + original_name + '</' + str(concept_id) + '>'
        content_types_str = concept.semtypes
        content_types = extract_content_types(content_types_str)
        phrase = Phrase(original_name, concept.preferred_name, content_types)
        dict_by_concept_id[concept_id] = phrase
        if concept.preferred_name not in dict_by_preferred_name:
            dict_by_preferred_name[concept.preferred_name] = []
        dict_by_preferred_name[concept.preferred_name].append(phrase)
        for content_type in content_types:
            if content_type not in dict_by_concept_type:
                dict_by_concept_type[content_type] = []
            dict_by_concept_type[content_type].append(phrase)

        string_pointer = starting_index - 1 + length

    while sentence_index < len(sentences):
        updated_sentence = finish_sentence(updated_sentence, string_pointer, sentence_index, sentences)
        updated_sentences.append(updated_sentence)
        updated_sentence = ''
        sentence_index += 1
        string_pointer = 0

    return updated_sentences, dict_by_concept_id, dict_by_preferred_name, dict_by_concept_type


def finish_sentence(updated_sentence, string_pointer, sentence_index, sentences):
    sentence = sentences[sentence_index]
    return updated_sentence + sentence[string_pointer:len(sentence)]


text = 'Hypertension is a multifactorial disease involving the nervous, renal, ' \
       'and cardiovascular systems. Macrophages are the most abundant and ubiquitous ' \
       'immune cells, placing them in a unique position to serve as key mediators between these components.'
d = '. '
updated_sentences, dict_by_concept_id, dict_by_preferred_name, dict_by_concept_type = f([e+d for e in text.split(d) if e])

print 'Printing updated sentences'
print
for sentence in updated_sentences:
    print sentence
    print
print
print
print
print 'Printing dict by concept id'
print
for key in dict_by_concept_id:
    print 'Id: ' + str(key)
    print dict_by_concept_id[key]
    print
print
print
print
print 'Printing dict by preferred name'
print
for key in dict_by_preferred_name:
    print 'Preferred name: ' + key
    for phrase in dict_by_preferred_name[key]:
        print phrase
    print
print
print
print
print 'Printing dict by content type'
print
for key in dict_by_concept_type:
    print 'Content type: ' + key
    for phrase in dict_by_concept_type[key]:
        print phrase
    print
