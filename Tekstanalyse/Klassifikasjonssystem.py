from classifier import Classifier
import paths

from os import listdir
from os.path import isfile, join
from timeit import default_timer
from time import sleep
from sys import stdout


class Klassifikasjonssystem:

    def __init__(self, p=0.01175, n=1):

        directory, dir_string = self.set_directory()
        print('Classifying: ' + dir_string + '\n')

        self.t0 = default_timer()
        classifier = Classifier(p, n)

        pos_paths, neg_paths = self.find_directories(directory)
        total_docs = len(pos_paths) + len(neg_paths)

        if n > 1:
            self.t1 = default_timer()
            print()
            print('-' * 40)
            print(str(n) + '-GRAMS')
            print('NOT IMPLEMENTED')
            print('IN CLASSIFICATION')
            print('Time:\t\t\t\t\t\t' + str(round(self.t1-self.t0, 2)) + ' s')
            print('-'*40)
        else:
            self.checker(classifier, directory)
            correct = self.check_correctness(classifier)

            self.t1 = default_timer()
            sleep(0.2)
            print()
            print('-' * 40)
            print('Correct classifications:\t' + str(correct))
            print('Pruned with:\t\t\t\t' + str(round(p * 100, 3)) + ' %')
            print('Correctness:\t\t\t\t' + str(round(correct / total_docs * 100, 2)) + ' %')
            print('Time:\t\t\t\t\t\t' + str(round(self.t1 - self.t0, 2)) + ' s')
            print('-' * 40)

        ans = input('Print lists? y/n\n>> ')
        if ans == 'y':
            print(classifier)

    def checker(self, classifier, directory):
        pos_paths, neg_paths = self.find_directories(directory)
        total_docs = len(pos_paths) + len(neg_paths)

        checked = 0
        prev_progress = 1
        print()
        for path in pos_paths:
            classifier.check_document(path)
            checked += 1
            progress = str(int(checked / total_docs * 100))
            if progress != prev_progress:
                s = 'Testing progress:\t\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

        for path in neg_paths:
            classifier.check_document(path)
            checked += 1
            progress = str(int(checked / total_docs * 100))
            if progress != prev_progress:
                s = 'Testing progress:\t\t' + progress + ' %'
                stdout.write('\r' + s)
            prev_progress = progress

    @staticmethod
    def check_correctness(classifier):
        pos = 0
        neg = 0
        na = 0
        correct = 0
        # {doc1: (calculated_answer, correct_answer), doc2: (calculated_answer, correct_answer) ... }
        for x in classifier.all_measure_of_goodness:
            if classifier.all_measure_of_goodness[x][0] == 1:
                pos += 1
            elif classifier.all_measure_of_goodness[x][0] == -1:
                neg += 1
            else:
                na += 1
            if classifier.all_measure_of_goodness[x][0] == classifier.all_measure_of_goodness[x][-1]:
                correct += 1
        return correct

    @staticmethod
    def find_directories(directory):
        pos_path = directory + '/pos/'
        neg_path = directory + '/neg/'
        return [pos_path + f for f in listdir(pos_path) if isfile(join(pos_path, f))], \
               [neg_path + f for f in listdir(neg_path) if isfile(join(neg_path, f))]

    @staticmethod
    def set_directory():
        directory = input('-'*40 + '\nTest classifier in ALL or SUBSET?\n>> ').lower()
        while directory not in ('alle', 'all', 'sub', 'subset', 'a', 's', 'ss'):
            directory = input('Test reviews in ALL or in SUBSET?\n>> ').lower()
        if directory in ('alle', 'all', 'a'):
            return paths.all_test, 'ALL'
        else:
            return paths.subset_test, 'SUBSET'


if __name__ == '__main__':
    Klassifikasjonssystem(0.01175, 1)
