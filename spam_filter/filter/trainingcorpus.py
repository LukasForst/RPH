import os.path
from corpus import Corpus


class TrainingCorpus:

    def __init__(self, dir_path):
        """
        :param dir_path: directory with emails
        """
        self.main_directory = dir_path
        self.truth_dict = {}  # dictionary that has name of the file as a key and tag as a value

        with open(os.path.join(dir_path, '!truth.txt'), encoding="utf-8") as file1:
            for line in file1:
                name = line.split()
                self.truth_dict[name[0]] = name[1]

    def get_class(self, file_name):
        """
        :param file_name: name of the email in the directory
        :return: spam tag - 'OK' or 'SPAM'
        """
        return self.truth_dict[file_name]

    def is_ham(self, file_name):
        """
        :param file_name: name of the email in the directory
        :return: True whether it is HAM, False if not
        """
        if( self.truth_dict[file_name] == 'OK' ):
            return True
        else:
            return False

    def is_spam(self, file_name):
        """
        :param file_name: name of the email in the directory
        :return: True whether it is SPAM, False if not
        """
        if (self.truth_dict[file_name] == 'SPAM'):
            return True
        else:
            return False

    def spams(self):
        """
        :returns - every SPAM in the directory - body and the name
        """
        c = Corpus(self.main_directory)
        for key in self.truth_dict.keys():
            if(self.truth_dict[key] == 'SPAM'):
                yield (key, c.get_body(key))

    def hams(self):
        """
        :returns - every HAM in the directory - body and the name
        """
        c = Corpus(self.main_directory)
        for key in self.truth_dict.keys():
            if(self.truth_dict[key] == 'OK'):
                yield (key, c.get_body(key))