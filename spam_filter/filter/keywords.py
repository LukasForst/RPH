import copy


class Keywords:
    """
    class dealing with phrases that are common in the SPAMS
    phrases are saved in the 'keys.txt' formatted as a:

    {phrase} + '\t' + {value}

    value is number of occurrences in the training data
    """
    def __init__(self, path):
        self.path = path

    def get_dict(self):
        """
        :return: dictionary of keys with value
        """
        dict = {}
        with open(self.path, encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                phrase = line.split('\t') # phrase[0] - phrase, phrase[1] - value

                if(len(phrase) == 1):
                    dict[phrase[0]] = 0
                else:
                    dict[phrase[0]] = int(phrase[1])
        return dict

    def add_keyword(self, keyword, value):
        """
        :param keyword: phrase to be stored
        :param value: value of the phrase - number of occurrences in the spam training data
        """
        with open(self.path, mode='a', encoding='utf-8') as file:
            file.write(keyword + '\t' + value + '\n')

    def save_dictionary(self, dict = {}):
        """
        :param dict: dictionary to be stored
        """
        with open(self.path, mode='w', encoding='utf-8') as file:
            for key in dict.keys():
                file.write(key + '\t' + str(dict[key]) + '\n')

    def set_data_to(self, demanded_value):
        """
        this method will set all values to the 0
        this is mainly used for testing
        :param demanded_value - value that will get every phrase in the dictionary
        """
        keywords_dict = self.get_dict()

        with open(self.path, mode="w", encoding="utf-8") as file:
            for key in keywords_dict.keys():  # save very key in dictionary
                if ('\n' in key):  # there were some problems with empty keywords from some data sources
                    continue
                text = key + '\t' + str(demanded_value) + '\n'
                file.write(text)

    def edit_format(self, input_file):
        """
        method reads data from input_file, formats them and afterwards store then to the main - 'keys.txt'
        :param input_file: path to the file with not formatted data
        """
        with open(input_file, encoding='utf-8') as file:
            r = file.read()
            r = r.replace('\t', '\n').lower()  # removing case sensitivity and tabs

        with open(self.path, mode='w', encoding='utf-8') as file:
            file.write(r)

        dict = {}
        dict = self.get_dict()
        tmp_dict = copy.deepcopy(dict)

        for key in dict.keys():
            if( len(key.split()) == 1 ):
                if( len(key.split()[0]) < 5 ):
                    tmp_dict.pop(key, None)

        with open(self.path, mode='w', encoding='utf-8') as file:
            for key in tmp_dict.keys():
                file.write(key + '\n')

        self.set_data_to(1)  # assigning values to the phrases


if __name__ == '__main__':
    key = Keywords('keys.txt')
    #dict = key.get_dict()

    key.edit_format('temp_keys.txt')

    #key.set_data_to()
    #print("Nulled.")
    #dict = key.get_dict()
    #print(dict)