# SettingGen
Fictional Setting Generator using nltk and WordNet
SettingGen consists of three files: SettingGenerator, LanguageModel, and Analyzer. 

# SettingGenerator

Setting Generator contains a LanguageModel object and a list of texts to sample from.

-add_text(text: str)
takes in a string to add to the list of texts.

-find_sensory_pairs(num_text)
finds the sensory pairs of the text specified by the index number of the text in the list of texts.

-add_sensory_pairs(self, sensory_pairs)
adds a list of sensory pairs to the LanguageModel

# Language Model
the SettingGenerator object contains a LanguageModel object.
It is initialized with a specified k and n for the n-gram generation based on previous k-grams, and an optional random seed.

-update()
Creates the conditional frequency distribution based on the currently added texts.

-add_text(text: str)
adds the text to the Language Model

-update_text(num_texts: list, use_all: bool=False)
specifies which texts to use for sampling. A list of the specific indexes of the desired texts are passed in. Alternatively, if the optional use_all bool is set to True, all of the texts will be used for sampling.

-sample(condition: tuple)
chooses the most probable n-gram based on the k-gram tuple passed in. If multiple n-grams have the same probability, a random n-gram will be selected from them.

-generate(starting_tokens: list, length: int, sep: str = ' ')
generates text using the "sample" method up to the specified number of tokens.

# Analyzer
Analyzes text distance and similarity using the textdistance library, as well as text complexity using the textstat library.

-distance
uses textdistance jaccard and cosine functions to return the text distances and similarites in a convenient list.

-text_complexity
uses textstat functions to return the Flesch-Kincaid, Gunning-Fog, and SMOG indexes of the text.

-difficult_words
uses the cmudict as well as syllable count to identify difficult words in the text

-replace_simple
replaces the word with a simpler word based on the cmudict

-replace_sent
replaces all of the difficult words in a given string using "replace_simple"


