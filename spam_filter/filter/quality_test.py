from keywords import Keywords
from filter import MyFilter
from trainingcorpus import TrainingCorpus
import time
import quality


class Training:

    def __init__(self):

        self.a = MyFilter()

    def training(self, data_set):
        start_time = time.time()

        k = Keywords('keys.txt')
        k.edit_format('temp_keys.txt')
        k.set_data_to(data_set)

        self.a.train('D:\ownCloud\RPH\spam_filter\emails\\1')
        print("First training DONE.")
        self.a.train('D:\ownCloud\RPH\spam_filter\emails\\2')
        print("Second training DONE.")

        print("traing: {:.2f}s".format(time.time() - start_time))

    def testing(self, sensitivity):
        start_time = time.time()

        self.a.filter_sensitivity = sensitivity

        path1 = 'D:\ownCloud\RPH\spam_filter\emails\\1'
        path2 = 'D:\ownCloud\RPH\spam_filter\emails\\2'

        path1 = "/media/lukas/Data/OneDrive/ownCloud/RPH/spam_filter/emails/1"
        path2 = "/media/lukas/Data/OneDrive/ownCloud/RPH/spam_filter/emails/2"

        self.a.test(path1)
        print("\nuspesnost 1 - %.2f%%" % (quality.compute_quality_for_corpus(path1) * 100))

        jedna = TrainingCorpus(path1)
        tmp1 = 0
        tmp2 = 0
        for q in jedna.spams():
            tmp1 += 1
        for q in jedna.hams():
            tmp2 += 1


        print("oznaceno jako spam - %d" % (self.a.spams))
        print("skutecny spam      - %d" % (tmp1))
        print("oznaceno jako ham  - %d" % (self.a.hams))
        print("skutecny ham       - %d" % (tmp2))

        self.a.test(path2)

        print("\nuspesnost 2 - %.2f%%" % (quality.compute_quality_for_corpus(path2) * 100))
        jedna = TrainingCorpus(path1)
        tmp1 = 0
        tmp2 = 0
        for q in jedna.spams():
            tmp1 += 1
        for q in jedna.hams():
            tmp2 += 1

        print("oznaceno jako spam - %d" % (self.a.spams))
        print("skutecny spam      - %d" % (tmp1))
        print("oznaceno jako ham  - %d" % (self.a.hams))
        print("skutecny ham       - %d" % (tmp2))

        print("\nevaluating: {:.3f}s".format(time.time() - start_time))

    def mult_train(self, sensitivity, data_set):
        #self.training(data_set)

        self.a.filter_sensitivity = sensitivity

        path1 = 'D:\ownCloud\RPH\spam_filter\emails\\1'
        path2 = 'D:\ownCloud\RPH\spam_filter\emails\\2'

        path1 = "/media/lukas/Data/OneDrive/ownCloud/RPH/spam_filter/emails/1"
        path2 = "/media/lukas/Data/OneDrive/ownCloud/RPH/spam_filter/emails/2"

        self.a.test(path1)

        result1  = quality.compute_quality_for_corpus(path1) * 100

        self.a.test(path2)

        result2 = quality.compute_quality_for_corpus(path2) * 100

        return ((result1+result2) / 2)

    def para_test(self, training, multi, since, to, step, sensitivity, data_set):
        train = Training()

        if (training):
            train.training(data_set)

        if (multi):
            tmp_i = 0
            tmp_value = 0

            i = since
            while (i < to):
                q = train.mult_train(i, data_set)
                if (q > tmp_value):
                    tmp_value = q
                    tmp_i = i
                print("%d - %.2f%%" % (i, q))
                i += step

            print("\n\nFinal sensitivity is - %2d with - %.2f%%" % (tmp_i, tmp_value))
        else:
            train.testing(sensitivity)
            print("\nSensitivity = " + str(sensitivity))

if __name__ == '__main__':

    sensitivity = 221
    data_set = 1

    training = False
    multi = False

    since = 299
    to = 600
    step = 2

    a = Training()
    a.para_test(training, multi, since, to, step, sensitivity, data_set)