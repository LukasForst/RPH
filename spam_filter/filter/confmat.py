class BinaryConfusionMatrix:

    def __init__(self, pos_tag, neg_tag):
        self.TP = 0  # true positives
        self.TN = 0  # true negatives
        self.FP = 0  # false positives
        self.FN = 0  # false negatives

        self.pos_tag = pos_tag
        self.neg_tag = neg_tag

    def as_dict(self):
        """
        :return: dictionary with tag tp, tn, fp, fn
        """
        return {'tp':self.TP, 'tn':self.TN, 'fp':self.FP, 'fn': self.FN}

    def update(self, truth, prediction):
        if(truth not in (self.pos_tag, self.neg_tag)):
            raise ValueError("Wrong truth tags.")
        if(prediction not in (self.pos_tag, self.neg_tag)):
            raise ValueError("Wrong prediction tags.")

        if(prediction == truth):
            if(self.pos_tag == prediction):
                self.TP += 1
            if(self.neg_tag == prediction):
                self.TN += 1
        else:
            if(prediction == self.pos_tag):
                self.FP += 1
            if(prediction == self.neg_tag):
                self.FN += 1

    def compute_from_dicts(self, truth_dict = {}, pred_dict = {}):
        if(truth_dict.keys() != pred_dict.keys()):
            raise ValueError("Wrong size of dictionaries!")

        for key in truth_dict.keys():
            self.update(truth_dict[key], pred_dict[key])

    def check_value_of(self, truth):
            if (truth not in (self.pos_tag, self.neg_tag)):
                raise ValueError("Wrong tag - tags should be either %s or %s.", self.neg_tag, self.pos_tag)


if __name__ == '__main__':
    cm1 = BinaryConfusionMatrix(pos_tag=True, neg_tag=False)

    cm1.compute_from_dicts({'a': True, 'b': False}, {'a':True, 'b':True})
    cm1.update(True, True)
    print(cm1.as_dict())



