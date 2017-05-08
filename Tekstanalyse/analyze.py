import paths
from reader import Reader

from os import listdir
from os.path import isfile, join
from collections import defaultdict
from sys import stdout


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Tekstanalyse"


class TrainerAnalyze:

    def __init__(self, p=0.01175, n=1):             # Init with optimal prune value and no grams as default

        self.number_of_reviews = None               # Total number of analyzed reviews
        self.total_pos_words = 0                    # Total positive words or n-grams
        self.total_neg_words = 0                    # Total negative words or n-grams
        self.directory = ''                         # Directory (alle or subset)

        self.pos_freq = defaultdict(int)            # Frequency of words or n-grams
        self.neg_freq = defaultdict(int)            # Frequency of words or n-grams

        self.most_common_pos = []                   # 25 most common words or n-grams
        self.most_common_neg = []                   # 25 most common words or n-grams

        self.pos_popularity = {}                    # Popularity values
        self.neg_popularity = {}                    # Popularity values
        self.pos_highest_pop = []
        self.neg_highest_pop = []

        self.pos_information_value = {}             # Informational values
        self.neg_information_value = {}             # Informational values
        self.pos_highest_inform_val = []            # 25 highest informational value
        self.neg_highest_inform_val = []            # 25 highest informational value

        self.pos_all_words_raw = []                 # Made in find_frequency (all docs as lists)
        self.neg_all_words_raw = []                 # Made in find_frequency (all docs as lists)

        self.pos_doc_count = defaultdict(int)       # Made in prune (in how many docs does the word appear).
        self.neg_doc_count = defaultdict(int)       # Made in prune (in how many docs does the word appear).

        self.set_directory()                        # Prompt
        r = Reader()

        if n > 1:
            self.pos_all_n_grams_raw = []
            self.neg_all_n_grams_raw = []

            self.make_n_grams_and_find_frequency(r, n)
            self.prune(p, self.pos_all_n_grams_raw, self.neg_all_n_grams_raw)
        else:
            self.find_frequency(r)
            self.prune(p, self.pos_all_words_raw, self.neg_all_words_raw)

        self.find_most_common()
        self.find_popularity()
        self.find_highest_pop_value()
        self.find_information_value()
        self.find_highest_informational_value()

    # Used
    def find_frequency(self, reader):

        pos_path = self.directory + 'pos'
        neg_path = self.directory + 'neg'
        pos_word_directs = self.list_files_in_directory(pos_path)
        neg_word_directs = self.list_files_in_directory(neg_path)
        self.number_of_reviews = len(pos_word_directs) + len(neg_word_directs)

        print('-' * 40)
        analyzed = 0
        prev_progress = 1
        for path in pos_word_directs:
            dir_path = self.directory + 'pos/' + path
            pos_word_list = Reader.default_read_from_file(reader, dir_path)
            self.pos_all_words_raw.append(pos_word_list)
            for word in pos_word_list:
                self.pos_freq[word] += 1
                self.total_pos_words += 1
            analyzed += 1
            progress = str(int(analyzed / self.number_of_reviews * 100))
            if progress != prev_progress:
                s = 'Training progress:\t\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        for path in neg_word_directs:
            dir_path = self.directory + 'neg/' + path
            neg_word_list = Reader.default_read_from_file(reader, dir_path)
            self.neg_all_words_raw.append(neg_word_list)
            for word in neg_word_list:
                self.neg_freq[word] += 1
                self.total_neg_words += 1
            analyzed += 1
            progress = str(int(analyzed / self.number_of_reviews * 100))
            if progress != prev_progress:
                s = 'Training progress:\t\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

    def make_n_grams_and_find_frequency(self, reader, n):
        pos_path = self.directory + 'pos'
        neg_path = self.directory + 'neg'
        pos_word_directs = self.list_files_in_directory(pos_path)
        neg_word_directs = self.list_files_in_directory(neg_path)
        self.number_of_reviews = len(pos_word_directs) + len(neg_word_directs)

        print('-' * 40)
        analyzed = 0
        prev_progress = 0
        for path in pos_word_directs:
            dir_path = self.directory + 'pos/' + path
            pos_word_list = reader.default_read_from_file(dir_path)
            self.pos_all_words_raw.append(pos_word_list)
            analyzed += 1
            total_loops = int(self.number_of_reviews + len(self.pos_all_words_raw) + len(self.neg_all_words_raw))
            progress = str(int(analyzed / total_loops * 100))
            if progress != prev_progress:
                s = 'Analyzing progress\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        for path in neg_word_directs:
            dir_path = self.directory + 'neg/' + path
            self.neg_all_words_raw.append(reader.default_read_from_file(dir_path))
            analyzed += 1
            total_loops = int(self.number_of_reviews + len(self.pos_all_words_raw) + len(self.neg_all_words_raw))
            progress = str(int(analyzed / total_loops * 100))
            if progress != prev_progress:
                s = 'Analyzing progress\t\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        pos_freq = defaultdict(int)
        neg_freq = defaultdict(int)

        for doc in self.pos_all_words_raw:
            l = []
            for i in range(1 + len(doc) - n):
                n_gram = '_'.join(doc[i:i+n])
                pos_freq[n_gram] += 1
                l.append(n_gram)
            self.pos_all_n_grams_raw.append(l)
            analyzed += 1
            total_loops = int(self.number_of_reviews + len(self.pos_all_words_raw) + len(self.neg_all_words_raw))
            progress = str(int(analyzed / total_loops * 100))
            if progress != prev_progress:
                s = 'Analyzing progress ' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        for doc in self.neg_all_words_raw:
            l = []
            for i in range(1 + len(doc) - n):
                n_gram = '_'.join(doc[i:i+n])
                neg_freq[n_gram] += 1
                l.append(n_gram)
            self.neg_all_n_grams_raw.append(l)
            analyzed += 1
            total_loops = int(self.number_of_reviews + len(self.pos_all_words_raw) + len(self.neg_all_words_raw))
            progress = str(int(analyzed / total_loops * 100))
            if progress != prev_progress:
                s = 'Analyzing progress ' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        self.pos_freq = pos_freq
        self.neg_freq = neg_freq

    def prune(self, decimal, pos_raw, neg_raw):
        for doc in pos_raw:
            l = list(set(doc))
            for w in l:
                if w in self.pos_freq:
                    self.pos_doc_count[w] += 1

        new_pos_percent = defaultdict(int)
        for w in self.pos_doc_count:
            p = round(self.pos_doc_count[w] / len(self.pos_all_words_raw), 7)
            if p > decimal:
                new_pos_percent[w] = self.pos_doc_count[w]
        self.pos_doc_count = new_pos_percent

        for doc in neg_raw:
            l = list(set(doc))
            for w in l:
                if w in self.pos_freq:
                    self.neg_doc_count[w] += 1

        new_neg_percent = defaultdict(int)
        for w in self.neg_doc_count:
            p = round(self.neg_doc_count[w] / len(self.neg_all_words_raw), 7)
            if p > decimal:
                new_neg_percent[w] = self.neg_doc_count[w]
        self.neg_doc_count = new_neg_percent

    def find_popularity(self):
        for word in self.pos_doc_count:
            value1 = self.pos_doc_count[word] / len(self.pos_all_words_raw)
            self.pos_popularity[word] = round(value1*100, 7)
        for word in self.neg_doc_count:
            value2 = self.neg_doc_count[word] / len(self.neg_all_words_raw)
            self.neg_popularity[word] = round(value2*100, 7)

    def find_information_value(self):
        for word in self.pos_doc_count:
            self.pos_information_value[word] = \
                round(self.pos_doc_count[word] / (len(self.pos_all_words_raw) + len(self.neg_all_words_raw)), 3)
        for word in self.neg_doc_count:
            self.neg_information_value[word] = \
                round(self.neg_doc_count[word] / (len(self.pos_all_words_raw) + len(self.neg_all_words_raw)), 3)

    def find_most_common(self):
        self.most_common_pos = sorted(self.pos_freq, key=self.pos_freq.get, reverse=True)[:25]
        self.most_common_neg = sorted(self.neg_freq, key=self.neg_freq.get, reverse=True)[:25]

    def find_highest_informational_value(self):
        self.pos_highest_inform_val = sorted(self.pos_information_value,
                                             key=self.pos_information_value.get, reverse=True)[:25]
        self.neg_highest_inform_val = sorted(self.neg_information_value,
                                             key=self.neg_information_value.get, reverse=True)[:25]

    def find_highest_pop_value(self):
        self.pos_highest_pop = sorted(self.pos_popularity, key=self.pos_popularity.get, reverse=True)[:25]
        self.neg_highest_pop = sorted(self.neg_popularity, key=self.neg_popularity.get, reverse=True)[:25]

    @staticmethod
    def list_files_in_directory(directory):
        return [f for f in listdir(directory) if isfile(join(directory, f))]

    def set_directory(self):
        directory = input('Train classifier in ALL or SUBSET?\n>> ').lower()
        while directory not in ('alle', 'all', 'sub', 'subset', 'a', 's', 'ss'):
            directory = input('Train classifier in ALL or SUBSET?\n>> ').lower()
        if directory in ('alle', 'all', 'a'):
            self.directory = paths.all_train
            print('Training in ALL')
        else:
            self.directory = paths.subset_train
            print('Training in: SUBSET')

    def __str__(self):
        ret = '-' * 250
        ret += '\nMOST COMMON:' + '\nP:\t' + str(self.most_common_pos) + '\nN:\t' + str(self.most_common_neg)
        ret += '\n' + '-' * 250
        ret += '\nPOPULARITY' + '\nP:\t' + str(self.pos_popularity) + '\nN:\t' + str(self.neg_popularity)
        ret += '\n' + '-' * 250
        ret += '\nHIGHEST POPULARITY' + '\nP:\t' + str(self.pos_highest_pop) + '\nN:\t' + str(self.neg_highest_pop)
        ret += '\n' + '-' * 250
        ret += '\nINFORMATIONAL VALUE' + '\nP:\t' + str(self.pos_information_value) +\
               '\nN:\t' + str(self.neg_information_value)
        ret += '\n' + '-' * 250
        ret += '\nHIGHEST INFORMATIONAL VALUE' + '\nP:\t' + str(self.pos_highest_inform_val) +\
               '\nN:\t' + str(self.neg_highest_inform_val)
        ret += '\n' + '-' * 250
        return ret
