from nltk.corpus import wordnet as wn
import nltk
from textstat.textstat import textstatistics


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

    diff_words_set = set()

    for word in words:
        syllable_count = syllables_count(word)
        if syllable_count > 2:
            diff_words_set.add(word)

    return diff_words_set


def replace_simple(word: str):
    sylls = 3
    simpler = ''
    synonyms = list()
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    for syn in synonyms:
        if syllables_count(syn) < sylls:
            simpler = syn
    return simpler


def replace_sent(sentence: str):
    difficult = difficult_words(sentence)
    tokens = nltk.word_tokenize(sentence)
    new_tokens = list()
    for token in tokens:
        if token in difficult:
            new_token = replace_simple(token)
            if new_token:
                new_tokens.append(new_token)
            else:
                new_tokens.append(token)
        else:
            new_tokens.append(token)
    return ' '.join(new_tokens)
