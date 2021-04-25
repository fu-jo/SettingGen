import nltk
import Analyzer
import LanguageModel


class SettingGenerator:
    def __init__(self):
        self.text = []
        self.model = LanguageModel.LanguageModel(2,1)

    def add_text(self, text: str):
        self.text.append(text)
        self.model.add_text(text)

    def find_sensory_pairs(self, num_text) -> list:
        tokens = nltk.word_tokenize(self.text[num_text])
        tokens_tagged = nltk.pos_tag(tokens, tagset='universal')
        sensory_pairs = list()
        for i in range(len(tokens_tagged)):
            if tokens_tagged[i][1] == 'ADJ' and tokens_tagged[i + 1][1] == 'NOUN':
                sensory_pairs.append(' '.join([tokens_tagged[j][0] for j in range(i, i + 2)]))
        return sensory_pairs

    def add_sensory_pairs(self, sensory_pairs):
        for pair in sensory_pairs:
            self.model.add_text(pair)


if __name__ == '__main__':
    my_text = open('setting.txt', 'r').read()
    my_text2 = open('setting2.txt', 'r').read()
    sg = SettingGenerator()
    sg.add_text(my_text)
    sg.add_text(my_text2)

    sp = sg.find_sensory_pairs(0)
    sp += sg.find_sensory_pairs(1)

    # print(sp)

    sg.add_sensory_pairs(sp)
    sg.model.update_text(use_all=True)
    sg.model.update()
    print(sg.model.generate(nltk.word_tokenize(sp[0]),10))





    # sg.add_text(my_text)
    # print('Sensory Pairs: '+str(sg.find_sensory_pairs(0)))
    # complex = Analyzer.text_complexity(my_text)
    # print()
    # print('Flesch Kincaid: ' + str(complex[0]))
    # print('Gunning-Fog: ' + str(complex[1]))
    # print('SMOG: ' + str(complex[2]))
    # print(Analyzer.difficult_words(my_text))
    # print()
    # print(Analyzer.distance(my_text, my_text))
    # print(Analyzer.distance(my_text, my_text2))
    # print()
    # print(my_text2)
    # text4 = Analyzer.replace_sent(my_text2)
    # print(Analyzer.replace_sent(my_text2))
    # print(Analyzer.difficult_words(my_text2))
    # print(Analyzer.distance(my_text2, text4))
    # print()
    # text5 = Analyzer.replace_sent(my_text)
    # print(my_text)
    # print(Analyzer.replace_sent(my_text))
    # print(Analyzer.difficult_words(my_text))
    # print(Analyzer.distance(my_text, text5))