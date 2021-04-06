from Analyzer import *


class SettingGenerator:
    def __init__(self, text: str):
        self.text = text

    def find_sensory_pairs(self) -> list:
        tokens = nltk.word_tokenize(self.text)
        tokens_tagged = nltk.pos_tag(tokens, tagset='universal')
        sensory_pairs = list()
        for i in range(len(tokens_tagged)):
            if tokens_tagged[i][1] == 'ADJ' and tokens_tagged[i + 1][1] == 'NOUN':
                sensory_pairs.append(' '.join([tokens_tagged[j][0] for j in range(i, i + 2)]))
        return sensory_pairs


if __name__ == '__main__':
    my_text = open('setting.txt', 'r').read()
    sg = SettingGenerator(my_text)
    print(sg.find_sensory_pairs())
