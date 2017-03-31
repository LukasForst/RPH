from trainingcorpus import TrainingCorpus
from keywords import Keywords
from corpus import Corpus
import time
import copy


class MyFilter:

    filter_sensitivity = 221  # effective range is 200-1000 - best results around 220

    def __init__(self):
        self.keywords_class = Keywords('keys.txt')  # module with keywords
        self.spam_words_dict = {}
        self.spam_words_dict = self.keywords_class.get_dict()  # dictionary with keywords and their value
        self.spams = 0  # detected spams - used for testing
        self.hams = 0  # detected hams - used gor testing

    def train(self, dir_path):
        """
        :param dir_path: directory with emails
        :effect - updates used keywords in the 'keys.txt'
        :return: void
        """
        train_corpus = TrainingCorpus(dir_path)

        for spam in train_corpus.spams():
            body = spam[1].lower()  # removing case sensitivity

            for key in self.spam_words_dict.keys():  # testing every phrase in the keys
                if(key in body and self.spam_words_dict[key] < 100):  # limit for one single word
                    self.spam_words_dict[key] += 1

        tmp_dict = {}
        tmp_dict = copy.deepcopy(self.spam_words_dict)

        for ham in train_corpus.hams():
            body = ham[1].lower()  # removing case sensitivity

            for key in self.spam_words_dict.keys():
                if(key in body):
                    tmp_dict[key] -= 5

        for key in self.spam_words_dict.keys():
            if (self.spam_words_dict[key] < 0):
                tmp_dict.pop(key, None)  # effort to reduce FP cases, removing phrases that are common in hams

        self.spam_words_dict = tmp_dict  # updating main dict with new one
        self.keywords_class.save_dictionary(self.spam_words_dict)  # saving trained dictionary with values

    def test(self, dir_path):
        """
        :param - path to the directory with mails - '!truth.txt' won't be there
        :effect - method will create file '!prediction.txt' in the directory
        :return - void
        """
        corp = Corpus(dir_path)
        conclusion = {}  # final dictionary with file names and marks SPAM/OK
        self.spams = 0  # used mainly for testing
        self.hams = 0   # used mainly for testing

        spam_trap = "spamtrap"
        for email in corp.emails():  # going though all emails in the directory
            file_name = email[0]
            body = email[1]
            value_of_keywords = 0

            if spam_trap in body:
                conclusion[file_name] = "SPAM"
                continue

            for key in self.spam_words_dict.keys():  # going though all phrases in the dictionary
                if( key in body ):  # body contains phrase substring
                    value_of_keywords += self.spam_words_dict[key]
                    value_of_keywords += 1

                if (value_of_keywords >= self.filter_sensitivity):  # filter sensitivity
                    conclusion[file_name] = "SPAM"
                    self.spams += 1
                    break  # breaks when it is marked as a spam
                else:
                    continue

            if(value_of_keywords < self.filter_sensitivity):  # not spam
                conclusion[file_name] = "OK"
                self.hams += 1

        corp.save_conclusion(conclusion)  # save final dict to the file

if __name__ == '__main__':
    """
    start_time = time.time()

    k = Keywords('keys.txt')
    k.set_data_to(1)

    a = MyFilter()
    a.train('D:\OneDrive\ownCloud\RPH\spam_filter\emails\\1')
    a.train('D:\OneDrive\ownCloud\RPH\spam_filter\emails\\2')

    print("\ntime elapsed: {:.5f}s".format(time.time() - start_time))
    """
    a = MyFilter()
    a.train('/media/lukas/Data/OneDrive/ownCloud/RPH/spam_filter/emails/1')

