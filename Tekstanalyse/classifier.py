from analyze import TrainerAnalyze
from reader import Reader

from collections import defaultdict
from math import log10


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Tekstanalyse"


class Classifier(TrainerAnalyze):

    def __init__(self, p=0.01175, n=1):
        super().__init__(p, n)
        self.document = []
        self.all_measure_of_goodness = defaultdict(int)

    def measure_goodness(self):
        pos_log_of_measure_of_goodness = 0
        neg_log_of_measure_of_goodness = 0

        for word in set(self.document):
            if word in self.pos_popularity:
                pos_log_of_measure_of_goodness += log10(self.pos_popularity[word])
            if word in self.neg_popularity:
                neg_log_of_measure_of_goodness += log10(self.neg_popularity[word])

        if pos_log_of_measure_of_goodness > neg_log_of_measure_of_goodness:
            return 1
        elif pos_log_of_measure_of_goodness < neg_log_of_measure_of_goodness:
            return -1
        else:
            return 0

    def check_document(self, path):
        formatted, pos_or_neg = self.format_path(path)
        self.document = self.get_document(path)
        goodness = self.measure_goodness()
        self.all_measure_of_goodness[formatted] = goodness, pos_or_neg

    def check_document_grams(self, doc):
        pass

    @staticmethod
    def format_path(path):
        l = path.split('/')
        val = 0
        if l[-2] == 'pos':
            val = 1
        elif l[-2] == 'neg':
            val = -1
        return l[-1], val

    @staticmethod
    def get_document(path):
        r = Reader()
        return r.default_read_from_file(path)
