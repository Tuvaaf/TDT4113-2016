import os


__author__ = "Martin Langmo Karlstrøm"
__project__ = "Tekstanalyse"


# Locates /data folder and gets path.

data_path = os.path.join(os.path.dirname(__file__), 'data')

all_test = data_path + '/alle/test/'
all_train = data_path + '/alle/train/'
subset_test = data_path + '/subset/test/'
subset_train = data_path + '/subset/train/'

stop_words = os.path.join(os.path.dirname(__file__), 'stop_words.txt') + "/"
