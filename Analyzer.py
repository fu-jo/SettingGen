from nltk.corpus import wordnet as wn
import nltk
import textstat
from textstat.textstat import textstatistics, legacy_round
easy_word_set = textstatistics.get_lang_easy_words()

def syllables_count(word):
    return textstatistics().syllable_count(word)

def text_complexity(text: str):
    scores = []
    scores.append(textstat.flesch_kincaid_grade(text))
    scores.append(textstat.gunning_fog(text))
    scores.append(textstat.smog_index(text))
    return scores


def difficult_words(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens, tagset='universal')
    words = [word for (word, tag) in tagged if tag != '.']

    diff_words_set = set()

    for word in words:
        syllable_count = syllables_count(word)
        if word not in easy_word_set and syllable_count >= 2:
            diff_words_set.add(word)

    return len(diff_words_set)

def replace_simple(word: str):
    sylls = 30
    simpler = ''
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name)
    for syn in synonyms:
        if syllables_count(word) < sylls:
            sylls = syllables_count(word)
            simpler = word
    return word

def replace_sent(sentence: str):
    difficult = difficult_words(sentence)
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        if token in difficult:
            token = replace_simple(token)
    return tokens
