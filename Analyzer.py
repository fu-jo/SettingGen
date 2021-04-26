from nltk.corpus import wordnet as wn
import nltk
from textstat.textstat import textstatistics
import textdistance


def distance(text1, text2):
    jaccardD = textdistance.jaccard.normalized_distance(text1, text2)
    cosineD = textdistance.cosine.normalized_distance(text1, text2)
    jaccardS = textdistance.jaccard.similarity(text1, text2)
    cosineS = textdistance.cosine.similarity(text1, text2)
    return [('Jaccard Distance', jaccardD), ('Cosine Distance', cosineD), ('Jaccard Similarity', jaccardS),
            ('Cosine Similarity', cosineS)]


def syllables_count(word):
    return textstatistics().syllable_count(word)


def text_complexity(text: str):
    scores = list()
    scores.append(textstatistics().flesch_kincaid_grade(text))
    scores.append(textstatistics().gunning_fog(text))
    scores.append(textstatistics().smog_index(text))
    return scores


def difficult_words(text: str):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens, tagset='universal')
    words = [word for (word, tag) in tagged if tag != '.']
    diff_words = set()
    porter = nltk.PorterStemmer()
    cmud = nltk.corpus.cmudict.dict()
    for word in words:
        stem = porter.stem(word)
        stem_freq = len([w for w in cmud.keys() if w.startswith(stem)])
        if syllables_count(word) > 2 and stem_freq < 10:
            diff_words.add(word)
    return diff_words


def replace_simple(word: str, tagged: list):
    sylls = 30
    simpler = ''
    synonyms = list()
    pos = [tag for (token, tag) in tagged if token == word][0]
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            tag = nltk.pos_tag([lemma.name()])[0][1]
            if tag == pos:
                synonyms.append(lemma.name())
    for syn in synonyms:
        if syllables_count(syn) < sylls:
            sylls = syllables_count(syn)
            simpler = syn
    return simpler


def replace_sent(sentence: str):
    difficult = difficult_words(sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    new_tokens = list()
    for token in tokens:
        if token in difficult:
            new_token = replace_simple(token, tagged)
            if new_token:
                new_tokens.append(new_token)
            else:
                new_tokens.append(token)
        else:
            new_tokens.append(token)
    return ' '.join(new_tokens)
