from confmat import BinaryConfusionMatrix
import utils
import os.path

def quality_score(tp, tn, fp, fn):
    return ((tp + tn) / (tp + tn + 10*fp + fn))

def compute_quality_for_corpus(corpus_dir):
    predictions_dict = {}
    truth_dict = {}
    final_dict = {}

    pred_path = os.path.join(corpus_dir, '!prediction.txt')
    truth_path = os.path.join(corpus_dir, '!truth.txt')

    predictions_dict = utils.read_classification_from_file(pred_path)
    truth_dict = utils.read_classification_from_file(truth_path)

    bm = BinaryConfusionMatrix(pos_tag="SPAM", neg_tag="OK")

    for key in predictions_dict.keys():
        bm.compute_from_dicts(truth_dict, predictions_dict)

    final_dict = bm.as_dict()

    return quality_score(final_dict['tp'], final_dict['tn'], final_dict['fp'], final_dict['fn'])

if __name__ == '__main__':
    print("uspesnost - %.2f%%" % (compute_quality_for_corpus('D:\ownCloud\RPH\spam_filter\emails\\1') * 100))