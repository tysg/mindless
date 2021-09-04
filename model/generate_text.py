import random
import re
import pickle
import sys
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))

class TextGenerator(object):

    def __init__(self):
        '''
            Initialize the text generator

            Parameters:
                n (int) : order of the n-gram model
                vocab (list) : vocabulary of the corpus
                word_count_dict : key=(context_n-1,...,context_1, word), value=count
                contexts_count_dict : key=(context_n-1,...,context_1), value=count
        '''
        self.n = 3
        self.vocab = list(pickle.load(open(os.path.join(absolute_path, 'vocab'), 'rb')))
        self.word_count_dict = pickle.load(open(os.path.join(absolute_path,'word_count'), 'rb'))
        self.contexts_count_dict = pickle.load(open(os.path.join(absolute_path, 'context_count'), 'rb'))
    

    def tokenize(self, text):
        return re.split(r'[^a-zA-Z\'’\-~]+', text)

    def get_next_word_probability(self, text, word, k):
        ''' 
        Returns the probability of word appearing after specified text 
        k (float) : smoothing hyperparameter
        '''
        
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
        return (count_word + k) / (count_context + k * len(self.vocab))

    def generate_word(self, text, k):
        '''
        Returns a random word based on the specified text and n-grams learned
        by the model
        '''
        weights = []
        for v in self.vocab:
            prob = self.get_next_word_probability(text, v, k)
            weights.append(prob)
            
        return random.choices(self.vocab, weights=weights, k=1)[0]

    def get_sentence_length(self, low, high):
        return random.randint(low, high)

    def capitalize_i(self, s):
        return s.replace(" i ", " I ").replace(" i'", " I'").replace(" i’", " I’")

    def get_ending_punctuation(self):
        ending_punctuations = [
            '.', '...', '!', '?', '?!', '!!', ' ~ ~', 
            '♡', '♥', '☆', '★', '☘', '♫', '♩', '☺', '☻',
            '☽', '⚠', '⚛', '♔'
        ]
        return random.choice(ending_punctuations)

    def continue_to_say_something(self, input_text):
        ''' Returns a phrase that follows the user input '''

        length = self.get_sentence_length(2,4)
        words_left = length
        answer = ""
        
        while words_left > 0:
            next_word = self.generate_word(input_text, 0.00004)
            if words_left == length and next_word == "~":
                continue

            if next_word == "~":
                break

            input_text += " " + next_word
            answer += next_word + " "
            words_left -= 1

        # formatting
        answer = self.capitalize_i(answer.strip())
        answer += self.get_ending_punctuation()

        return answer


    def say_something(self):
        ''' Returns a complete sentence based on the learned model '''

        # to achieve a natual ending sentence, the sentence should end when reaching a sentence separator ("~")
        # instead of being cut off by the word limit. so we retry building the sentence for max 3 times.
        for retry in range(3):        
            length = 10 # max length
            
            # generating the start of the sentence based on word count dictionary
            starting_of_sentence = [x for x in self.word_count_dict.items() if x[0][0]=="~"]
            words = [x[0] for x in starting_of_sentence]
            prob = [x[1] for x in starting_of_sentence]
            max_key = random.choices(words, weights=prob, k=1)[0]
            sentence = " ".join(max_key)
            words_left = length - (self.n-1)
            if sentence[-1] == "~":
                return sentence[2:-1].strip().capitalize()
        
            # generate the rest of the sentence
            for i in range(words_left, 0, -1):
                next_word= self.generate_word(sentence, 0.00001)
                if next_word == "~":
                    break
                sentence += " " + next_word
            if i != 0:
                print(retry)
                break
        
        # remove "~" at start
        if sentence[0] == "~":
            sentence = sentence[2:]


        # formatting
        sentence = self.capitalize_i(sentence.strip().capitalize())
        sentence += self.get_ending_punctuation()

        return sentence

# tg = TextGenerator()
# print(tg.continue_to_say_something("i want"))
# print(tg.say_something())