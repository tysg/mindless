import re
import pickle
import sys

class NgramLM(object):

    def __init__(self, n, k):
        '''
            Initialize the n-gram LM class

            Parameters:
                n (int) : order of the n-gram model
                k (float) : smoothing hyperparameter
                corpus (string) : text corpus used
                tokens (list) : results of tokenization
                word_count_dict : key=(context_n-1,...,context_1, word), value=count
                contexts_count_dict : key=(context_n-1,...,context_1), value=count
        '''
        self.n = n
        self.k = k
        self.corpus = ""
        self.tokens = []

        self.word_count_dict = {}
        self.contexts_count_dict = {}


    def update_corpus(self, text):
        ''' Updates the n-grams corpus based on text '''
        
        self.tokens = self.tokenize(text)
        
        # get a list of ngrams and a list of contexts
        ngrams, contexts = self.ngrams()

        # update the counts in word_count_dict and contexts_count_dict
        for item in ngrams:
            if item in self.word_count_dict:
                self.word_count_dict[item] += 1
            else:
                self.word_count_dict[item] = 1
        for item in contexts:
            if item in self.contexts_count_dict:
                self.contexts_count_dict[item] += 1
            else:
                self.contexts_count_dict[item] = 1


    def read_file(self, path):
        ''' Read the file and update the corpus  '''
        with open(path, encoding='utf-8', errors='ignore') as f:
            self.corpus = f.read()
        self.corpus = self.add_padding()
        self.update_corpus(self.corpus)


    def ngrams(self):
        ''' 
        Returns 2 dictionaries
        1. ngrams of the text as list of tuples - [(context_n-1,...,context_1,word)] 
        2. all the contexts as list of tuples - [(context_n-1,...,context_1)]
        '''
        ngrams = []
        contexts = []
        for i in range(self.n-1,len(self.tokens)):
            word = self.tokens[i]
            
            context = []
            for j in range(1, self.n):
                context.append(self.tokens[i-(self.n-j)])

            # only allow ~ to be the first word in the sequence
            if ("~" not in context) or ((context.count("~") == 1) and (context[0] == "~")) :
                contexts.append(tuple(context))
                context.append(word)
                ngrams.append(tuple(context))
        return ngrams, contexts
        

    def add_padding(self):
        '''  Returns padded text '''
        # Use '~' as the padding symbol
        self.corpus = "~ " + self.corpus
        return re.sub(r'((?<!Mr|Dr|Ms)(?<!Mrs)\.|\?|!|;|,)+', r' ~ ', self.corpus)


    def tokenize(self, text):
        for c in re.findall("([A-Z]+)", text):
            text = text.replace(c, c.lower())
        # split by non-alphabet, except ' - and ~
        tokens = re.split(r'[^a-zA-Z\'’\-~]+', text)      
        return [x for x in tokens if x != ""]


    def get_vocabulary(self):
        ''' Returns the vocabulary as set of words '''        
        return set(self.tokens)
    
    def wrtie_to_file(self, word_count_path, context_count_path, vocab_path):
        pickle.dump(self.word_count_dict, open(word_count_path, 'wb'))
        pickle.dump(self.contexts_count_dict, open(context_count_path, 'wb'))
        pickle.dump(self.get_vocabulary(), open(vocab_path, 'wb'))

ng = NgramLM(3, 0.00001)
print(sys.argv[1])
ng.read_file(sys.argv[1])
ng.wrtie_to_file("word_count", "context_count", "vocab")