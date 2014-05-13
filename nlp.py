from nltk import pos_tag,word_tokenize,ne_chunk,collocations

pronouns = ["it","I","you","he","they","we","she","who","them","me","him","one","her","us","something","nothing","anything","himself","everything","someone","themselves","everyone","itself","anyone","myself"]

#https://gist.github.com/322906/90dea659c04570757cccf0ce1e6d26c9d06f9283
def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

def extract_named_entities(text):
    entity_names = []
    entities = ne_chunk(pos_tag(word_tokenize(text)), binary=True)
    for tree in entities:
        entity_names.extend(extract_entity_names(tree))
    return entity_names

def trigrams(text, exclude=pronouns, freq=3, limit=10):
    temp = []
    trigram_measures = collocations.TrigramAssocMeasures()
    finder = collocations.TrigramCollocationFinder.from_words(word_tokenize(text))
    finder.apply_word_filter(lambda w: w in exclude)
    finder.apply_freq_filter(freq)
    [temp.append(each) for each in finder.nbest(trigram_measures.pmi, limit)]
    return temp

def bigrams(text, exclude=pronouns, freq=3, limit=10):
    temp = []
    bigram_measures = collocations.BigramAssocMeasures()
    finder = collocations.BigramCollocationFinder.from_words(word_tokenize(text))
    finder.apply_word_filter(lambda w: w in exclude)
    finder.apply_freq_filter(freq)
    [temp.append(each) for each in finder.nbest(bigram_measures.pmi, limit)]
    return temp
