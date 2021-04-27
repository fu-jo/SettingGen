import random

import nltk as nltk
from nltk.util import ngrams


class LanguageModel:
    def __init__(self, k: int, n: int, seed: int = 0):
        self.texts = []
        self.text = []
        self.seed = seed
        self.k = k
        self.n = n
        self.cfd = nltk.ConditionalFreqDist()

    def update(self):
        if self.n > 1:
            n_grams = tuple(ngrams(self.text, self.n))
        else:
            n_grams = tuple(self.text)
        if self.k > 1:
            k_grams = tuple(ngrams(self.text, self.k))
        else:
            k_grams = tuple(self.text)
        if self.n > self.k:
            n_grams = n_grams[1:]
        else:
            n_grams = n_grams[self.k:]
        for i in range(len(k_grams) - 1):
            self.cfd[tuple(k_grams[i])][n_grams[i]] += 1

    def add_text(self, text: str):
        self.texts.append(nltk.word_tokenize(text))

    def update_text(self, num_texts: list = [], use_all: bool = False):
        if use_all:
            self.text = []
            for text in self.texts:
                self.text += text
        else:
            for i in range(len(self.texts)):
                if i in num_texts:
                    self.text += self.texts[i]

    def sample(self, condition: tuple) -> tuple:
        if type(condition) is not tuple:
            condition = tuple(condition)
        if self.cfd.get(condition) is None:
            raise KeyError
        rands = [tup for tup in self.cfd[condition].keys()]
        waits = [tup for tup in self.cfd[condition].values()]
        return random.choices(rands, weights=waits, k=1)[0]

    def generate(self, starting_tokens: list, length: int, sep: str = ' ') -> str:
        gener = starting_tokens
        while len(gener) < length:
            if self.n != 1:
                gener += [self.sample(gener[-self.k:])]
            else:
                gener += [self.sample(gener[-self.k:])]
        ret = sep.join(gener)
        return ret
