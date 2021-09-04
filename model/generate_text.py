'''
    NUS CS4248 Assignment 1 - Objective 3 (n-gram Language Model)

    Class NgramLM for handling Objective 3
'''
import random, math
import re
import pickle
import sys

class TextGenerator(object):

    def __init__(self, n, k):
        '''
            Initialize your n-gram LM class

            Parameters:
                n (int) : order of the n-gram model
                k (float) : smoothing hyperparameter

        '''
        # Initialise other variables as necessary
        self.n = n
        self.k = k
        self.vocab = list(pickle.load(open('vocab', 'rb')))
        
        '''
        1. word_count_dict: key=(context_n-1,...,context_1, word), value=count
        2. contexts_count_dict: key=(context_n-1,...,context_1), value=count
        '''
        self.word_count_dict = pickle.load(open('word_count', 'rb'))
        self.contexts_count_dict = pickle.load(open('context_count', 'rb'))
    
    def tokenize(self, text):
        for c in re.findall("([A-Z]+)", text):
            text = text.replace(c, c.lower())
        # split by non-alphabet, except ' - and ~
        tokens = re.split(r'[^a-zA-Z\'\-~]+', text)      
        return [x for x in tokens if x != ""]

    def get_next_word_probability(self, text, word):
        ''' Returns the probability of word appearing after specified text '''
        
        text = "~ " + text

        if self.n == 1:
            tokens = []
        else:
            tokens = self.tokenize(text)[-(self.n-1):]
        
        context = tuple(tokens)
        tokens.append(word)
        item = tuple(tokens)

        # check zero values
        if item in self.word_count_dict:
            count_word = self.word_count_dict[item]
        else:
            count_word = 0
        
        if context in self.contexts_count_dict:
            count_context = self.contexts_count_dict[context]
        else:
            count_context = 0
        
        # apply add-k smoothing
        return (count_word + self.k) / (count_context + self.k * len(self.vocab))

    def generate_word(self, text):
        '''
        Returns a random word based on the specified text and n-grams learned
        by the model
        '''
        weights = []
        for v in self.vocab:
            prob = self.get_next_word_probability(text, v)
            weights.append(prob)
            
        return random.choices(self.vocab, weights=weights, k=1)[0]

    def generate_text(self, length):
        ''' Returns text of the specified length based on the learned model '''        
        # get start of the sentence 
        if self.n == 1:
            sentence = self.generate_word("")
            words_left = length - 1
        else: 
            starting_of_sentence = [x for x in self.word_count_dict.items() if x[0][0]=="~"]
            words = [x[0] for x in starting_of_sentence]
            prob = [x[1] for x in starting_of_sentence]
            max_key = random.choices(words, weights=prob, k=1)[0]
            sentence = ""
            for i in range(0, len(max_key)):
                sentence += max_key[i]
                if i != (len(max_key) - 1):
                    sentence += " "
            words_left = length - (self.n-1)
        
        # check if the start of the sentence generated exceeds the length
        if words_left <= 0:
            if sentence[0] == "~":
                sentence = sentence[2:]
            return sentence
        
        # generate the rest of the sentence
        for i in range(words_left):
            next_word= self.generate_word(sentence)
            sentence += " "
            sentence += next_word
        
        if sentence[0] == "~":
            sentence = sentence[2:]
        return sentence

tg = TextGenerator(3, 0.00001)
print(tg.generate_text(int(sys.argv[1])))